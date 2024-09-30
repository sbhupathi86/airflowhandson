from airflow import DAG
from airflow.decorators import task 
from datetime import datetime 


with DAG(dag_id='xcom_test_dag',
         start_date=datetime(2024,9,20),
         description='Dag to define xcom explicitly',
         tags=['xcom'],
         schedule_interval='@daily',
         catchup=False
        )as dag:
    
    @task
    def peter_task(ti=None):
        ti.xcom_push(key='mobile_phone',value='iPhone')
    
    @task
    def bryan_task(ti=None):
        phone = ti.xcom_pull(task_ids='peter_task',key='mobile_phone')
        print(f"phone is",phone)

    peter_task() >> bryan_task()    
