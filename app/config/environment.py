import os

def get_db_host() -> str:
    return os.environ.get('DB_HOST')

def get_db_name() -> str:
    return os.environ.get('DB_NAME')

def get_db_user() -> str:
    return os.environ.get('DB_USER')

def get_db_password() -> str:
    return os.environ.get('DB_PASSWORD')