import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
#SECRET_KEY = 'aed691be502fc12e1babcb0c2d1841e0e916be8f7910b2732e265b2d43b03612'
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") 

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
