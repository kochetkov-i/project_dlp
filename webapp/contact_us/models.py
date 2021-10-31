from webapp import db


class Contacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    text = db.Column(db.Text(300), nullable=False)

    def __repr__(self):
        return '<Contacter username:{} text:{}>'.format(
            self.username, self.text
        )
