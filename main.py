# Title:        main.py
# Description:  Template for a script running a data update

import logging
from logger import create_logger
from os import path, makedirs, sep
from datetime import timedelta
from time import time
from pathlib import Path
from collections import OrderedDict
import dstlib


SCRIPT_START = time()

# define steps here
steps = OrderedDict([("1", "create_schema.sql"),
                     ("2", "something_else")])


# parameters dummy
# I want the log to be one level up. Keeps the git folder tidy (we need to discuss this)
log_dir = Path(path.abspath(path.join(path.dirname(__file__), '..', 'log')).replace(sep, '/'))
work_dir = Path(path.abspath(path.dirname(__file__)).replace(sep, '/'))
version = 199001
prep_steps = True
schema = 'template'
process = {"host": "etl-server03", "dbname": "process", "user": "geodbadmin", "password": "", "port": 5432}
dbuser = 'geodb'


def main() -> None:
    # Creating necessary directories
    for directory in [log_dir]:
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
            with open(f"{work_dir}\\sql\\{steps[step]}", encoding='utf-8-sig') as f:
                step_query = f.read().format(version=version, schema=schema, dbadmin=process['user'], dbuser=dbuser)
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

