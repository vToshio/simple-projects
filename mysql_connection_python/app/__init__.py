from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app() -> object:
    '''Instancia um objeto da classe Flask e o retorna para o main.py'''
    
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
