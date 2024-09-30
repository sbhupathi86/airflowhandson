from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime 
import requests

#define python function to import data from API.
# since we are using Xcom, its important to pass task instance (ti) into the function.

def _transform(ti):
    resp = requests.get('https://swapi.dev/api/people/1').json()
    print(resp)
    print(f"type of response:", type(resp))

    my_character ={}
    print(type(my_character))
    my_character['height'] = int(resp['height'])-20
    my_character["mass"] = int(resp["mass"]) - 50
    my_character["hair_color"] = "black" if resp["hair_color"] == "blond" else "blond"
    my_character["eye_color"] = "hazel" if resp["eye_color"] == "blue" else "blue"
    my_character["gender"] = "female" if resp["gender"] == "male" else "female"
    #push task instance by assigning a key
    ti.xcom_push("character_info", my_character)

#define python function to receive the xcom_push sent

def _load(ti):
    a=ti.xcom_pull(key="character_info", task_ids='_transform')
    print(a)


#define a dag 
with DAG(dag_id='xcom_dag2',
         start_date=datetime(2024,9,24),
         catchup=False,
         description='xcom push/pull example',
         tags=['xcom demo'],
         schedule='@daily'
         ):
    
    task_xcom_push = PythonOperator(
            task_id = 'task_xcom_push',
            python_callable=_transform
    )

    task_xcom_pull = PythonOperator(
        task_id = 'task_xcom_pull',
        python_callable=_transform
    )

#define task dependency
    task_xcom_push >> task_xcom_pull 
    


