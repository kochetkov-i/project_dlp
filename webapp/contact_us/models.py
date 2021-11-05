from webapp import db


class Reporter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(
        db.String(64),
        index=True,
        unique=True
    )

    def __repr__(self):
        return '<Contacter username:{} text:{}>'.format(
            self.username, self.text
        )
