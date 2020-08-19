import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        if len(self.numero) == 12:
            padrao = "([0-9]{3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao,self.numero)
        else:
            padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao,self.numero)
        numero_formatado = f"+0{resposta.group(1) if resposta.group(1) != None else 55}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado


