# Title:        step_functions.py
# Description:  Template for a script running a data update. It contains functions for the processing steps

from dstlib import execute_query
import logging

# Executing the sql steps
def execute_step_query(connection, sql_dir, query, version, schema, dbadmin, dbuser) -> None:
    logging.info(f"Executing query {query}")
    with open(f"{sql_dir}{query}", encoding='utf-8-sig') as f:
        step_query = f.read().format(version=version,
                                     schema=schema,
                                     dbadmin=dbadmin,
                                     dbuser=dbuser)
    execute_query(connection, step_query)

def example_step() -> None:
    # do something here
    pass

