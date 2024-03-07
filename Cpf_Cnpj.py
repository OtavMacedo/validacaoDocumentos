from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento):
        documento = str(documento)
        self.documento = documento
        if self.verifica_doc(documento):
            print(self)
        else:
            raise ValueError("Documento inválido")
    
    def valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
        
    def valida_cnpj(self, cnpj):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(cnpj)
        
    def verifica_doc(self, documento):
        if len(documento) == 11:
            self.cpf = documento
            return self.valida_cpf(documento)
        elif len(documento) == 14:
            self.cnpj = documento
            return self.valida_cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida")
        
    def __str__(self):
        if len(self.documento) == 11:
            mascara = CPF()
            return f"CPF válido\n{mascara.mask(self.cpf)}"
        else:
            mascara = CNPJ()
            return f"CNPJ válido\n{mascara.mask(self.cnpj)}"
