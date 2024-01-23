# https://docs.python.org/3/tutorial/errors.html

import sys

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # Get the exception traceback (file and line number)
    error_message="Error: " + str(error) + " in " + str(exc_tb.tb_frame.f_code.co_filename) + " at line " + str(exc_tb.tb_lineno)
    return error_message

class CustomError(Exception):
    def __init__(self, error, error_detail:sys):
        self.error_message = error_message_details(error, error_detail)
        super().__init__(self.error_message)


    def __str__(self):
        return self.error_message