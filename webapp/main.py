from flask import render_template, Blueprint
from flask_login import current_user


main = Blueprint('main', __name__)


@main.route('/')
def index():
    title = "Главная"
    return render_template(
        'index.html',
        page_title=title,
        current_user=current_user)


@main.route('/contact_us')
def contact_us():
    title = "Форма связи"
    return render_template(
        'contactus.html',
        page_title=title,
        current_user=current_user)
