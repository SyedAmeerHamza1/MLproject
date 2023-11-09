import sys
from src.logger import logging

def error_msg_details(error, error_details:sys):
    _,_,exc_tb= error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno

    error_msg="Error occured in python scrit file name [{0}], line number [{1}], error message [{2}]". format(file_name, line_no, str(error))

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_details:sys):
        super().__init__(error_msg)
        self.error_msg= error_msg_details(error_msg, error_details=error_details)

    def __str__(self):
        return self.error_msg
    

        
