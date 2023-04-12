import sqlalchemy as db
import pandas as pd
from datetime import datetime


username = ''
password = ''
database = ''
port = '1433'
TDS_Version = '8.0'
server = ''
driver = 'FreeTDS'

engine = db.create_engine("mysql+mysqlconnector://rck:frdrck1@localhost:3306/ram")

myQuery = "SELECT * FROM frd"
df = pd.read_sql_query(myQuery, engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

print(df)
