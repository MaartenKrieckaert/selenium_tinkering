# Title:        main.py
# Description:  Template for a script running a data update

import logging
from os import path, makedirs, sep
from datetime import timedelta
from time import time
from pathlib import Path
from collections import OrderedDict
import dstlib.dstlib



SCRIPT_START = time()

# define steps here
steps = OrderedDict([("1", "step1.sql"),
                     ("2", "something else")])


# parameters dummy
# I want the log to be one level up. Keeps the git folder tidy (we need to discuss this)
log_dir = Path(path.abspath(path.join(path.dirname(__file__), '..', 'log')).replace(sep, '/'))
version = 199001
prep_steps = True
schema = 'template'
process = {"host": "etl-server03", "dbname": "process", "user": "geodbadmin", "password": "", "port": 5432}


def make_dir(directory: str) -> None:
    """
    Simple function for creating directories (and check if they exist)
    Directories: list of strings of the paths to be created as directories
    """
    if not path.exists(directory):
       #logging.info(f'Creating folder {directory}')
       makedirs(directory)


def main() -> None:
    # Creating necessary directories
    for directory in [log_dir]:
        make_dir(directory)

    # Creating log file and -stream
    logging.getLogger()
    logging.basicConfig(
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        handlers=[
                            logging.FileHandler(f'{log_dir}/overall_log_{version}.log'),
                            logging.StreamHandler()
                        ])
    logging.info(f'Starting conversion')


    # create database connection
    logging.info('Creating database connection')
    connection = dstlib.dstlib.connect_databases(process)

    # defining queries
    create_schema_query = f'''
        DROP SCHEMA IF EXISTS {schema}_{version} CASCADE;
        CREATE SCHEMA {schema}_{version} AUTHORIZATION {process['user']};
        GRANT USAGE ON SCHEMA {schema}_{version} TO geodb;
        '''

    # running preparation steps
    if prep_steps:
        logging.info("Running preparation queries")
        # executing queries
        for query in [create_schema_query]:
            dstlib.dstlib.execute_query(connection, query)

    # run steps
    for step in steps:
        logging.info(f"running step {step}")

        logging.info(f'Do something here')


if __name__ == '__main__':
    main()
    runtime = time() - SCRIPT_START
    logging.info(f'Script finished in {(timedelta(seconds=runtime))} seconds')

