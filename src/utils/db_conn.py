import os
from dotenv import load_dotenv
import pg8000
from pg8000.native import Connection

load_dotenv()

def db_conn(db='SOURCE'):
    '''
    parameters:
    
        db (str): 'SOURCE' or 'TARGET' - default is 'SOURCE'
    
    returns:
    
        database connection object
    
    '''
    conn = Connection(
        database=os.getenv(f'{db}_DB_NAME'),
        user=os.getenv(f'{db}_DB_USER'),
        password=os.getenv(f'{db}_DB_PASSWORD'),
        host=os.getenv(f'{db}_DB_HOST'),
        port=os.getenv(f'{db}_DB_PORT')
    )
    
    # GET ENV VARS FROM load_db_config (throwing an error)
    
    # db_credentials = load_db_config()[db]
    # conn = Connection(
    #     db_credentials['user'],
    #     database=db_credentials['dbname'],
    #     password=db_credentials['password'],
    #     host=db_credentials['host'],
    #     port=db_credentials['port']
    # )
    
    return conn