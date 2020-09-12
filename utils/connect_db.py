import psycopg2
import mysql.connector
from psycopg2 import Error
from mysql.connector import Error
from sqlalchemy import create_engine


#function to connect to postgres
def get_pgsql_conn(db):
    try:
        conn = psycopg2.connect(
            database=db['NAME'],
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            port=db['PORT']
        )
        print("PgSQL Database Connected....")
        return conn
    except (Exception, psycopg2.Error) as error:
        print(
            "Error while connecting to PostgreSQL", error
        )


#function to connect to mysql
def get_mysql_conn(db):
    try:
        conn = mysql.connector.connect(
            database=db['NAME'],
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            port=db['PORT']
        )
        print("MySQL Database Connected....")
        return conn
    except (Exception, mysql.connector.Error) as error:
        print(
            "Error while connecting to MySQL", error
        )


#function to get postgres engine
def get_pgsql_engine(db):
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{db['USER']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['NAME']}"
        )
        print("PostgreSQL Database Connected...")
        return engine
    except(Exception) as error:
        print(
            'Error while connecting to PostgreSQL...', error
        )


#function to get mysql engine
def get_mysql_engine(db):
    try:
        engine = create_engine(
            f"mysql+mysqlconnector://{db['USER']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['NAME']}"
        )
        print("MySQL Database Connected...")
        return engine
    except(Exception) as error:
        print(
            'Error while connecting to MySQL...', error
        )