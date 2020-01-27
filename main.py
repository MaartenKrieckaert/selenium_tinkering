# Title:        main.py
# Description:  Template for a script running a data update

import logging
from helper_functions.logger import create_logger
from helper_functions.config_parser import import_config
from helper_functions.step_functions import execute_step_query, example_step
from os import makedirs, path
from datetime import timedelta
from time import time
from typing import List
from dstlib import connect_databases

SCRIPT_START = time()

# import parameters
params = import_config()

# database parameters
process = params['process']

# directories
work_dir = f"{params['work_dir']}{params['version']}"
log_dir = f'{work_dir}/log/'
data_dir = f'{work_dir}/data/'
sql_dir = f'{path.join(path.dirname(__file__))}/sql/'


# define steps here
steps: List[dict] = [
    {
        'command': execute_step_query,
        'args': [sql_dir, 'create_schema.sql', params['version'], params['schema'], process['user'], params['db_user']],
        'description': 'Creating the schema for further data processing',
        'returned_result': None
    },
    {
        'command': example_step,
        'args': [],
        'description': 'Dummy for a step executing "something"',
        'returned_result': None
    }
]


def main() -> None:
    # Creating necessary directories
    for directory in [log_dir, work_dir, data_dir]:
        makedirs(directory, exist_ok=True)

    # create logger
    create_logger(f"{log_dir}/overall_log_{params['version']}.log")

    logging.info(f'Starting conversion')

    # create database connection
    logging.info('Creating database connection')
    connection = connect_databases(process)

    # run steps
    for step in steps:
        logging.info(f"running step {step['command'].__name__} ({step['description']})")

        # In case the connection is needed
        if step['command'].__name__ == 'execute_step_query':
            step['command'](connection, *step['args'])

        # any other processing step
        else:
            step['command'](*step['args'])

        logging.info(f"Finished running step {step['command'].__name__}")

    # closing the connection
    connection.close()


if __name__ == '__main__':
    main()
    runtime = time() - SCRIPT_START
    logging.info(f'Script finished in {(timedelta(seconds=runtime))} seconds')
