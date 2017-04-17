# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/__init__.py

from flask import Flask
from .config import *
from .db import db, User
from .api import api, auth

def create_app(config='development'):
    app = Flask(__name__)
    #Config
    if config == 'production':
        app.config.from_object(Config)
    elif config == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    #Database
    if config != 'testing':
        db.init(app.config["DB_NAME"],
            host=app.config["DB_HOST"],
            user=app.config["DB_USER"],
            password=app.config["DB_PASS"],
            port=app.config["DB_PORT"])
        db.create_tables([User], safe=True)
    #Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(api)
    return app