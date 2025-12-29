
from json import load
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd



import pymysql

from dotenv import load_dotenv

# loading the enviroment variables
# 
load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')



# reading the data from mysql database
def read_sql_data():
    logging.info('Readding sql database has started')
    try:
        # connecting to mysql database here
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        logging.info('connection establised',mydb)

        # creating a dataframe after reading the data

        df=pd.read_sql('select * from students', mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)






