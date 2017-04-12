# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/__init__.py

from flask import Flask
from .config import *
#Blueprints
from .api import api

def create_app(config='development'):
    app = Flask(__name__)
    if config == 'production':
        app.config.from_object(Config)
    elif config == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    app.register_blueprint(api)
    return app