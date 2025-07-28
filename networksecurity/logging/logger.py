import os
import logging
from datetime import datetime

# Generate log filename
LOG_FILE = f'{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log'

# Construct directory and full path
logs_dir = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s',
    level=logging.INFO,
)
