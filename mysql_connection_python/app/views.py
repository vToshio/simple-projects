from flask import Blueprint, render_template
from models import User

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    user_list = User.query.order_by(User.id)
    return render_template('index.html', nome='teste.py', users_list=user_list) 