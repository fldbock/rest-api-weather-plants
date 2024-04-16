class LocalConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./local_database.db'

class TestConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test_database.db'