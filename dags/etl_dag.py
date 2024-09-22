from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.http.sensors.http import HttpSensor
import os

os.environ['NO_PROXY'] = '*'

import requests
import json
import psycopg2


default_args = {
    'owners': 'airflow',
    'depends_on_past': False,
    'start_date':datetime(2024, 9, 14),
    'max_active_runs': 1,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule':'@once',
    'schedule_interval':'@daily',
}

base_url = 'http://host.docker.internal:8000/'

@dag(
    dag_id='etl_dag',
    catchup=False,
    default_args=default_args,
    description='etl dag to extract-transform-load data'
)
def etl_dag():
    @task()
    def extract_orders_api(ti):
        response = requests.get('http://host.docker.internal:8000/generate_data/orders', timeout=10)
        data = response.json()
        return data
    
    @task()
    def extract_customers_api(ti):
        response = requests.get('http://host.docker.internal:8000/generate_data/customers', timeout=10)
        data = response.json()
        return data
    
    @task()
    def extract_products_api(ti):
        response = requests.get('http://host.docker.internal:8000/generate_data/products')
        data = response.json()
        return data
    
    customers_data = extract_customers_api()
    products_data = extract_products_api()
    orders_data = extract_orders_api()
    
    @task()
    def transform():
        # Apply transformation logic
        pass
    
    @task()
    def load(ti):
        customers_xcomarg = ti.xcom_pull(key='return_value', task_ids='extract_customers_api')
        products_xcomarg = ti.xcom_pull(key='return_value', task_ids='extract_products_api')
        orders_xcomarg = ti.xcom_pull(key='return_value', task_ids='extract_orders_api')
        
        customers_data = json.loads(r"{}".format(customers_xcomarg.__str__().replace("\'", "\"")))
        products_data = json.loads(r"{}".format(products_xcomarg.__str__().replace("\'", "\"")))
        orders_data = json.loads(r"{}".format(orders_xcomarg.__str__().replace("\'", "\"")))
        connection = psycopg2.connect(
            dbname='cdp',
            user='airflow',
            password='airflow',
            host='host.docker.internal',
            port=54320
        )
        
        print("db ok")
        print(customers_data[1])
        print(customers_data[2])
        cursor = connection.cursor()
        for customer in customers_data:
            cursor.execute("""
                           INSERT INTO CUSTOMER(cust_id, name, sex, age, address, phone, job)
                           VALUES(%s, %s, %s, %s ,%s ,%s, %s);
                           INSERT INTO SUM(cust_id, count, sum)
                           VALUES(%s, 0, 0)""",
                           (customer['cust_id'], customer['name'], customer['sex'], customer['age'], customer['address'], customer['phone'], customer['job'], customer['cust_id']))
            
        for product in products_data:
            cursor.execute("""
                           INSERT INTO PRODUCT(prod_id, name, price)
                           VALUES(%s, %s, %s)""",
                           (product['prod_id'], product['name'], product['price']))
            
        for order in orders_data:
            cursor.execute("""
                           INSERT INTO ORDERS(ord_id, cust_id, prod_id, count)
                           VALUES(%s, %s, %s, %s);
                           
                           UPDATE SUM s
                           SET count = count + %s,
                           sum = sum + %s * p.price
                           FROM PRODUCT p
                           WHERE p.prod_id = %s
                           AND s.cust_id = %s""",
                           (order['ord_id'], order['cust_id'], order['prod_id'], order['count'], order['count'], order['count'], order['prod_id'], order['cust_id']))
            
        connection.commit()
        cursor.close()
        connection.close()
    
    bash_echo = BashOperator(
        task_id='echo_task',
        bash_command='echo Successfully'
    )
    
    [customers_data, products_data] >> orders_data >> transform() >> load() >> bash_echo

etl_dag()
    