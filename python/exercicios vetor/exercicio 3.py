import os
def limpa():
    os.system('cls')#cria e define a funçao limpa
limpa()#limpa

num = []#cria uma nova lista

for i in range(8):#cria um laço de repetiçao
    numeros = float(input("Informe 8 numeros: "))#pede os numeros da lista
    num.append(numeros)#armazena os numeros na lista
limpa()#limpa

print("São multiplos de 3 os numeros:\n")

for i in range(8):#cria um laço de repetiçao
    if num[i]%3 == 0:#verifica se os numeros sao multiplos de 3
        print(num[i])#escre os numeros multiplos de 3
