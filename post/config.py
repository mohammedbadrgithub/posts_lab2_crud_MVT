
class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfigration(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfigration(Config):
    DEBUG= False
    # postgresql:://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/posts"



projectConfig= {
    'dev': DevelopmentConfigration,
    'prod': ProductionConfigration
}