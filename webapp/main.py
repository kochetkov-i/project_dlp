from flask import render_template, Blueprint
from flask_login import current_user, login_required
from webapp.forms import WithdrawalMoneyForm


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


@main.route('/edit')
def edit_moneycollector():
    title = "Редактирование"
    return render_template(
        'collect/edit_moneycollector.html',
        page_title=title,
        current_user=current_user)


@main.route('/withdrawal_money')
def withdrawal_money():
    withdrawa_form = WithdrawalMoneyForm()
    title = "Сбор"
    return render_template(
        'collect/withdrawal_money.html',
        page_title=title,
        form=withdrawa_form,
        current_user=current_user)
