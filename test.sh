#!/usr/bin/env bash
set -ex

# Run unit tests on all testable python scripts
python -m unittest discover .

# If there is a mypy ini file: run mypy type checking on all python files
if [ -f mypy.ini ]
then
  find . -name '*.py' -print0 | xargs -0 mypy #
fi
