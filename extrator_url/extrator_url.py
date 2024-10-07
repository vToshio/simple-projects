import re

class ExtratorURL:
    def __init__(self, url: str) -> None:
        self.url = self.sanitiza_url(url)
        self.valida = self.valida_url()

    def sanitiza_url(self, url) -> str:
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self) -> bool:
        if not self.url:
            raise ValueError('URL está vazia')
        url_padrao = re.compile(r'^(http(s)?://)?(www\.)[a-zA-Z0-9-]{3,}+[\.a-z]+(/[a-zA-Z0-9-]*)*(\?[a-zA-Z0-9-]{1,}(=)[a-zA-Z0-9-]{1,}+(&[a-zA-Z0-9-]{1,}(=)[a-zA-Z0-9-]{1,})*)?$')
        if not url_padrao.match(self.url):
            return False
        return True

        
    def get_url_base(self) -> str:    
        indice_interrogacao = self.url.find('?')
        if type(indice_interrogacao) != str:
            return self.url[:]
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self) -> str:
        indice_interrogacao = self.url.find('?')
        if (indice_interrogacao>0):
            url_parametros = self.url[indice_interrogacao+1:]
            return url_parametros
        return ''

    def get_valor_parametro(self, busca: str) -> any:
        query_string = self.get_url_parametros().lstrip('?') 
        padrao = re.compile(re.escape(busca) + r'(=)[a-zA-Z0-9-]{1,}$')

        match = re.search(padrao, query_string)
        if match:
            index_igual = match.group().find('=')
            return match.group()[index_igual+1:]
        return None

        
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        if self.valida:
            return f'{self.url} | {self.valida}\nParâmetros: {self.get_url_parametros()}\nURL Base: {self.get_url_base()}'
        return f'{self.url} | {self.valida}'

    def __eq__(self, other):
        return self.url == other.url 