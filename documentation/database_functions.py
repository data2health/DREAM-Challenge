import pandas as pd
import json
import pyodbc
import os.path


def database_connection():

    creds = json.load(open('sql_credentials.json')) #/data/common/data/credentials/
    database = creds['database']
    username = creds['username']
    password = creds['password']
    server = creds['server']
    
    driver = '{ODBC Driver 13 for SQL Server}'

    if database:
        cnxn = pyodbc.connect('DRIVER='+ driver +';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    else:
        cnxn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;UID=' + username + ';PWD=' + password)
    return cnxn

def get_tables():

    query = "SELECT * FROM information_schema.TABLES"
    df = pd.read_sql(query, con=database_connection())
    return df


def query(sql_string):
    df = pd.read_sql(sql_string, con=database_connection())
    return df


def chunked_query(sql_string, num):
    df = pd.read_sql(sql_string, con=database_connection(), chunksize=num)
    return df