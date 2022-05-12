from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
# from zoneinfo import ZoneInfo

def print_hello(ti, **context):
    
    f = open("out.txt", "a")
    f.write(f"{datetime.now() + timedelta(hours=5, minutes=30)} - Hello World! {context['dag_run'].conf['key']}\n")
    f.close()
    
    return 'Hello world from first Airflow DAG!'

with DAG(
    'hello_world', 
    description='Hello World DAG!',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017, 3, 20), catchup=False
    ) as dag:

    task_1 = PythonOperator(task_id='hello_task', python_callable=print_hello)