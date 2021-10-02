class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://collector_user_db:password@localhost:5432/db_moneycollect'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    FLASK_APP='webapp'