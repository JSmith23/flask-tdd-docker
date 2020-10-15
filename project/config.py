class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    Testing = True

class ProductConfig(BaseConfig):
    pass




