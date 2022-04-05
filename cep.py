# Nome : cep.py
# Desenvolvedor : Marco Aurélio
# Data : 04-04-2022
import requests
from bs4 import BeautifulSoup
import json

class BuscaCEP:
    Numero = ""
    Cep = ""
    Logradouro = ""
    Complemento = ""
    Bairro = ""
    Localidade = ""
    Uf = ""
    Ibge = ""
    Gia = ""
    Ddd = ""
    Siafi = ""
    
    def __init__(self, numero):
        self.Numero = numero
    
    def Buscar(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.Numero)
        
        res = requests.get(url)
        html_page = res.text
        soup = BeautifulSoup(html_page, 'html.parser')
        dados = json.loads(soup.text)
        self.Cep = dados['cep']
        self.Logradouro = dados['logradouro']
        self.Complemento = dados['complemento']
        self.Bairro = dados['bairro']
        self.Localidade = dados['localidade']
        self.Uf = dados['uf']
        self.Ibge = dados['ibge']
        self.Gia = dados['gia']
        self.Ddd = dados['ddd']
        self.Siafi = dados['siafi']
     
    def get_cep(self):
        return self.Cep
    
    def get_logradouro(self):
        return self.Logradouro
    
    def get_complemento(self):
        return self.Complemento
    
    def get_bairro(self):
        return self.Bairro
    
    def get_localidade(self):
        return self.Localidade
    
    def get_uf(self):
        return self.Uf
    
    def get_ibge(self):
        return self.Ibge
    
    def get_gia(self):
        return self.Gia
    
    def get_ddd(self):
        return self.Ddd
    
    def get_siafi(self):
        return self.Siafi
        