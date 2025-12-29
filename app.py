from src.mlproject.logger import logging
# both logging and exception module are imported here and run

from src.mlproject.exception import CustomException
import sys



if __name__ == "__main__":
    logging.info('the execution started')

    try:
        a=1/0
    
    except Exception as e:
        logging.info('custome exception has been raised')
        raise CustomException(e, sys)
    


