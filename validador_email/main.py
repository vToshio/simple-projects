from email import Email
import os

dominios = ['gmail.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'uol.com', 'yahoo.com']

def main():
    while True:
        try:
            while True:
                nome_email = str(input('Insira um email: '))
                email = Email(nome_email, dominios)
                if email.valido:
                    break
                print('Email inválido. Tente novamente.')
            
            print(f'E-mail: {email.endereco}')
            print(f'Nome do usuário: {email.username}')
            print(f'Domínio: {email.dominio}')
        except ValueError:
            print('Valor inválido. Por favor, tente novamente.\n')
        except KeyboardInterrupt:
            os.system('clear')
            print('Programa encerrado.')
            exit(1)

if __name__ == '__main__':
    main()