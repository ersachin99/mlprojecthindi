# data injection phase 
# how to read the data from source
# how to store the data
### mysql -> 

import os
import sys

import test

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd

# importng some libraries for mysql
from src.mlproject.utils import read_sql_data

# import sklenarn for train test split
from sklearn.model_selection import train_test_split


# importing some dataclasses 
from dataclasses import dataclass

# dataclass 
@dataclass
class DataIngestionConfig:
    train_data_path: str =os. path.join('artifacts','train.csv')
    test_data_path: str =os. path.join('artifacts','test.csv')
    raw_data_path: str =os. path.join('artifacts','data.csv')  ## row getting all the data



# creating class for data ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # reading code here

            df=read_sql_data()

            logging.info('Reading completed from mysql database')
            # after saving the data in dataframe we have to save it in artifacts folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # after reading the data converted into cvs files
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # after importing libraties split the data using trai test spit
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)


            # same as above saving the train and test data as per csv file/same path as per above train,test path
            # for train data path
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            # for test data path 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            #create some logging info
            logging.info('Data Ingestion is Completed')

            # and return the train and test data path

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        





# for reading from mysql databse we need enviroment varibales
# creating a env file 
# reading file will be done in utils files 
# after done aal the go to app.py and call teh data ingestion file 