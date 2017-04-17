# !usr/bin/python
# -*- coding: utf-8 -*-
# /app/db/models.py

from peewee import Model, CharField, DateTimeField
from playhouse.postgres_ext import PostgresqlExtDatabase
from playhouse.hybrid import hybrid_property
from flask import current_app
from datetime import datetime
from hashids import Hashids
import bcrypt

db = PostgresqlExtDatabase(None, register_hstore=False)

class BaseClass(Model):
    class Meta:
        database = db


class User(BaseClass):
    username = CharField(unique=True)
    password = CharField()
    register_date = DateTimeField()

    @hybrid_property
    def hashed_id(self):
        hashid_instance = Hashids(salt=current_app.config['SECRET_KEY'])
        return hashid_instance.encode(self.id)

    def users_list():
        return [u.username for u in User.select()]

    def add_user(payload):
        payload['register_date'] = datetime.utcnow()
        payload['password'] = bcrypt.hashpw(payload['password'].encode('utf-8'), bcrypt.gensalt())
        registered = User.create(**payload)
        return registered

    def check_password(payload):
        try:
            user = User.get(User.username == payload['username'])
            hashed = user.password.encode('utf-8')
            if bcrypt.hashpw(payload['password'].encode('utf-8'), hashed) == hashed:
                return user
        except User.DoesNotExist:
            return False
        return False