from flask import render_template, Blueprint


route = Blueprint('route', __name__)


@route.route('/')
def index():
    title = "Главная"
    return render_template('index.html', page_title=title)


@route.route('/profile')
def sign_up():
    title = "Приветствие"
    return render_template('profile.html', page_title=title)


@route.route('/edit')
def edit_moneycollector():
    title = "Редактирование"
    return render_template('edit_moneycollector.html', page_title=title)


@route.route('/withdrawal_money')
def withdrawal_money():
    title = "Сбор"
    return render_template('withdrawal_money.html', page_title=title)
