# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/__init__.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/__init__.py

from flask_testing import TestCase
from app import create_app

class BaseTest(TestCase):
    
    def create_app(self):
        app = create_app('testing')
        return app

from .test_config import *