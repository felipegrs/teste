import os
def limpa():
    os.system('cls')
limpa()
codigo = int(input("Informe o codigo do funcionario: "))
nome = input("Informe o nome do funcionario: ")
salario = float(input("Informe o salario do funcionario:R$ "))
ativo = True

print("\n")
print("Codigo: %d "%codigo)
print("Nome: %s "%nome)
print("Salario: %.2f "%salario)
print("Ativo: %r "%ativo)
