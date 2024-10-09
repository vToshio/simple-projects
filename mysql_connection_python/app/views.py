from flask import Blueprint, render_template
from models import Users

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    user_list = Users.query.order_by(Users.id)
    return render_template('index.html', nome='teste.py', users_list=user_list) 