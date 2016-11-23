# -*- coding: utf-8 -*-

__author__ = 'MJ Berends'
__email__ = 'mjr.berends@gmail.com'
__version__ = '0.1.0'
__all__ = []

#	Stdlib
import logging

"""
TBD: Move this elsewhere
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)


from trans_passports.app.flask_app import flask_app, db, appbuilder
__all__.append('flask_app')
__all__.append('db')
__all__.append('appbuilder')


from trans_passports.app import views
__all__.append('views')
