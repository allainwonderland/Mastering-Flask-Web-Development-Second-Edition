class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    PYMYSQL_DATABASE_URI ='mysql+pymysql://user:password@ip:port/db_name'
    CX_ORACLE_DATABASE_URI = 'oracle+cx_oracle://user:password@ip:port/db_name'

SQLALCHEMY_ECHO = True.