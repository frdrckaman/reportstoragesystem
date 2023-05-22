from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import os
from pathlib import Path
import environ
import pandas as pd
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    RSS_PR=(bool, False),
    RSS_DR=(bool, False),
    RSS_UAT=(bool, False),
)

environ.Env.read_env(ENV_DIR)

RSVR_CLUSTER = env.str("RSVR_CLUSTER")
RSS_SERVER = env.str("RSS_SERVER_PR01")
RSS_USERNAME = env.str("RSS_USERNAME")
RSS_PASSWORD = env.str("RSS_PASSWORD")
RSS_DB = env.str("RSS_DB")
RSS_PORT = env.str("RSS_PORT")
RSS_DRIVER = env.str("RSS_DRIVER")
RSS_TDS_VERSION = env.str("RSS_TDS_VERSION")
RSS_INSTANCE = env.str("RSS_PR")
RTISS_SCHEMA = env.str("RTISS_SCHEMA")
EXCHANGE_RATES = env.str("EXCHANGE_RATES")

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + RSVR_CLUSTER + ';DATABASE=' + RSS_DB + ';ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID=' + RSS_USERNAME + ';PWD=' + RSS_PASSWORD
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

myQuery = EXCHANGE_RATES
df = pd.read_sql_query(myQuery, engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

df.to_sql('CustomerAccountMasterListReport', engine, schema=RTISS_SCHEMA, if_exists='append', index=False)