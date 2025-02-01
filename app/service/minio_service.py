from minio import Minio
from app.config.environment import (
    get_minio_root_user,
    get_minio_root_password
)

minio_client = Minio(
"localhost:9000",
    access_key=get_minio_root_user(),
    secret_key=get_minio_root_password(),
    secure=False
)

def upload_file(bucket_name, file_path, object_name):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"Arquivo {object_name} subido para o bucket {bucket_name}.")
    except Exception as e:
        print(f"Erro ao subir o arquivo: -> {e}")

def download_file(bucket_name, object_name, file_path):
   try:
       minio_client.fget_object(bucket_name, object_name, file_path)
       print(f"Arquivo {object_name} baixado para {file_path}.")
   except Exception as e:
       print(f"Erro ao baixar o arquivo: -> {e}")