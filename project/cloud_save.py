from sqlalchemy import create_engine 
def save_dataset(self, ls):
    DATABASE_TYPE = 'postgresql'
    DBAPI = 'psycopg2'
    ENDPOINT = 'career-skills.c6a6xhdjmptr.ap-northeast-1.rds.amazonaws.com'
    USER = 'postgres'
    PASSWORD = ''
    PORT = 5432
    DATABASE = 'postgres'
    engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

    ls.to_sql(f'{self.job}{self.loc}_skills', engine, if_exists='replace')