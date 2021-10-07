from flask_migrate import Migrate
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes import route as route_blueprint
    app.register_blueprint(route_blueprint)

    return app
