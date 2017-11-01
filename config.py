import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app): pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # mysql-config
    MYSQL_USER = os.getenv('CML_MYSQL_USER')
    MYSQL_PASS = os.getenv('CML_MYSQL_PASS')
    MYSQL_HOST = os.getenv('CML_MYSQL_HOST')
    MYSQL_DATABASE = 'cml_develop'
    SQLALCHEMY_DATABASE_URI = 'mysql://'+MYSQL_USER+':'+MYSQL_PASS+'@'+MYSQL_HOST+'/'+MYSQL_DATABASE


class TestingConfig(Config):
    MYSQL_USER = os.getenv('CML_MYSQL_USER')
    MYSQL_PASS = os.getenv('CML_MYSQL_PASS')
    MYSQL_HOST = os.getenv('CML_MYSQL_HOST')
    MYSQL_DATABASE = 'cml_test'
    SQLALCHEMY_DATABASE_URI = 'mysql://' + MYSQL_USER + ':' + MYSQL_PASS + '@' + MYSQL_HOST + '/' + MYSQL_DATABASE
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    MYSQL_USER = os.getenv('CML_MYSQL_USER')
    MYSQL_PASS = os.getenv('CML_MYSQL_PASS')
    MYSQL_HOST = os.getenv('CML_MYSQL_HOST')
    MYSQL_DATABASE = 'cml_product'
    SQLALCHEMY_DATABASE_URI = 'mysql://' + MYSQL_USER + ':' + MYSQL_PASS + '@' + MYSQL_HOST + '/' + MYSQL_DATABASE


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
