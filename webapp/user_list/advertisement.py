from webapp.models import Collections
from flask import Blueprint, render_template
from flask_login import current_user


adver = Blueprint('adver', __name__)


@adver.route('/user_list')
def get_info():
    information = Collections.query.filter_by(collector_user_id=current_user.id).all()
    return render_template('user_list_adver/advertisement.html', info=information)
