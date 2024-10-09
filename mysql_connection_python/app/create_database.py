import mysql.connector as sqlconnect
from mysql.connector import errorcode

# Conectando ao SGBD
print('Connecting to the database...')
try:
    conn = sqlconnect.connect(
        user = 'root',
        password = 'admin',
        host = 'localhost',
    )
except sqlconnect.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Nome de usuário ou senha inválidos.')
        exit(1)
    else:
        print(err)
        exit(1)

# Definindo o cursor
cursor = conn.cursor() 

# Criando o banco de dados e definindo as tabelas

cursor.execute(f'CREATE DATABASE IF NOT EXISTS `teste`;')
cursor.execute(f'USE teste;')

create_users_table = '''
    CREATE TABLE IF NOT EXISTS `users`(
        `user_id` int(11) NOT NULL AUTO_INCREMENT,
        `user_name` varchar(30) NOT NULL,
        `user_role` varchar(20) NOT NULL,
        `user_passwd` varchar(100) NOT NULL,
        PRIMARY KEY (`user_id`)    
        );
'''

add_master_user = """
    INSERT INTO users(user_name, user_role, user_passwd)
    VALUES ('master', 'master', 'master')
"""

cursor.execute(create_users_table)
cursor.execute(add_master_user)
conn.commit()

print(f'Database teste created sucessfully!')

cursor.close()
conn.close()