from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

#define a python function 

def print_hello():
    print("hello world") 

#Define DAG

with DAG(
    'PythonOperator_DAG',
    start_date=datetime(2024,9,19),
    description='Example1 DAG',
    catchup=False,
    schedule='@daily',
    tags = ['initial learning']
):
    pytask = PythonOperator( 
        task_id='pytask',
        python_callable=print_hello
    )
