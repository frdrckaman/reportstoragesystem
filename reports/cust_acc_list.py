from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

username = 'clusterInstaller'
password = 'clusterInstaller'
database = 'RSVRCuratedInterfaceFinacleTZ'
port = '1433'
TDS_Version = '8.0'
server = '10.231.33.102'
driver = 'FreeTDS'

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;TrustServerCertificate=Yes;UID='+username+';PWD='+ password
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

myQuery = "SELECT * FROM CustomerAccountMasterList.vwCuratedTZACustomerAccountMasterListReport"
df = pd.read_sql_query(myQuery, engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

df.to_sql('CustomerAccountMasterListReport', engine, schema="CustomerAccountMasterList", if_exists='append', index=False)