from webapp import db
from webapp.collect.models import Collections
from datetime import datetime


def check_collect():
    now = datetime.now()
    all_collect = Collections.query.filter_by(is_end=False)
    for collect in all_collect:
        if collect.amount >= collect.finish_count or now >= collect.finish_time:
            collect.is_end = True

            db.session.refresh(collect)
            db.session.commit()


def main():
    check_collect()


if __name__ == "__main__":
    main()
