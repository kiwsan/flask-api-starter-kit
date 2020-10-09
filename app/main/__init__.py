from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config.from_object(config_by_name[config_name])

    return app
