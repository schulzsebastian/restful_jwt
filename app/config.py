# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/config.py

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'test'
    DB_NAME = 'api'
    DB_HOST = 'localhost'
    DB_USER ='ss'
    DB_PASS = 'zaq12wsx'
    DB_PORT = 5432

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DB_NAME = 'api_test'