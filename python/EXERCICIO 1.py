import os
def limpa():
    os.system('cls')
limpa()
#Elaborar um programa Python para calcular a soma de 1 até 50.
#da um valor inicial para variavel soma
soma = 0
#cria um laço de repetiçao para fazer a contagem
for i in range(1, 51):
    soma += i
#exibe o resultado da soma
    print("Soma:", soma)
