import os

class Config:
    # SQLAlchemy database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # run the code once in create_app()
    INITIALIZE_ON_STARTUP = True

    # Debug mode
    DEBUG = os.getenv('DEBUG') == 'True'
