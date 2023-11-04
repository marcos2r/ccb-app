from flask import Flask

from ccb.extensions import configuration
from ccb.extensions import database

from ccb.blueprints import restapi


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    restapi.init_app(app)
    return app
