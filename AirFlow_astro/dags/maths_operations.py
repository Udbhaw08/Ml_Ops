"""

task 1 - start with inital number
task 2- add 5 to the number 
task 3 - multiply the result by 3 
task 4 - subtract 3 from the result 
task 5 - compute the square of the result 

"""

from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime


##define function for each task 

def start_number(**context):
    
    context["ti"].xcom_push(key="current_value", value = 10)
    print("starting number 10")



def add_five(**context):

    current_value = context["ti"].xcom_pull(key="current_value",task_ids='start_task')
    new_value=current_value + 5
    context["ti"].xcom_push(key="current_value", value = new_value)
    print(f"number after adding 5 is {new_value}")
    


def multiply_by_two(**context):
    current_value = context["ti"].xcom_pull(key="current_value",task_ids='add_five_task')
    new_value=current_value * 2
    context["ti"].xcom_push(key="current_value", value = new_value)  
    print(f"number after multiplying by two is {new_value}")



def subtract_by_three(**context):
    current_value = context["ti"].xcom_pull(key="current_value",task_ids='multiply_by_two_task')
    new_value = current_value - 3
    context["ti"].xcom_push(key="current_value", value = new_value)  
    print(f"number after subtracting three is {new_value}")


def square_the_number(**context):
    current_value = context["ti"].xcom_pull(key="current_value",task_ids='subtract_by_three_task')
    new_value = current_value * current_value
    context["ti"].xcom_push(key="current_value", value = new_value)  
    print(f"number after squaring is {new_value}")       




#define the DAG


with DAG(
    dag_id='maths_operation_dag',
    start_date=datetime(2023,1,1),
    schedule='@once',
    catchup=False
) as dag:
    ##define the task 

    start_task=PythonOperator(
        task_id='start_task',
        python_callable=start_number,
        
    )
    
    add_five_task=PythonOperator(
        task_id='add_five_task',
        python_callable=add_five,
        
    )
    
    multiply_by_two_task=PythonOperator(
        task_id='multiply_by_two_task',
        python_callable=multiply_by_two,
    )
    
    subtract_by_three_task=PythonOperator(
        task_id='subtract_by_three_task',
        python_callable=subtract_by_three,
    )
    
    square_the_number_task=PythonOperator(
        task_id='square_the_number_task',
        python_callable=square_the_number,
        )

    #define the dependencies 
    start_task >> add_five_task >> multiply_by_two_task >> subtract_by_three_task >> square_the_number_task