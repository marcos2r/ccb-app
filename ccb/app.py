from flask import Flask
from ccb.extensions import configuration
from ccb.extensions import database

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
