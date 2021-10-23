from webapp.models import Collections
from flask import Blueprint, render_template
from flask_login import current_user, login_required


adver = Blueprint('adver', __name__)


@adver.route('/user_list')
def get_info():
    information = Collections.query.filter_by(collector_user_id=current_user.id).all()
    return render_template('user_list_adver/advertisement.html', info=information)

@login_required
def user_list():
    if current_user.is_authenticated:
        title = 'Лист объявлений'
        username = current_user
        advertisement = Collections.query.filter_by(collector_user_id=username.id).all()
        return render_template(
            'user_list_adver.user_list.html',
            title=title,
            username=username,
            advertisement=advertisement)
    else:
        return redirect(url_for('login'))
