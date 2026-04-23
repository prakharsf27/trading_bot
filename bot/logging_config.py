import logging
import os

def setup_logging(log_file="bot.log"):
    """Sets up logging to both console and a file."""
    # Ensure the directory for logs exists if needed
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("TradingBot")
    return logger
