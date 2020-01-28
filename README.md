# python-template

Template project for Python projects executed by DST. The template uses a data processing pipeline logic by dividing the process in processing steps.

## Usage
When creating a new repository in the DST group, you can add files from this template. See the [dst docs for instructions](https://docs.geodan.io/dst/python_template).
The script is looping through a set of processing steps. You can add steps by adding them to the Steps dictionary in main.py. The 'command' parameter refers to functions in step_functions.py. 
Add new functions to step_functions.py to keep the main.py clean.