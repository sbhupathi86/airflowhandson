from airflow import DAG
from datetime import datetime 
from my_packages.packages_a.module_a  import TestClass
from airflow.operators.python import PythonOperator

def test_module():
    print(TestClass.my_time())

with DAG(
    dag_id='relative path dag',
    start_date= datetime(2024,9,24),
    catchup=False
):
    
    pytask = PythonOperator(
        task_id = 'pytask',
        python_callable=test_module()
    )

    pytask
