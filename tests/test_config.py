# !usr/bin/python
# -*- coding: utf-8 -*-
# /tests/test_config.py

import sys, os.path
sys.path.append(os.path.abspath('../'))

import unittest
from flask_testing import TestCase
from api import create_app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        return create_app('development')

    def test_variables(self):
        self.assertTrue(self.app.config['DEBUG'])
        self.assertFalse(self.app.config['TESTING'])


class TestTestingConfig(TestCase):
    def create_app(self):
        return create_app('testing')

    def test_variables(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['DEBUG'])


class TestProductionConfig(TestCase):
    def create_app(self):
        return create_app('production')

    def test_variables(self):
        self.assertFalse(self.app.config['DEBUG'])
        self.assertFalse(self.app.config['TESTING'])