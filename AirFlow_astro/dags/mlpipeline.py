from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime




#define task 1


def preprocess_data():
    print("Preprocessing data")

#define task 2
def train_model():
    print("Training model")

#define task 3

def evaluate_model():
    print("Evaluating model")

#define task 4

def deploy_model():
    print("Deploying model")



#defining DAG 


with DAG(
    'ml_pipeline',
    start_date=datetime(2026,1,1),
    schedule='@weekly'
) as dag:

    #define the task 
    preprocess= PythonOperator(
        task_id='preprocess_task',python_callable=preprocess_data)
    train= PythonOperator(
        task_id='train_task',python_callable=train_model)
    evaluate= PythonOperator(
        task_id='evaluate_task',python_callable=evaluate_model)
    deploy= PythonOperator(
        task_id='deploy_task',python_callable=deploy_model)



    #set dependecies 

    preprocess >> train >> evaluate >> deploy         