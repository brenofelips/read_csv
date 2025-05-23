import os
from dotenv import load_dotenv

load_dotenv()


def get_db_host() -> str:
    return os.environ.get('DB_HOST')


def get_db_name() -> str:
    return os.environ.get('DB_NAME')


def get_db_user() -> str:
    return os.environ.get('DB_USER')


def get_db_password() -> str:
    return os.environ.get('DB_PASSWORD')


def get_minio_root_user() -> str:
    return os.environ.get('MINIO_ROOT_USER')


def get_minio_root_password() -> str:
    return os.environ.get('MINIO_ROOT_PASSWORD')
