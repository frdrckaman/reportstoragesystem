import pandas as pd
from datetime import datetime
import schedules.settings as settings
import stg.customer_list_stg as stg


def main():
    df1 = pd.read_sql_query(stg.myQuery, settings.engine)
    df2 = pd.read_sql_query(stg.myQuery1, settings.engine)

    df1['JOB_DATE'] = datetime.today().strftime('%Y-%m-%d')
    df1['JOB_TIMESTAMP'] = datetime.now()
    df2['CUSTOMER_NUMBER'] = df2['CUSTOMER_ID']

    df3 = pd.merge(df1, df2, how='left', on='CUSTOMER_NUMBER')

    df = df3[['CUSTOMER_NUMBER', 'CUSTOMER_NAME', 'CUST_DOB', 'SALES_CODE', 'PORTIFOLIO_CODE',
               'SEGMENT_DESCRIPTION', 'BUSINESS_UNIT', 'EXTRACT_DATE', 'BRANCH_NAME', 'CUST_STATUS',
               'CIF_CREATION', 'PRMRY', 'PREFERREDPHONE', 'PREFERREDEMAIL', 'EMPLOYER_NAME', 'JOB_DATE',
               'JOB_TIMESTAMP']]

    # df.to_sql(stg.table, settings.engine, schema=stg.schema,
    #           if_exists='append', index=False)


if __name__ == '__main__':
    main()