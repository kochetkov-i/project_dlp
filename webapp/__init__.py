from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/signup')
    def sign_up():
        return render_template('signup.html')


    @app.route('/edit')
    def edit_moneycollector():
        return render_template('edit_moneycollector.html')


    @app.route('/withdrawal_money')
    def withdrawal_money():
        return render_template('withdrawal_money.html')


    return app
