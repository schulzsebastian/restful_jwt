# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/api/status.py

from . import api, token_required
from flask import jsonify

@api.route('/status')
def status():
    return jsonify({'message': 'ok'})

@api.route('/status_auth')
@token_required
def status_auth():
    return jsonify({'message': 'auth'})