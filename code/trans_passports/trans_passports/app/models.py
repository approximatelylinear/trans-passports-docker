# -*- coding: utf-8 -*-

#	Stdlib
import logging

#	3rd party

#		Flask
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

#		SQLalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

LOGGER = logging.getLogger(__name__)

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""
