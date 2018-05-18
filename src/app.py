from flask import Flask
from api import api
from db import db
from os import getenv

app = Flask(__name__)

def db_uri_setup():
    return 'mysql://root:password@server/db'

if __name__=='__main__':
    with app.app_context():

        # Connect RESTful API to Flask Server
        api.init_app(app)

        # Get DB connection path if specified, else default to sqlite
        db_uri = getenv('SQLALCHEMY_DATABASE_URI')

        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri if db_uri else 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_RECORD_QUERIES'] = True
        app.config['SQLALCHEMY_ECHO'] = True

        # Connect DB instance to Flask Server
        db.init_app(app)
        db.drop_all() # Clear all tables [DEBUG ONLY]
        db.create_all() # Create any tables if they do not exist

    app.run(debug=True) # Run Flask Server
