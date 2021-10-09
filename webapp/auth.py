from flask import Blueprint
from . import db
from flask import render_template, redirect, url_for, flash
from webapp.forms import LoginForm, SignUpForm
from webapp.models import Users
from flask_login import login_user, logout_user, current_user
from flask_login import LOGIN_MESSAGE, REFRESH_MESSAGE


LOGOUT_MESSAGE = 'До встречи'
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        'login.html',
        page_title=title,
        form=login_form,
        current_user=current_user)


@auth.route('/prosess-login', methods=['POST', 'GET'])
def procces_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(LOGIN_MESSAGE)
            return redirect(url_for('main.index'))
    flash(REFRESH_MESSAGE)
    return redirect(url_for('login'))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    signup_form = SignUpForm()
    title = "Регистрация"
    user = Users.query.filter_by(username=signup_form.name)
    if user:
        return render_template(
            'signup.html',
            page_title=title,
            form=signup_form,
            current_user=current_user)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))


@auth.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_MESSAGE)
    return redirect(url_for('main.index'))
