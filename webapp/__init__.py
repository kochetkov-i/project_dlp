from flask_migrate import Migrate
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


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

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    admin.init_app(app)
    from webapp.models import Users
    admin.add_view(ModelView(Users, db.session))

    return app
