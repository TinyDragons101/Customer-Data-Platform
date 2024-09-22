from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owners': 'airflow',
    'depends_on_past': False,
    'start_date':datetime(2024, 9, 14),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule':'@once',
    'schedule_interval':'@daily',
}

@dag(
    dag_id='create_table_dag',
    catchup=False,
    default_args=default_args,
    description='dag to create table in database'
)
def create_table_dag():
    create_customer_table = SQLExecuteQueryOperator(
        task_id='create_customer_table',
        conn_id="postgres_localhost",
        sql="sql/create_customer_table.sql"
    )
    
    create_product_table = SQLExecuteQueryOperator(
        task_id='create_product_table',
        conn_id="postgres_localhost",
        sql="sql/create_product_table.sql"
    )
    
    create_order_table = SQLExecuteQueryOperator(
        task_id='create_order_table',
        conn_id="postgres_localhost",
        sql="sql/create_order_table.sql"
    )
    
    create_sum_table = SQLExecuteQueryOperator(
        task_id='create_sum_table',
        conn_id='postgres_localhost',
        sql='sql/create_sum_table.sql'
    )
    
    bash_echo = BashOperator(
        task_id='echo_task',
        bash_command='echo created table successfully'
    )
    
    [create_customer_table, create_product_table, create_order_table, create_sum_table] >> bash_echo

create_table_dag()
    