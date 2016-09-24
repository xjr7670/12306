class Config(object):
    SECRET_KEY = 'xjr7670'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATONS = True
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass

config = {
        'default': Config
        }
