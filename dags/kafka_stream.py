from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

def stream_data():
    res = requests.get('https://randomuser.me/api/')
    res = res.json()['results'][0]
    print(json.dumps(res, indent=3))

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()
