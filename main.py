from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from datasbr import DatasBr
from datetime import datetime

exemplo_cpf = "94561576010"
exemplo_cnpj = "35379838000112"
telefone = "11976453329"

cpf_um = Documento.cria_documento(exemplo_cpf)
cnpj_um = Documento.cria_documento(exemplo_cnpj)
telefone_um = TelefonesBr(telefone)
hora_cadastro = DatasBr()

print(f'''
CPF: {cpf_um}
CNPJ: {cnpj_um}
Telefone: {telefone_um}'
Hora do Cadastro: {hora_cadastro}
''')