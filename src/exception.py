# https://docs.python.org/3/tutorial/errors.html

import logging
import sys
import traceback

# Ensure that logging configurations are loaded
from logger import LOG_FILE_PATH 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

# Custom Exception Class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

def log_exception(exc_type, exc_value, exc_traceback):
    logging.error("Exception occurred", exc_info=(exc_type, exc_value, exc_traceback))
    raise CustomError(f"{exc_type.__name__}: {exc_value}")

# Set the custom exception handler
sys.excepthook = log_exception

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Handling an exception")
        raise