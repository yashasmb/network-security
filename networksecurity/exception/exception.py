import sys
from networksecurity.logging import logger

class NetworksecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_number}]. Error message: [{self.error_message}]"


if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log message.")
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise NetworksecurityException(e, sys) from e