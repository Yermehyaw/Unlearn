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

from .index import *
from .courses import *
from .lessons import *
from .quiz import *
from .result import *
from .topics import *
