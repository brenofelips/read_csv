from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from app.service.minio_service import upload_file, download_file

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
    'minio_dag',
    default_args=default_args,
    description='A simple DAG to upload and download files from Minio',
    schedule_interval=timedelta(days=1),
)

upload_task = PythonOperator(
    task_id='upload_file',
    python_callable=upload_file,
    op_kwargs={'bucket_name': 'my-bucket', 'file_path': '/path/to/local/file', 'object_name': 'uploaded_file'},
    dag=dag,
)

download_task = PythonOperator(
    task_id='download_file',
    python_callable=download_file,
    op_kwargs={'bucket_name': 'my-bucket', 'object_name': 'uploaded_file', 'file_path': '/path/to/download/file'},
    dag=dag,
)

upload_task >> download_task