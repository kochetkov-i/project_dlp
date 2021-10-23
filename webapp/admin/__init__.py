from flask_admin.contrib.sqla.view import ModelView
from webapp import db
from webapp.auth.models import Users
from webapp.collect.models import Collections
from webapp.admin.views import WebappModelView
from webapp.config import Config
from flask_admin import Admin


admin = Admin(name=Config.FLASK_APP, index_view=WebappModelView())
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Collections, db.session))
