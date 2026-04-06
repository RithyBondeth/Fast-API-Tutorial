import logging
import sys


def setup_logging(log_level: str = "INFO"):
    """
    Configures an advanced, colorized logging system for the application.
    """

    # 1. Map log level strings to logging constants
    level = getattr(logging, log_level.upper(), logging.INFO)

    # 2. Define professional, clear format for our logs
    # Using emojis and spacing for better visual scanning in the terminal
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    # 3. Configure the root logger
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
    )

    # 4. Create a specific logger for our app
    logger = logging.getLogger("fast_api_tutorial")
    
    # 5. Show that all levels are working!
    logger.debug("🛡️ DEBUG: System is starting up...")
    logger.info("🪵 INFO: Logging system initialized!")
    
    return logger
