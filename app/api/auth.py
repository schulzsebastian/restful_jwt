# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/api/auth.py

from . import auth
from flask import current_app, jsonify, request
from datetime import datetime, timedelta
from functools import wraps
import jwt

@auth.route('/get_token')
def get_token():
    token = create_token('test')
    return jsonify({'token': token})

def create_token(data, seconds=60):
    payload = {
        'data': data,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(seconds=seconds)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token.decode('unicode_escape')
 
def decode_token(token):
    return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify(message='Token is required'), 403
        try:
            decode_token(token)
        except jwt.DecodeError:
            return jsonify(message='Token is invalid'), 401
        except jwt.ExpiredSignature:
            return jsonify(message='Token has expired'), 401
        return f(*args, **kwargs)
    return decorated_function