# Title:        main.py
# Description:  Template for a script running a data update

import logging
from helper_functions.logger import create_logger
from helper_functions.config_parser import import_config
from os import makedirs, path
from datetime import timedelta
from time import time
from collections import OrderedDict
import dstlib


SCRIPT_START = time()

# define steps here
steps = OrderedDict([("1", "create_schema.sql"),
                     ("2", "something_else")])


# import parameters
params = import_config()

# databases
process = params['process']
products = params['products']

# directories
work_dir = f"{params['work_dir']}{params['version']}"
log_dir = f'{work_dir}\\log\\'
data_dir = f'{work_dir}\\data\\'
sql_dir = f'{path.join(path.dirname(__file__))}\\sql\\'


def main() -> None:
    # Creating necessary directories
    for directory in [log_dir, work_dir, data_dir]:
        makedirs(directory, exist_ok=True)

    # create logger
    create_logger(f"{log_dir}/overall_log_{params['version']}.log")

    logging.info(f'Starting conversion')

    # create database connection
    logging.info('Creating database connection')
    connection = dstlib.connect_databases(process)

    # run steps
    for step in steps:
        logging.info(f"running step {step}")
        # running SQL steps
        if steps[step].endswith(".sql"):
            logging.info(f'Executing query {steps[step]}')
            with open(f"{sql_dir}{steps[step]}", encoding='utf-8-sig') as f:
                step_query = f.read().format(version=params['version'],
                                             schema=params['schema'],
                                             dbadmin=process['user'],
                                             dbuser=params['db_user'])
            dstlib.execute_query(connection, step_query)

        else:
            logging.info(f'Do something here')

        logging.info(f'Finished running step {step}')

    # closing the connection
    connection.close()


if __name__ == '__main__':
    main()
    runtime = time() - SCRIPT_START
    logging.info(f'Script finished in {(timedelta(seconds=runtime))} seconds')

