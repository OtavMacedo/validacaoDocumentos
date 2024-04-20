from validate_docbr import CPF, CNPJ


class Documento:

    # Método factory, utilizado para trazer mais flexibilidade ao código
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        documento = documento.replace('.', '').replace('-', '').replace('/', '')
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
            print(self)
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    # Utiliza a biblioteca validade_docbr para realizar os cálculos e verificar se o CPF é valido
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    # Formata o CPF
    def format(self):
        mascara = CPF()
        return f"CPF válido\n{mascara.mask(self.cpf)}"


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
            print(self)
        else:
            raise ValueError("CNPJ inválido")

    # Utiliza a biblioteca validade_docbr para realizar os cálculos e verificar se o CNPJ é valido
    def valida(self, documento):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(documento)

    # Formata o CNPJ
    def format(self):
        mascara = CNPJ()
        return f"CNPJ válido\n{mascara.mask(self.cnpj)}"

    def __str__(self):
        return self.format()
