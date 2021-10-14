from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from webapp.config import Config
from webapp.auth.models import Users
from webapp.auth.views import blueprint as auth_blueprint
from webapp.main import main as main_blueprint


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
admin = Admin(name=Config.FLASK_APP)


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    admin.init_app(app)
    admin.add_view(ModelView(Users, db.session))

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
