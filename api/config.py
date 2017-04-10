# !usr/bin/python
# -*- coding: utf-8 -*-
# /api/config.py

class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True