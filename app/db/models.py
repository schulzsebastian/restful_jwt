# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/db/models.py

from peewee import Model, CharField, DateTimeField
from playhouse.postgres_ext import PostgresqlExtDatabase
from flask import current_app
from datetime import datetime
from hashids import Hashids
import bcrypt

db = PostgresqlExtDatabase(None, register_hstore=False)

class BaseClass(Model):
    class Meta:
        database = db

    def hash_id(uid):
        hashid_instance = Hashids(salt=current_app.config['SECRET_KEY'])
        return hashid_instance.encode(uid)

    def unhash_id(uid):
        hashid_instance = Hashids(salt=current_app.config['SECRET_KEY'])
        return hashid_instance.decode(uid)


class User(BaseClass):
    username = CharField(unique=True)
    password = CharField()
    register_date = DateTimeField()

    def users_list():
        return [u.username for u in User.select()]

    def add_user(payload):
        payload['register_date'] = datetime.utcnow()
        payload['password'] = bcrypt.hashpw(payload['password'].encode('utf-8'), bcrypt.gensalt())
        registered = User.create(**payload)
        return registered

    def check_password(payload):
        user = User.get(User.username == payload['username'])
        hashed = user.password.encode('utf-8')
        if bcrypt.hashpw(payload['password'].encode('utf-8'), hashed) == hashed:
            return user
        return False