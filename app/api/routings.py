# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/api/status.py

from . import api
from flask import jsonify

@api.route('/status')
def status():
    return jsonify({'status': 'ok'})
