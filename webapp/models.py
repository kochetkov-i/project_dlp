from app import db

class Collector_users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    Phone = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User Id:{self.id} Name:{self.name} Surname:{self.surname}>'


class Collections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collector_user_id = db.Column(db.Integer, db.ForeignKey('Collector_users.id'),nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)
    finish_count = db.Column(db.Integer, nullable=False)
    finish_time = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    last_modify = db.Column(db.DateTime, nullable=False)
    is_end = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Collection Id:{self.id} Name:{self.name} Is_End:{self.is_end}>'


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collections_id = db.Column(db.Integer, db.ForeignKey('collections.id'),nullable=False)
    link = db.Column(db.String(256), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Image Id:{self.id} Collection Id:{self.collections_id}>'
