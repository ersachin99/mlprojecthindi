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
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)



    
    except Exception as e:
        logging.info('custome exception has been raised')
        raise CustomException(e, sys)
    


