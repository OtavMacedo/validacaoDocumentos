import requests



class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.format_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acesso_api(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        if "erro" in dados:
            raise ValueError("CEP inválido")
        return (
            dados["logradouro"],
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
