import os
def limpa():
    os.system('cls')
limpa()
codigo = 10
salario = 1500.00
nome = 'jose'
situação = True

tipo = type (codigo)
tipo2 = type(nome)
tipo3 = type (salario)

print("codigo:",codigo)
print(tipo)
print("nome:",nome)
print(tipo2)
print("salario:R$",salario)
print(tipo3)

limpa()

print("codigo:", codigo, "\nnome:", nome, "\no salario atual é de:R$", salario)
print("\n")
print("codigo:"+ str (codigo)+ "\nnome:"+nome+ "\no salario atual é de:R$ "+str(salario))
limpa()

codigo2 = 105
nome2 = 'Jose Santana'
salario2 = 1650.00
ativo = True

print("Codigo: %d "% codigo2)
print("Nome: %s "% nome2)
print("Salario:R$ %.2f "% salario2)
print("Ativo: %r "% ativo)