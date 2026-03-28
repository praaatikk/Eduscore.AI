import logging
import os
from datetime import datetime
import pytz

# Indian Standard Time
ist = pytz.timezone('Asia/Kolkata')

# Log file name with IST time
LOG_FILE = f"{datetime.now(ist).strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Custom time converter for logging (forces IST in logs)
class ISTFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, ist)
        if datefmt:
            return dt.strftime(datefmt)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

formatter = ISTFormatter(
    "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)