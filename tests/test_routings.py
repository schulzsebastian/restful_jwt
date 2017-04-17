# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/test_routings.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

import unittest
from tests import BaseTest

class TestRoutings(BaseTest):

    def test_status(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'ok')

    def test_status_auth(self):
        #Without token
        response = self.client.get('/status_auth')
        self.assertEqual(response.status_code, 403)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Token is required')
        #Invalid token
        response = self.client.get('/status_auth?token=test')
        self.assertEqual(response.status_code, 401)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Token is invalid')
        #Expired token
        user = self.add_user('test', 'test')
        token = self.create_token(user, -1)
        response = self.client.get('/status_auth?token={}'.format(token))
        self.assertEqual(response.status_code, 401)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Token has expired')
        #Request with token
        token = self.create_token(user)
        response = self.client.get('/status_auth?token={}'.format(token))
        self.assertEqual(response.status_code, 200)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'auth')
