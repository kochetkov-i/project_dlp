class Config:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://collector_user_db:password@localhost:5432/db_moneycollect'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'zgsbd345tnyutBUYFUTc576239457rke6rsy324sfgtryt'
    FLASK_APP = 'webapp'
    FLASK_ADMIN_SWATCH = 'cerulean'
