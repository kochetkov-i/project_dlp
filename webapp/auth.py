from flask import Blueprint
from . import db
from flask import render_template, redirect, url_for, flash
from webapp.forms import LoginForm, SignUpForm
from webapp.models import Users, Collections
from flask_login import login_required, login_user, logout_user, current_user
from webapp.auth_messages_const import LOGIN_MESSAGE, LOGOUT_MESSAGE
from webapp.auth_messages_const import USER_ALREADY_EXIST_MESSAGE
from webapp.auth_messages_const import INCORRECT_FILL_FORM_MESSAGE
from webapp.auth_messages_const import FAIL_LOGIN_MESSAGE

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
        user = Users.query.filter_by(useremail=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(LOGIN_MESSAGE)
            return redirect(url_for('main.index'))
    flash(FAIL_LOGIN_MESSAGE)
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
    user = Users.query.filter_by(useremail=signup_form.email.data).first()
    if user:
        flash(USER_ALREADY_EXIST_MESSAGE)
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

    flash(INCORRECT_FILL_FORM_MESSAGE)
    return redirect(url_for('auth.signup'))


@auth.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_MESSAGE)
    return redirect(url_for('main.index'))
