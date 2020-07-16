class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF INVALIDO")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        fatiaUm     = self.cpf[:3]
        fatiaDois   = self.cpf[3:6]
        fatiaTres   = self.cpf[6:9]
        fatiaQuatro = self.cpf[9:]
        return f"{fatiaUm}.{fatiaDois}.{fatiaTres}-{fatiaQuatro}"