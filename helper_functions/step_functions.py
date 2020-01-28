# Title:        step_functions.py
# Description:  Template for a script running a data update. It contains functions for the processing steps

from dstlib import execute_query
from psycopg2 import extensions
import logging


# Executing the sql steps
def execute_step_query(connection: extensions.connection, query_file: str, version: str, schema: str, dbadmin: str,
                       dbuser: str) -> None:
    """
    :param connection: psycopg2 connection to the database (use the dstlib.connect_databases function to create it)
    :param query_file: query file to be executed
    :param version: data update version
    :param schema: Schema name (without version)
    :param dbadmin: Database admin user
    :param dbuser: Database reader user
    :return: None
    """

    logging.info(f"Executing query {query_file}")
    with open(f"{query_file}", encoding='utf-8-sig') as f:
        step_query = f.read().format(version=version,
                                     schema=schema,
                                     dbadmin=dbadmin,
                                     dbuser=dbuser)
    execute_query(connection, step_query)


def example_step() -> None:
    # do something here
    pass

