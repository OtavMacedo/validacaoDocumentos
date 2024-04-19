from acesso_cep import BuscaEndereco
from Cpf_Cnpj import Documento
from datas_br import Cadastro
from TelefonesBr import TelefonesBr

# Demonstração acesso_cep
print("\nDemostração acesso_cep")
obj_busca_endereco = BuscaEndereco(88106470)
print(obj_busca_endereco)
rua, bairro, localidade, estado = obj_busca_endereco.acesso_api()
print(f"{rua}\nBairro {bairro}\n{localidade}\n{estado}")

# Demonstração Cpf_Cnpj
print("\nDemonstração Cpf_Cnpj")
obj_documento = Documento.cria_documento(10141001607)
obj_documento_2 = Documento.cria_documento(15106777000102)

# Demonstração datas_br
print("\nDemonstração datas_br")
obj_datas_br = Cadastro()
print(obj_datas_br)
print(obj_datas_br.mes_cadastro())
print(obj_datas_br.dia_semana())
print(obj_datas_br.tempo_cadastro())

# Demonstração TelefonesBr
print("\nDemonstração TelefonesBr")
obj_telefones_br = TelefonesBr(3434217934)

