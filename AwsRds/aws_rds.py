import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

class AwsSQL:
    def __init__(self, job, loc):

        load_dotenv("../.env")

        DATABASE_TYPE = os.environ["DATABASE_TYPE"]
        DBAPI = os.environ["DBAPI"]
        ENDPOINT = os.environ["ENDPOINT"]
        USER = os.environ["USER"]
        PASSWORD = os.environ["PASSWORD"]
        PORT = os.environ["PORT"]
        DATABASE = os.environ["DATABASE"]

        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
        self.job = job.replace(' ', '').capitalize()
        self.loc = loc.replace(' ', '').capitalize()

    def save_dataset(self, df):
        df.to_sql(f"{self.job}{self.loc}_skills", self.engine, if_exists='replace')

    def read_table(self, tbl):
        self.engine.execute(f'''SELECT * FROM {tbl}
            LIMIT 20''').fetchall()


if __name__ == '__main__':
    db = AwsSQL('test', 'testloc')
    db.engine.connect()