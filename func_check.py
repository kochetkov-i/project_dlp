from datetime import datetime
from webapp import create_app
from webapp.collect.models import Collections, db

app = create_app()

with app.app_context():
    def check_collect():
        now = datetime.now()
        active_collect = Collections.query.filter_by(is_end=False)
        for collect in active_collect:
            finish_time = collect.finish_time
            if collect.amount >= collect.finish_count or now >= finish_time:
                collect.is_end = True

                db.session.refresh(collect)
                db.session.commit()
