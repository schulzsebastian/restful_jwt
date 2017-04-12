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
        data = response.json
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'ok')