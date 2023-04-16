import sqlalchemy as db
import pandas as pd
from datetime import datetime
from schedules import settings
from stg import test_report_stg

# engine = db.create_engine("mysql+mysqlconnector://rck:frdrck1@localhost:3306/ram")

# myQuery = "SELECT * FROM frd"
df = pd.read_sql_query(test_report_stg.myQuery, settings.engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

print(df)
