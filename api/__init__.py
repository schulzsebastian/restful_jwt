# !usr/bin/python
# -*- coding: utf-8 -*-
# /api/__init__.py

from flask import Flask
from .config import *

def create_app(config='development'):
    app = Flask(__name__)
    if config == 'production':
        app.config.from_object(Config)
    elif config == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    return app