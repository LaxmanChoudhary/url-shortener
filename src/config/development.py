from . import Config
import os

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'dev.sqlite')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres.dlkmllgjnugadfulpsbk:cbA7lWddCxl51cjH@aws-0-us-west-1.pooler.supabase.com:6543/postgres"