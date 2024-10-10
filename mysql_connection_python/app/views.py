from flask import Blueprint, render_template, flash, redirect, url_for, request
from __init__ import db
from models import User

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    user_list = User.query.order_by(User.id)
    return render_template('index.html', nome='teste.py', users_list=user_list) 

@views.route('/adicionar', methods=['POST'])
def create():
    name = request.form['username']
    password = request.form['password']
    job = request.form['job']
    role = request.form['role']
    
    cadastro = User.query.filter_by(name=name).first()
    if cadastro:
        flash('Usuário já cadastrado.', 'error')
        return redirect(url_for('views.index'))
    
    new_register = User(name=name, passwd=password, job=job, role=role)
    db.session.add(new_register)
    db.session.commit()

    return redirect(url_for('views.index'))

@views.route('/remover')
def remove():
    pass

@views.route('/editar/<int:id>')
def edit(id):
    pass