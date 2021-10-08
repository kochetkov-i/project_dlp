from flask import render_template, Blueprint
from flask_login import current_user, login_required
from webapp.forms import WithdrawalMoneyForm


route = Blueprint('route', __name__)


@route.route('/')
def index():
    title = "Главная"
    return render_template(
        'index.html',
        page_title=title,
        current_user=current_user)


@route.route('/profile')
def sign_up():
    title = "Приветствие"
    return render_template(
        'profile.html',
        page_title=title,
        current_user=current_user)


@route.route('/edit')
def edit_moneycollector():
    title = "Редактирование"
    return render_template(
        'edit_moneycollector.html',
        page_title=title,
        current_user=current_user)


@route.route('/withdrawal_money')
def withdrawal_money():
    withdrawa_form = WithdrawalMoneyForm()
    title = "Сбор"
    return render_template(
        'withdrawal_money.html',
        page_title=title,
        form=withdrawa_form,
        current_user=current_user)


@route.route('/admin')
@login_required
def admin_index():
    return 'Привет админ'
