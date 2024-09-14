#!/usr/bin/python3
"""
Modules Imported: Flask
Flask: web app franework
swagger: flasgger's web app testing and documen interface
CORS: allows cross prigin resouece sharing across diff endpoints

"""
from views import app_views
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

swagger = Swagger(app)

# cors activation


@app.teardown_appcontext
def close_app():
    """Closes storage when app is closed"""
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
