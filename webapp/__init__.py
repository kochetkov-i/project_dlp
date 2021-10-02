from flask.app import Flask
from flask_migrate import Migrate
from webapp.config.default import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = False
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app.config.from_pyfile('config.py', silent=True)
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    return app

from webapp import models, routes

