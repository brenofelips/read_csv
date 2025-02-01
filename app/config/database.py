import pyscopg2
from dotenv import load_dotenv

from environment import (
    get_db_host,
    get_db_name,
    get_db_user,
    get_db_password
)

def get_connection() -> psycopg2.extensions.connection:
    load_dotenv()
    return psycopg2.connect(
        host=get_db_host(),
        database=get_db_name(),
        user=get_db_user(),
        password=get_db_password()
    )