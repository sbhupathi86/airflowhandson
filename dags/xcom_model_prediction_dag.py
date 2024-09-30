from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from random import uniform


#define python functins

def _training_model(ti):
    accuracy = uniform(0.1,10.0)
    print(f"model accuracy is: ",accuracy)
    ti.xcom_push(key='model_accuracy', value=accuracy)
    # return accuracy
    

def _choose_best_model(ti):
    fetched_accuracy = ti.xcom_pull(key='model_accuracy',task_ids=['training_model_A','training_model_B','training_model_C'])
    print(f"choose best model: ",fetched_accuracy)

with DAG(
    dag_id='xcom_pick_accurate_model',
    start_date=datetime(2024,9,20),
    catchup=False,
    description='Xcom Dag to choose accurate model',
    tags=['xcom dag'],
    schedule='@daily'
):
    
    downloding_data = BashOperator(task_id='downloading_data',
                                   bash_command='echo "Hello there!. Welcome to XCOM play"',
                                   do_xcom_push=True
                                   )
    
    training_model_task = [PythonOperator(
        task_id = f'training_model_{task}',
        python_callable=_training_model

    ) for task in ['A','B','C']]

    choose_model = PythonOperator(
        task_id = 'choose_model',
        python_callable=_choose_best_model
    )

    downloding_data >> training_model_task >> choose_model



