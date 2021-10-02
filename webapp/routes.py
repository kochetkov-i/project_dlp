from flask import Flask, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

from webapp import app, db
from webapp.models import Collector_users

   
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def sign_up():
    return render_template('profile.html')


@app.route('/edit')
def edit_moneycollector():
    return render_template('edit_moneycollector.html')


@app.route('/withdrawal_money')
def withdrawal_money():
    return render_template('withdrawal_money.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
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


@app.route('/logout')
def logout():
    return 'Logout'