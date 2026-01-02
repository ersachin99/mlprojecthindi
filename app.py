from pyexpat import model
from src.mlproject.logger import logging
# both logging and exception module are imported here and run

from src.mlproject.exception import CustomException
import sys

# data ingestion is reading
from src.mlproject.components.data_ingestion  import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig


# for data transformation and model training we will import later
from src.mlproject.components.data_transformation import DataTransformationconfig
from src.mlproject.components.data_transformation import DataTransformation


# for model training and model transer we will import later
from src.mlproject.components.data_transformation import DataTransformationconfig
from src.mlproject.components.model_transer import ModelTrainer, ModelTransferConfig
from src.mlproject.components.model_transer import ModelTrainer




if __name__ == "__main__":
    logging.info('the execution started')

    try:
        # data ingestion start here for only testing
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # for data transformation testing

        # data_transformation_config=DataTransformationconfig()
        # above code is commedte becuase under data transformation class we have already data)_transformation_config object

        data_transformation = DataTransformation()
        train_arr,test_arr,_ =data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        # for model trainer code here 

        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    
    except Exception as e:
        logging.info('custome exception has been raised')
        raise CustomException(e, sys)
    


