from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


#define dag 

with DAG(
    dag_id='BashOperator_DAG',
    start_date=datetime(2024,9,19),
    schedule='@daily',
    description='BashOperator Example',
    tags=['BashOperator Example'],
    catchup=False
):
    bash_task = BashOperator(task_id='bash_task', bash_command='echo "Hello world"')



