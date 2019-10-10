# Title:        config_parser.py
# Description:  Contains a function for loading a yaml configuration file

# import stuff
import yaml
import sys


# function for importing the parameter file
def import_config(config: str = 'config/config.yml') -> dict:
    """
    :param config: normaly you shouldn't change this value. Rename the config file instead
    :return: your parameters
    """

    try:
        # read config file
        with open(config) as f:
            params = yaml.safe_load(f)

        return params

    except FileNotFoundError:
        print(f'{config} cannot be found, have you renamed the config_template.yml to config.yml?')
        sys.exit(1)




