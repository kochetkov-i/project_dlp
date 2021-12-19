from webapp import create_app
from webapp.collect.models import Collections, db
from datetime import datetime

app = create_app()

with app.app_context():
    for collect in Collections.query.filter_by(is_end=False):
        if (collect.current_amount >= collect.finish_count) or (datetime.now() >= collect.finish_time):
            collect.is_end = True

            db.session.add(collect)
            db.session.commit()
