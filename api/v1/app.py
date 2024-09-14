#!/usr/bin/python3
"""
Modules Imported: Flask
Flask: web app franework
swagger: flasgger's web app testing and documen interface

"""
from flask import Flask
from flasgger import Swagger


app = Flask(__name__, instance_relative_config=False)
swagger = Swagger(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
