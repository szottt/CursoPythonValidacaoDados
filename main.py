from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from datasbr import DatasBr
from acesso_cep import BuscaEndereco
import requests

exemplo_cpf = "94561576010"
exemplo_cnpj = "35379838000112"
telefone = "11976453329"
cep = "01001000"

cpf_um = Documento.cria_documento(exemplo_cpf)
cnpj_um = Documento.cria_documento(exemplo_cnpj)
telefone_um = TelefonesBr(telefone)
hora_cadastro = DatasBr()
tempo_cadastro = hora_cadastro.tempo_cadastro()
objeto_cep = BuscaEndereco(cep)
logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(f'''
CPF: {cpf_um}
CNPJ: {cnpj_um}
Telefone: {telefone_um}'
Hora do Cadastro: {hora_cadastro}
Tempo de Cadastro: {tempo_cadastro}
Dados Cadastrais:
Rua: {logradouro}
Bairro: {bairro}
Cidade: {cidade}
Uf: {uf}
''')
