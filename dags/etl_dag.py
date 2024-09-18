from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
    'owners': 'airflow',
    'depends_on_past': False,
    'start_date':datetime(2024, 9, 14),
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'schedule':'@daily',
    'schedule_interval':'@daily',
}

@dag(
    dag_id='etl_dag',
    catchup=False,
    default_args=default_args,
    description='etl dag to extract - transform - load data'
)
def extract():
    # Logic to extract data from an API
    pass

def transform():
    # Logic to transform the data
    pass

def load():
    # Logic to load data into a database
    pass

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load,
    dag=dag,
)

# Setting the task dependencies
extract_task >> transform_task >> load_task
    