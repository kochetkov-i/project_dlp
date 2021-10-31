from flask import render_template, Blueprint
from flask_login import current_user
from webapp.collect.models import Collections
from sqlalchemy import asc


blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    collections = Collections.query.filter_by(
        is_end=False
    ).order_by(
        asc(Collections.finish_time)
    )
    title = "Главная"
    return render_template(
        'main/index.html',
        page_title=title,
        current_user=current_user,
        data=collections)

