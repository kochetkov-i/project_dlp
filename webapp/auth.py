from flask import Blueprint
from . import db
from flask import render_template, redirect, url_for, request
from webapp.forms import LoginForm
from webapp.models import Collector_users
from werkzeug.security import generate_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    surname = request.form.get('surname')
    phone = request.form.get('phone')
    password = request.form.get('password')

    user = Collector_users.query.filter_by(email=email)
    if user:
        return render_template('signup.html')

    new_user = Collector_users(
        email=email,
        name=name,
        surname=surname,
        Phone=phone,
        password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))


@auth.route('/logout')
def logout():
    return 'Logout'
