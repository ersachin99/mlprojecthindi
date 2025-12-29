# we use for custom exception handling

from os import error
import sys
from src.mlproject.logger import logging


# this custome message geting from documentation

def error_message_details(error, error_details:sys):
    _,_,exc_tb= error_details.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message= f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message



# createing a class for handing exception

class CustomException(Exception):
    def __init__(self,error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message= error_message_details(error_message, error_details)
    
    

    def __str__(self):
        return self.error_message