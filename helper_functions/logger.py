# Title:        logger.py
# Description:  Contains a function for creating a basic config for a logger

import logging


def create_logger(log_file: str) -> None:

    # If you try to log before creating the basicconfig it will not create it.
    # Strange implementation of the logging module...
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    # Creating log file and -stream
    logging.getLogger()
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ])
