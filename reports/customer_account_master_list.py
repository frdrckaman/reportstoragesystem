import pandas as pd
from datetime import datetime

from schedules import settings as settings
import stg.customer_account_master_list_stg as stg


def main():
    df = pd.read_sql_query(stg.myQuery, settings.engine)
    df['job_date'] = datetime.today().strftime('%Y-%m-%d')
    df['job_timestamp'] = datetime.now()

    # df.to_sql(stg.table, settings.engine, schema=stg.schema,
    #           if_exists='append', index=False)


if __name__ == '__main__':
    main()