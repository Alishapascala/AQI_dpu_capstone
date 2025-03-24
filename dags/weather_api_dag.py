from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone

import requests


def _get_weather_data():
    API_KEY = "7d4d4878-78f0-4520-8106-b8dafd61a9f8"
    # API_KEY = os.environ.get("WEATHER_API_KEY")
    # API_KEY = Variable.get("weather_api_key")

    payload = {
        "q": "bangkok",
        "appid": API_KEY,
        "units": "metric"
    }
    url = "http://api.airvisual.com/v2"
    response = requests.get(url, params=payload)
    print(response.url)

    data = response.json()
    print(data)


with DAG(
    "get_weather_api_dag",
    schedule="@hourly",
    start_date=timezone.datetime(2025, 3, 24),
    tags = ["dpu"]
):
    start = EmptyOperator(task_id="start")

    get_weather_data = PythonOperator(
        task_id="get_weather_data",
        python_callable=_get_weather_data,
    )

    end = EmptyOperator(task_id="end")

    start >> get_weather_data >> end 

 