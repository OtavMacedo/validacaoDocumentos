from Cpf_Cnpj import Documento

# pip install validate-docbr

# Digite o CPF ou CNPJ aqui:
documento = Documento.cria_documento("CPF OU CNPJ")

#Exemplo
# documento = Documento.cria_documento(12345678910)

print(documento)