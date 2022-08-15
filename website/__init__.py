import re
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'i like to eat rice'
    
    return app