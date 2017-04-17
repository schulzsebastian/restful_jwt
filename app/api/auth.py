# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/api/auth.py

from . import auth
from ..db import User
from flask import current_app, jsonify, request
from datetime import datetime, timedelta
from functools import wraps
import jwt

@auth.route('/get_token', methods=['POST'])
def get_token():
    payload = request.get_json(force=True)
    if payload['username']:
        payload['username'] = payload['username'].replace(' ', '')
        if payload['password']:
            logged = User.check_password(payload)
            if logged:
                print(logged.id)
                token = create_token()
                return jsonify({'token': token})
            return jsonify({'message': 'invalid credentials'}), 403
        return jsonify({'message': 'password required'}), 400
    return jsonify({'message': 'username required'}), 400


@auth.route('/register', methods=['POST'])
def register():
    payload = request.get_json(force=True)
    if payload['username']:
        payload['username'] = payload['username'].replace(' ', '')
        if payload['username'] not in User.users_list():
            if payload['password']:
                User.add_user(payload)
                return jsonify({'message': 'user {} registerd'.format(payload['username'])})
            return jsonify({'message': 'password required'}), 400
        return jsonify({'message': 'user exists'}), 400
    return jsonify({'message': 'username required'}), 400

def create_token(seconds=60):
    payload = {
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