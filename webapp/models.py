from webapp import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    usersurname = db.Column(db.String(64))
    useremail = db.Column(
        db.String(64),
        index=True,
        unique=True)
    userphone = db.Column(db.String(32))
    userpassword = db.Column(db.String(128))
    userrole = db.Column(db.String(32))
    is_deleted = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.userpassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.userpassword, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User Id:{} Name:{} Surname:{} Email:{}>'.format(
            self.id, self.username, self.usersurname, self.useremail)


class Collections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collector_user_id = db.Column(
        db.Integer,
        db.ForeignKey(Users.id),
        nullable=False)
    collection_name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)
    finish_count = db.Column(db.Integer, nullable=False)
    finish_time = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    last_modify = db.Column(db.DateTime, nullable=False)
    is_end = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Collection Id:{} Name:{} Is_End:{}>'.format(
            self.id, self.collection_name, self.is_end
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
    return Users.query.get(int(user_id))
