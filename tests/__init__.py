# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/__init__.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

from flask_testing import TestCase
from app import create_app, TestingConfig
from app.api import create_token, decode_token
from app.db import db, User
import json

class BaseTest(TestCase):

    def setUp(self):
        db.init(TestingConfig.DB_NAME,
            host=TestingConfig.DB_HOST,
            user=TestingConfig.DB_USER,
            password=TestingConfig.DB_PASS,
            port=TestingConfig.DB_PORT)
        db.create_tables([User], safe=True)

    def tearDown(self):
        db.drop_tables([User], safe=True)
    
    def create_app(self):
        app = create_app('testing')
        return app

    def create_token(self, user, seconds=60):
        return create_token(user, seconds)

    def decode_token(self, token):
        return decode_token(token)
    
    def add_user(self, username, password):
        return User.add_user({'username': username, 'password': password})

    def post_json(self, url, payload):
        payload = json.dumps(payload)
        return self.client.post('/get_token', data=payload, content_type='application/json')

    def token_is_valid(self, token):
        try:
            decode_token(token)
            return True
        except:
            return False