# Title:        logger.py
# Description:  Contains a function for creating a basic config for a logger

# import stuff
import logging


def create_logger(log_file: str) -> None:
    # Creating log file and -stream
    logging.getLogger()
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ])