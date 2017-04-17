# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/test_auth.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

import unittest
from tests import BaseTest

class TestRoutings(BaseTest):

    def test_get_token(self):
        #Without username
        payload = {}
        response = self.post_json('/get_token', payload)
        self.assertEqual(response.status_code, 400)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'username required')
        #Without password
        payload['username'] = 'test'
        response = self.post_json('/get_token', payload)
        self.assertEqual(response.status_code, 400)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'password required')
        #Invalid credentials
        payload['password'] = 'test'
        response = self.post_json('/get_token', payload)
        self.assertEqual(response.status_code, 403)        
        data = response.json
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'invalid credentials')
        #Success
        user = self.add_user('test', 'test')
        response = self.post_json('/get_token', payload)
        self.assertEqual(response.status_code, 200)        
        data = response.json
        self.assertIn('token', data)
        self.assertTrue(self.token_is_valid(data['token']))
        token = self.decode_token(data['token'])
        self.assertEqual(token['uid'], user.hashed_id)
        #TODO: register