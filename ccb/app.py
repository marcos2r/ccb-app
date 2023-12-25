from flask import Flask
from dynaconf import FlaskDynaconf
from ccb.extensions import database
from ccb.blueprints import restapi


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=["settings.toml"])
    configuration.init_app(app)
    database.init_app(app)
    restapi.init_app(app)
    return app
