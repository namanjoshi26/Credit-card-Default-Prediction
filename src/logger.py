import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# logs_path = "cwd/../../logsLOG_FILE" This is how it will be created
os.makedirs(logs_path,exist_ok=True)
# exist_ok (even thought there is a file/folder keep on apppending inside taht folder)

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format ="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__=="__main__":  #testing logging
#     logging.info("Logging has started")