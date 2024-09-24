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
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config.from_object(config.Config)  # configs not set yet
swagger = Swagger(app)

# cors activation code

with app.app_context():
    app.register_blueprint(app_views, url_prefix='/api/v1')


#@app.teardown_appcontext
#def close_app():
#    """Closes storage when app is closed"""

@app.route('/api/v1', strict_slashes=False)
def welcome():
    return 'Welcome to Unlearn'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
