from __init__ import db

'''
    Classe deve ter o mesmo nome da tabela relacional e seus
atributos devem tem os mesmos nomes de cada coluna da tabela 
'''
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    passwd = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.user_name}>'