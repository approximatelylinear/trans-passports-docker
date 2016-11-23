# -*- coding: utf-8 -*-

#	Stdlib
import logging

#	3rd party

#		Flask
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

#	Custom
from trans_passports.app.flask_app import appbuilder, db

LOGGER = logging.getLogger(__name__)

"""
    Create your Views::
    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)
    Next, register your Views::
    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
    	render_template(
    		'404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404)


#	After all views have been defined and added.
db.create_all()
