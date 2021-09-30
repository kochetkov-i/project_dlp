from flask import Flask, render_template
from flask_migrate import Migrate
import psycopg2


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #здесь планировался дефолтный конфиг но что-то пошло не так
    app.config.from_pyfile('config.py')
    db = psycopg2.connect(**app.config['DATABASE_CRED'])
    migrate = Migrate(app, db)


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
