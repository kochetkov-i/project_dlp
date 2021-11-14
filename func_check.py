from datetime import datetime
from webapp import create_app
from webapp.collect.models import Collections, db

app = create_app()


with app.app_context():
    now = datetime.now()
    active_collect = Collections.query.filter_by(is_end=False)
    for collect in active_collect:
        finish_time = collect.finish_time
        if collect.current_amount >= collect.finish_count or now >= finish_time:
            collect.is_end = True

            db.session.add(collect)
            db.session.commit()

