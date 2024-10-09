from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import views
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True) 