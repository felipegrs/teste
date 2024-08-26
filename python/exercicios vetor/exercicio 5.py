import os
def limpa():
    os.system('cls')#cria e define a funçao limpa
limpa()#limpa

nome = []
salario = []
salarioFinal = []#cria 3 novas listas

for i in range(5):#cria um laço de repetiçao
    funcionario = str(input(f"Informe o nome do trabalhador {i+1}: "))#pede para informar o nome do funcionario
    nome.append(funcionario)#armazena o nome do funcionario na lista
limpa()#limpa

for i in range(5):#cria um laço de repetiçao
    salarioInicial = float(input(f"Informe o salario inicial do {nome[i]}: "))#pede para informar o salario do funcionario
    salario.append(salarioInicial)#armazena o salario do funcionario na lista
limpa()#limpa

for i in range(5):#cria um laço de repetiçao
    aumento = salario[i]*0.8#faz o calculo do aumento
    somaSalario = salario[i]+aumento#faz o calculo do salario final
    salarioFinal.append(somaSalario)#armazena o salario final na lista

print("Todos os funcionarios receberam 8% de aumento!")
print("Salario atualizado dos funcionarios:\n")
for i in range(5):#cria um laço de repetiçao
    print(f"Nome:{nome[i]}  Salario:{salarioFinal[i]}")#informe o noome 
