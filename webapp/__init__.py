from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from webapp.config import Config


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

    admin.init_app(app)

    from webapp.auth.views import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from webapp.main.views import blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    from webapp.collect.views import blueprint as collect_blueprint
    app.register_blueprint(collect_blueprint)

    return app


from webapp.admin import admin
