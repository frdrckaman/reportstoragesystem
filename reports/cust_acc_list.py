import sqlalchemy as db
import pandas as pd
from datetime import datetime
from schedules import settings

engine = db.create_engine(settings.MYSQL_CONN)

myQuery = "SELECT * FROM frd"
df = pd.read_sql_query(myQuery, engine)
df['job_date'] = datetime.today().strftime('%Y-%m-%d')
df['job_timestamp'] = datetime.now()

print(df)
