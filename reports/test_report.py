import pandas as pd
from datetime import datetime
from schedules import settings
from stg import test_report_stg

df = pd.read_sql_query(test_report_stg.myQuery, settings.engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

print(df)
