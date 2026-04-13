import logging
import os
from datetime import datetime

# Create logs directory path
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full path for log file
logs_path = os.path.join(os.getcwd(), log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger("cnnClassifierLogger")