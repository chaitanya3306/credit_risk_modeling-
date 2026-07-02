import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Generate timestamped log file
LOG_FILE = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler()  # also prints logs to console
    ]
)

logger = logging.getLogger(__name__)
