import logging
import sys
from typing import Any


def setup_logging():
    """
    Configures the standard Python logging system for the application.
    It will output to the terminal (stdout).
    """

    # 1. Define the format for our logs
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # 2. Configure the root logger
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)  # Output to terminal
        ],
    )

    # 3. Create a specific logger for our app
    logger = logging.getLogger("fast_api_tutorial")
    logger.info("Logging system initialized! 🪵")

    return logger
