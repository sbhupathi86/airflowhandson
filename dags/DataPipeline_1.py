from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime 


#python function 
def read_file():
    print(open('/tmp/dummy.txt', 'rb').read())




#define DAG 

with DAG(
    dag_id='DataPipeline_1',
    start_date=datetime(2024,9,19),
    description='Simple Data pipeline',
    catchup=False,
    tags=['Data Pipeline'],
    schedule='@daily'
):
    
    create_file = BashOperator(task_id='create_file',
                          bash_command= 'echo "Hi there" > /tmp/dummy.txt')
    
    check_file_exists = BashOperator(task_id='check_file_exists',
                                     bash_command='test -f /tmp/dummy.txt')
    
    read_file = PythonOperator(
        task_id='read_file',
        python_callable=read_file
    )

    create_file >> check_file_exists >> read_file
    

