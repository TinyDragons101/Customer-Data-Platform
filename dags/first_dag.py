from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

default_args = {
    'owners': 'airflow',
    'retries': 5,
    'rery_delay': timedelta(minutes=1)
}

@dag(
    dag_id='first_dag',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2024, 9, 14),
    schedule='@daily'
)
def first_def():
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is my first task'
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey am task 2 and will be running after task 1'
    )
    
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo this is task 3 and i will run after task 1'
    )
    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    
    # task1 >> task2
    # task1 >> task3
    
    task1 >> [task2, task3]
    
first_def()
