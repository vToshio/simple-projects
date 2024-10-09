from flask import Flask, render_template, url_for
from app.create_database import connect
from app.views import views

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(views)
db = connect('localhost', 'root', 'admin', 'teste')

if __name__ == '__main__':
    app.run(debug=True)