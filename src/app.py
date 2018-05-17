from flask import Flask
from api import api

app = Flask(__name__)

if __name__=='__main__':
    with app.app_context():
        api.init_app(app)
    app.run(debug=True) # Run Flask Server