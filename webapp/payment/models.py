from webapp import db


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collections_id = db.Column(
        db.Integer,
        db.ForeignKey('collections.id'),
        nullable=False)
    operation_id = db.Column(db.String)
    status = db.Column(db.String)
    datetime = db.Column(db.String)
    title = db.Column(db.String)
    pattern_id = db.Column(db.String)
    direction = db.Column(db.String)
    amount = db.Column(db.String)
    label = db.Column(db.String)
    type = db.Column(db.String)

    def __repr__(self):
        return '<Transaction Id:{} Status:{} Amount:{}>'.format(
            self.id, self.status, self.amount
        )
