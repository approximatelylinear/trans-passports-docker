# -*- coding: utf-8 -*-

#	Stdlib
import logging

#	3rd party

#		Flask
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder


flask_app = Flask(__name__)
flask_app.config.from_object('trans_passports.app.config')

db = SQLA(flask_app)

appbuilder = AppBuilder(flask_app, db.session)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event
#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""
