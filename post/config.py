import os
class Config:
    SECRET_KEY=os.urandom(32)
    @staticmethod
    def init_app():
        pass

class DevelopmentConfigration(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfigration(Config):
    DEBUG= False
    SQLALCHEMY_DATABASE_URI = "postgresql://newrady:iti@localhost:5432/itir"



projectConfig= {
    'dev': DevelopmentConfigration,
    'prod': ProductionConfigration
}



