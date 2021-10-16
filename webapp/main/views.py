from flask import render_template, Blueprint
from flask_login import current_user


blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    title = "Главная"
    return render_template(
        'main/index.html',
        page_title=title,
        current_user=current_user)


@blueprint.route('/contact_us')
def contact_us():
    title = "Форма связи"
    return render_template(
        'main/contactus.html',
        page_title=title,
        current_user=current_user)
