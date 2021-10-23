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


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
