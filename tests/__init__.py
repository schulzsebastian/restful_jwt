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
from app.api import create_token, decode_token

class BaseTest(TestCase):
    
    def create_app(self):
        app = create_app('testing')
        return app

    def create_token(self, data, seconds=60):
        return create_token(data, seconds)

    def decode_token(self, token):
        return decode_token(token)