# Title:        main.py
# Description:  Template for a script running a data update

import logging
from python.logger import create_logger
from os import makedirs, path
from datetime import timedelta
from time import time
from collections import OrderedDict
import dstlib
import yaml


SCRIPT_START = time()

# define steps here
steps = OrderedDict([("1", "create_schema.sql"),
                     ("2", "something_else")])


# Parameters
with open('config/config.yml') as f:
    params = yaml.safe_load(f)

version = params['version']
schema = params['schema']
process = params['process']
db_user = params['db_user']

work_dir = f"{params['work_dir']}{version}"
log_dir = f'{work_dir}\\log\\'
data_dir = f'{work_dir}\\data\\'

sql_dir = f'{path.join(path.dirname(__file__))}\\sql\\'


def main() -> None:
    # Creating necessary directories
    for directory in [log_dir, work_dir, data_dir]:
        makedirs(directory, exist_ok=True)

    # create logger
    create_logger(f'{log_dir}/overall_log_{version}.log')

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
                step_query = f.read().format(version=version, schema=schema, dbadmin=process['user'], dbuser=db_user)
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

