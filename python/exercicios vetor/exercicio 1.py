import os
def limpa():
    os.system('cls')#cria e define a funçao limpa
limpa()#limpa o codigo, pq fica bonito

num = []#cria uma nova lista

for i in range(15):#cria um laço de repetiçao
    numero = int(input(f"{i + 1} de 15)Informe um numero inteiro: "))#pede pra informar os numeros da lista
    num.append(numero)#armazena os numeros na lista
limpa()#limpa

print("Informações:\n")#escreve "informaçoes"
for i in range(15):#cria um laço de repetiçao
    if num[i]%2 == 0:#verifica se o numero e par
        print(f"{i+1}) O numero {num[i]} é par")#se o numero for par informa para o usuario
    else:
        print(f"{i+1}) O numero {num[i]} é impar")#caso o numero seja impar iinforma para o usuario