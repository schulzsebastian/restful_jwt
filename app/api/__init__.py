# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/api/__init__.py

from flask import Blueprint

api = Blueprint('api', __name__)
auth = Blueprint('auth', __name__)

from .auth import *
from .routings import *
