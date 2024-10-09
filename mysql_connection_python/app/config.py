from dotenv import load_dotenv

SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI = \
    '{sgbd}://{user}:{passwd}/{hostname}/{database}'.format(
        sgbd = 'mysql+mysqlconnector',
        user = load_dotenv('USERNAME'),
        passwd = load_dotenv('PASSWD'),
        hostname = load_dotenv('HOST'),
        database = load_dotenv('DATABASE')
    )