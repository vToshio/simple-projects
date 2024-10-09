SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI = \
    '{sgbd}://{user}:{passwd}@{hostname}/{database}'.format(
        sgbd = 'mysql+mysqlconnector',
        user = 'root',
        passwd = 'admin',
        hostname = 'localhost',
        database = 'teste'
    )