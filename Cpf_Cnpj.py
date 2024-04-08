from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return f"CPF válido\n{mascara.mask(self.cpf)}"


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def valida(self, documento):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(documento)

    def format(self):
        mascara = CNPJ()
        return f"CNPJ válido\n{mascara.mask(self.cnpj)}"

    def __str__(self):
        return self.format()
