
from json import load
from math import e
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd


# this libraieis for data transformaton for model pickle file
import pickle
import numpy as np


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





# function create for saving the object as pickle file
# this function is used for data transormation and model file

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)


        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)


