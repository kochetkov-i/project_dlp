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
        return redirect(url_for('main.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        'login.html',
        page_title=title,
        form=login_form,
        current_user=current_user)


@auth.route('/prosess-login', methods=['POST'])
def procces_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(LOGIN_MESSAGE)
            return redirect(url_for('main.index'))
    flash(REFRESH_MESSAGE)
    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    signup_form = SignUpForm()
    title = "Регистрация"
    return render_template(
        'signup.html',
        page_title=title,
        form=signup_form)


@auth.route('/procces_signup', methods=['POST'])
def procces_signup():
    signup_form = SignUpForm()
    user = Users.query.filter_by(username=signup_form.name.data).first()
    if user:
        flash('Такой пользователь уже есть')
        return redirect(url_for('auth.signup'))
    if signup_form.validate_on_submit():
        new_user = Users(
            username=signup_form.name.data,
            usersurname=signup_form.surname.data,
            useremail=signup_form.email.data,
            userphone=signup_form.phone.data,
            userrole="user")

        new_user.set_password(signup_form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    flash('Форма заполнена некоректно')
    return redirect(url_for('auth.signup'))


@auth.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_MESSAGE)
    return redirect(url_for('main.index'))
