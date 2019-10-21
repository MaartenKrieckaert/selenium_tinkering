# Title:        config_parser.py
# Description:  Contains a function for loading a yaml configuration file
from typing import Dict, Union

import yaml


def import_config(config: str = 'config.yml') -> Dict[str, Union[str, Dict[str, str]]]:
    """
    Function for importing the parameter file
    :param config: normally you shouldn't have to change this value.
        Rename the config file from config_template.yml to config.yml instead
    :return: your parameters
    """

    if config.endswith('config_template.yml'):
        raise ValueError('Don\'t use the template config directly to load the configuration, '
                         'create a copy of the template to config.yml instead.')

    try:
        # read config file
        with open(config) as f:
            params = dict(yaml.safe_load(f))

        return params

    except FileNotFoundError:
        print(f'{config} cannot be found, have you renamed the config_template.yml to config.yml?')
        raise




