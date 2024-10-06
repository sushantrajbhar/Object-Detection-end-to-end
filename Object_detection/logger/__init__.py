import logging
import os
from datetime import datetime
from from_root import from_root

# Set a static log file name
LOG_FILE = 'application.log'  # Fixed log file name

# Create log path
log_path = os.path.join(from_root(), 'log')
os.makedirs(log_path, exist_ok=True)

# Full path to log file
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging to append to the log file
logging.basicConfig(
    filename=lOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode='a'  # Append mode
)

# Example logging messages
logging.info('Logging started.')
