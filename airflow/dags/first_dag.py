from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
# from zoneinfo import ZoneInfo

def print_header(ti, **context):
    
    f = open("out.txt", "a")
    f.write("================================\n")
    f.write(f"Running DAG @{datetime.now() + timedelta(hours=5, minutes=30)}\n")
    f.close()
    
    return 'Hello world from first Airflow DAG!'

def print_body(ti, **context):
    
    f=open("out.txt", "a")
    f.write(f"Message: {context['dag_run'].conf['message']}\n")

def print_footer(ti, **context):
    f = open("out.txt", "a")
    f.write(f"Cleaning up @{datetime.now() + timedelta(hours=5, minutes=30)}\n")
    f.write("================================\n")
    f.close()

with DAG(
    'hello_world', 
    description='Hello World DAG!',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017, 3, 20), catchup=False
    ) as dag:

    task_1 = PythonOperator(task_id='header_task', python_callable=print_header)
    task_2 = PythonOperator(task_id='body_task', python_callable=print_body)
    task_3 = PythonOperator(task_id='footer_task', python_callable=print_footer)
    
    task_1 >> task_2 >> task_3