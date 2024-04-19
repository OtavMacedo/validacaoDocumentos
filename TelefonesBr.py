import re


class TelefonesBr:
    # Inicializa o objeto, transforma a entrada em string, verifica se a entrada é valida
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_telefone(telefone):
            self.numero = telefone
            print(self)

        else:
            raise ValueError("Telefone inválido")

    def __str__(self):
        return self.format_numero()

    # Método para validação
    def valida_telefone(self, telefone):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    # Método para formatação
    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        if not resposta.group(1):
            return f"({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        else:
            return f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"