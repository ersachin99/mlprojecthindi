from src.mlproject.logger import logging
# both logging and exception module are imported here and run

from src.mlproject.exception import CustomException
import sys

# data ingestion is reading
from src.mlproject.components.data_ingestion  import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig




if __name__ == "__main__":
    logging.info('the execution started')

    try:
        # data ingestion start here for only testing
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    
    except Exception as e:
        logging.info('custome exception has been raised')
        raise CustomException(e, sys)
    


