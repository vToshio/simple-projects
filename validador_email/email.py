import re

class Email:
    def __init__(self, email:str, lista_dominios:list) -> None:
        '''
        Construtor da classe Email
        '''
        self.endereco = self.sanitize(email)
        self.valido = self.validate(lista_dominios)
        self.username = self.get_username()
        self.dominio = self.get_domain()

    def sanitize(self, email:str) -> str:
        '''
        Retira espaços em branco do início e do fim da string do email
        '''
        if isinstance(email, str):
            return email.strip()
        return ''

    def validate(self, dominios:list) -> bool:
        '''
        Retorna True se um endereço de e-mail for válido de acordo com os padrões
        de uma regex, que aceita caracteres alfanuméricos e os caracteres '.', '-' e '_'.
        Retorna False caso o endereço de email não seja válido.
        '''
        if not self.endereco:
            return False
        padrao = re.compile(r'^[a-zA-Z0-9._-]+@(?:' + '|'.join(map(re.escape, dominios)) + r')$')
        if padrao.match(self.endereco):
            return True
        return False
    
    def get_username(self) -> str:
        '''Retorna o nome do usuário a partir do endereço de email.'''
        return self.endereco[0: self.endereco.find('@')]

    def get_domain(self) -> str:
        '''Retorna o domínio a partir do endereço de email.'''
        return self.endereco[self.endereco.find('@')+1:]
            
    def __eq__(self, other):
        return isinstance(other, Email) and self.endereco == other.endereco
    
    def __str__(self):
        return f'{self.endereco} | {self.valido}'
