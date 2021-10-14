from webapp import db
from webapp.auth.models import Users


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
