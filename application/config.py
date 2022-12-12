class Config(object):
    DEBUG = True
    STATIC_URL = "static"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    AUTH_LOGIN_ENDPOINT = 'login'
    AUTH_PASSWORD_HASH = 'sha512_crypt'
    AUTH_PASSWORD_SALT = 'add_salt'
    SECRET_KEY = 'acndef'
    SESSION_COOKIE_SALT = 'salt_key'