# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/test_tokens.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

import unittest
from tests import BaseTest
from datetime import datetime, timedelta
from time import time

class TestTokens(BaseTest):

    def test_tokens(self):
        #Create token for one minute
        request_time = int(time())
        expire_time = request_time + timedelta(seconds=60).total_seconds()
        user = self.add_user('test', 'test')
        token_encoded = self.create_token(user)
        self.assertEqual(type(token_encoded), str)
        token_decoded = self.decode_token(token_encoded)
        self.assertIn('iat', token_decoded)
        self.assertIn('exp', token_decoded)
        #TODO: to_calendar
        #self.assertEqual(request_time, token_decoded['iat'])
        #self.assertEqual(expire_time, token_decoded['exp'])
        #Create token for one hour
        request_time = int(time())
        expire_time = request_time + timedelta(hours=1).total_seconds()
        token_encoded = self.create_token(user, timedelta(hours=1).total_seconds())
        self.assertEqual(type(token_encoded), str)
        token_decoded = self.decode_token(token_encoded)
        self.assertIn('iat', token_decoded)
        self.assertIn('exp', token_decoded)
        self.assertEqual(request_time, token_decoded['iat'])
        self.assertEqual(expire_time, token_decoded['exp'])