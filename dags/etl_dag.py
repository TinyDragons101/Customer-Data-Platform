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
    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='http_localhost',
        endpoint='generate_data/customers'
    )
    
    @task()
    def extract_order_api():
        response = requests.get('http://host.docker.internal:8000/generate_data/orders', timeout=10)
        data = response.json()
        with open('../data/raw_data/raw_orders.json', 'w') as f:
            json.dump(data, f)
    
    @task()
    def extract_customers_api():
        response = requests.get('http://host.docker.internal:8000/generate_data/customers', timeout=10)
        data = response.json()
        with open('../data/raw_data/raw_customers.json', 'w') as f:
            json.dump(data, f)
    
    @task()
    def extract_products_api():
        response = requests.get('http://host.docker.internal:8000/generate_data/products')
        data = response.json()
        with open('../data/raw_data/raw_products.json', 'w') as f:
            json.dump(data, f)
    
    @task()
    def transform():
        with open('../data/raw_data/raw_customers.json') as f:
            customers_data = json.load(f)
        with open('../data/raw_data/raw_products.json') as f:
            products_data = json.load(f)
        with open('../data/raw_data/raw_orders.json') as f:
            orders_data = json.load(f)
        
        # Apply transformation logic
        transformed_customers_data = customers_data
        transformed_products_data =  products_data
        transformed_orders_data = orders_data
        
        with open('../data/raw_data/transformed_customers.json', 'w') as f:
            json.dump(transformed_customers_data, f)
        with open('../data/raw_data/transformed_products.json', 'w') as f:
            json.dump(transformed_products_data, f)
        with open('../data/raw_data/transformed_orders.json', 'w') as f:
            json.dump(transformed_orders_data, f)
        
    @task()
    def load():
        with open('../data/raw_data/transformed_customers.json') as f:
            customers_data = json.load(f)
        with open('../data/raw_data/transformed_products.json') as f:
            products_data = json.load(f)
        with open('../data/raw_data/transformed_orders.json') as f:
            orders_data = json.load(f)
        
        connection = psycopg2.connect(
            dbname='cdp',
            user='airflow',
            password='airflow',
            host='localhost'
        )
        
        cursor = connection.cursor()
        for customer in customers_data:
            cursor.execute("""
                           INSERT INTO CUSTOMER(cust_id, name, sex, age, address, phone, job)
                           VALUES(%s, %s, %s, %s ,%s ,%s, %s)""",
                           (customer['cust_id'], customer['name'], customer['sex'], customer['age'], customer['address'], customer['phone'], customer['job']))
            
        for product in products_data:
            cursor.execute("""
                           INSERT INTO PRODUCT(prod_id, name, price)
                           VALUE(%s, %s, %s)""",
                           (product['prod_id'], product['name'], product['price']))
            
        for order in orders_data:
            cursor.execute("""
                           INSERT INTO ORDERS(ord_id, cust_id, prod_id, count)
                           VALUES(%s, %s, %s)""",
                           (order['ord_id'], order['cust_id'], order['prod_id'], order['count']))
            
        connection.commit()
        cursor.close()
        connection.close()
        
    bash_echo = BashOperator(
        task_id='echo_task',
        bash_command='echo created table successfully'
    )
    
    extract_customers_api() >> extract_products_api() >> extract_order_api() >> transform() >> load() >> bash_echo

etl_dag()
    