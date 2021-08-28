from sqlalchemy import create_engine
import pandas as pd

class AwsSQL:
    def __init__(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = 'career-skills.c6a6xhdjmptr.ap-northeast-1.rds.amazonaws.com'
        USER = 'postgres'
        PASSWORD = 'c8ydw9Ar8opmK8IRh78C'
        PORT = 5432
        DATABASE = 'postgres'

        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

    def save_dataset(self, df):
        df.to_sql(f'{self.job}{self.loc}_skills', self.engine, if_exists='replace')

    def read_table(self, tbl):
        self.engine.execute(f'''SELECT * FROM {tbl}
            LIMIT 20''').fetchall()