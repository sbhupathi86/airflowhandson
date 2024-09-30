from airflow import DAG
from airflow.sensors.python import PythonSensor
from datetime import datetime 


# define a func

def _passvalue():
    return False

#define dag

with DAG(
    dag_id='Sensor_Demo_Dag1',
    start_date=datetime(2024,9,24),
    catchup=False, 
    schedule='@daily'
):
    
    check_condition_task = PythonSensor(
        task_id= 'check_condition_task',
        python_callable=_passvalue,
        poke_interval=5,
        timeout=7*24*60*60
    )


