from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from app.service.minio_service import download_file
from app.service.csv_service import read_csv
from app.service.db_service import save_to_db

default_args = {
    'owner': 'brenofelips',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'process_csv_dag',
    default_args=default_args,
    description='A DAG to download a CSV file from Minio, read it, and save the data to the database',
    schedule_interval=timedelta(days=1),
)

def process_csv(**kwargs):
    bucket_name = kwargs['bucket_name']
    object_name = kwargs['object_name']
    download_path = kwargs['download_path']

    download_file(bucket_name, object_name, download_path)
    df = read_csv(download_path)
    save_to_db(df)

process_task = PythonOperator(
    task_id='process_csv',
    python_callable=process_csv,
    op_kwargs={
        'bucket_name': 'my-bucket',
        'object_name': 'uploaded_file.csv',
        'download_path': '/path/to/download/file.csv'
    },
    dag=dag,
)