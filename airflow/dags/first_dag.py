from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
# from zoneinfo import ZoneInfo

def print_hello(ti, **context):
    
    f = open("out.txt", "a")
    f.write(f"{datetime.now() + timedelta(hours=5, minutes=30)} - Hello World!\n")
    f.close()
    
    return 'Hello world from first Airflow DAG!'

dag = DAG('hello_world', description='Hello World DAG!',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator