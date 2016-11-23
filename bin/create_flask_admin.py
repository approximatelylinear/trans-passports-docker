# -*- coding: utf-8 -*-

#   Stdlib
import os
import sys
import logging
from importlib import import_module

#   3rd party
import click
import yaml
from flask_appbuilder import const as fab_const


LOGGER = logging.getLogger(__name__)

FLASK_PROJECT_DIRECTORY = '/opt/trans_passports/code/trans_passports'


def import_application(app_package, appbuilder):
    sys.path.append(os.getcwd())
    try:
        _app = import_module(app_package)
    except Exception as e:
        click.echo(click.style('Was unable to import {0} Error: {1}'.format(app_package, e), fg='red'))
        exit(3)
    if hasattr(_app, 'appbuilder'):
        return getattr(_app, appbuilder)
    else:
        click.echo(click.style('There in no appbuilder var on your package, you can use appbuilder parameter to config', fg='red'))
        exit(3)


def create_flask_admin(**params):
    curdir = os.path.curdir
    os.chdir(FLASK_PROJECT_DIRECTORY)
    try:
        #   TBD: Put in a yaml file
        params_dflt = {
            'app': 'trans_passports',
            'appbuilder': u'appbuilder',
            'username': u'admin',
            'firstname': u'admin',
            'lastname': u'user',
            'email': u'mjr.berends@gmail.com',
            'password': u'admin'
        }
        #   Update defaults and rename as 'params' for clarity
        params_dflt.update(params)
        params = params_dflt
        _appbuilder = import_application(params['app'], params['appbuilder'])
        #   Describe auth method
        auth_type = {fab_const.AUTH_DB:"Database Authentications",
                    fab_const.AUTH_OID:"OpenID Authentication",
                    fab_const.AUTH_LDAP:"LDAP Authentication",
                    fab_const.AUTH_REMOTE_USER:"WebServer REMOTE_USER Authentication",
                    fab_const.AUTH_OAUTH:"OAuth Authentication"}
        click.echo(click.style('Recognized auth method {0}.'.format(auth_type.get(_appbuilder.sm.auth_type,'No Auth method')), fg='green'))
        #   Create roles
        role_admin = _appbuilder.sm.find_role(_appbuilder.sm.auth_role_admin)
        user = _appbuilder.sm.add_user(
            params['username'], params['firstname'], params['lastname'],
            params['email'], role_admin, params['password'])
        if user:
            click.echo(click.style('Admin User {0} created.'.format(params['username']), fg='green'))
        else:
            click.echo(click.style('No user created an error occured', fg='red'))
    finally:
        #   Change back to the original directory
        os.chdir(curdir)


if __name__ == '__main__':
    create_flask_admin()

