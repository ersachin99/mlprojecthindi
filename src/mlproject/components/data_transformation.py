from math import log
import sys
import os
from dataclasses import dataclass

from networkx import number_attracting_components
import numpy  as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# now we import some libraies for pickle file, 
# this use for import libraie from uitils file for pickel save_object function
from src.mlproject.utils import save_object


from src.mlproject.exception import CustomException
from src.mlproject.logger import logging


# data class createdd 
@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path= os.path.join('artifacts','preprocessor.pkl')



class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation
        """

        try :
            # define the numerical and categorical columns
            # you may write same as per your eda file 
            # here we write another way to define this columns
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = ['gender',
                                   'race_ethnicity',
                                    'parental_level_of_education',
                                    'lunch',
                                    'test_preparation_course']
            
            # we create piepline for numerical columns, and categorical columns
            num_piepline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])

            # for categorical columns
            cat_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
            ])

            # now we do logging information
            logging.info(f'Categorical columns: {categorical_columns}')
            logging.info(f'Numerical columns: {numerical_columns}')

            # now we combile both pipelines
            preprocessor=ColumnTransformer([
                ('num_pipeline', num_piepline,numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns  )
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        


    def initiate_data_transformation(self, train_path, test_path):
        try:
            # reading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            # logging info
            logging.info('Reading the train and test data is completed')



            # obtaining preprocessor object

            preprocessing_obj= self.get_data_transformer_object()

            # set the target varibale  so we get here math score as output target
            target_column_name= 'math_score'
            numerical_columns=['writing_score','reading_score']

            # divide the  train dataset into independent and dependent features

            # from train data we drop some data for output feature 
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            # target feature for train df here
            target_feature_train_df=train_df[target_column_name]


            # divide the  test dataset into independent and dependent features

            # from test data we drop some data for output feature 
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            # target feature for test df here
            target_feature_test_df=test_df[target_column_name]


            # logging info
            logging.info('Applying preprocessing object on training and testing datasets.')

            # now we apply the and fit the data and output will be in arr format
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            # here apply only fit.transform on for test data
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)


            # now we combine and conerted arr  format and combine
            # for train and test data we use np.c_ to combine both input and output feature

            train_arr=np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            # logging info
            logging.info('Saved preprocessing object.')


            # create a function to save the object
            # now when you import libraeia and function from utils file 
            # save the model as pickle file
            # in this save object we pass file path and object

            save_object(
                file_path= self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            # this function go to ustils file and save the object as pickle file as dump
            # ad this file go to artifacts folder and save the preprocessor.pkl file

            # after train we return the train arr, test arr and preprocessor obj file path

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )














        except Exception as e:
            raise CustomException(e,sys)    
        

