from webapp import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Collector_users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, index=True, unique=True)
    Phone = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    def set_password(self, password):
        print(self)
        print(password)
        self.password_hash = generate_password_hash(password)

    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)

    @property
    def is_admin(self):
        return self.is_admin

    def __repr__(self):
        return '<User Id:{} Name:{} Surname:{} Email:{}>'.format(
            self.id, self.name, self.surname, self.email)


class Collections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collector_user_id = db.Column(
        db.Integer,
        db.ForeignKey(Collector_users.id),
        nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)
    finish_count = db.Column(db.Integer, nullable=False)
    finish_time = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    last_modify = db.Column(db.DateTime, nullable=False)
    is_end = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Collection Id:{} Name:{} Is_End:{}>'.format(
            self.id, self.name, self.is_end
        )


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collections_id = db.Column(
        db.Integer,
        db.ForeignKey('collections.id'),
        nullable=False)
    link = db.Column(db.String(256), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Image Id:{} Collection Id:{}>'.format(
            self.id, self.collections_id
        )


@login_manager.user_loader
def load_user(user_id):
    return Collector_users.query.get(int(user_id))
