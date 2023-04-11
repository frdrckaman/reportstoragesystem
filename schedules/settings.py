from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import os
from pathlib import Path
import environ
import pymysql

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    RSS_PR=(bool, False),
    RSS_DR=(bool, False),
    RSS_UAT=(bool, False),
)

environ.Env.read_env(ENV_DIR)

RSS_SERVER = env.str("RSS_SERVER_PR01")
RSS_USERNAME = env.str("RSS_USERNAME")
RSS_PASSWORD = env.str("RSS_PASSWORD")
RSS_DB = env.str("RSS_DB")
RSS_PORT = env.str("RSS_PORT")
RSS_DRIVER = env.str("RSS_DRIVER")
RSS_TDS_VERSION = env.str("RSS_TDS_VERSION")
RSS_INSTANCE = env.str("RSS_PR")

# connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + RSS_SERVER + ';DATABASE=' + RSS_DB + ';ENCRYPT=yes;TrustServerCertificate=Yes;UID=' + RSS_USERNAME + ';PWD=' + RSS_PASSWORD
# connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
# engine = create_engine(connection_url)


conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysql.sock', user=env.str('MSQL_USER'),
                       passwd=env.str('MSQL_PASSWORD'), db=env.str('MYSQL_DB'))
engine = conn.cursor()


