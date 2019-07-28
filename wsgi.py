#!/usr/bin/env python3

import logging
import sys
import os

curdir = os.path.split(__file__)[0]

activate_this = os.path.join(curdir, '.venv', 'bin', 'activate_this.py')

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, curdir)
from app import app as application