#!/usr/bin/python3
"""
Package initializer for views in flask app

Modules Imported: Blieprint

Blueprint: Create reusable flask routes
"""
from flask import Blueprint


app_views = Blueprint(
    'app_views',
    __name__,
    template_folder='',
    static_folder=''
)

# Default url prefix is '/api/v1'

from api.v1.views.index import *
from api.v1.courses import *
from api.v1.lessons import *
from api.v1.quiz import *
from api.v1.result import *
from api.v1.topics import *
