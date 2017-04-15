# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/config.py

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'test'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True