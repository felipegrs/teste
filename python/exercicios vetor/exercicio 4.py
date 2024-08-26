import os
def limpa():
    os.system('cls')#cria e define a funçao limpa
limpa()#limpa

vetor1 = []#cria 3 novas listas
vetor2 = []
vetor3 = []

for i in range(0,10):#cria um laço de repetiçao
    numeros1 = float(input(f"Informe o {i+1}º numero do vetor1: "))#pede os numeros da primeira lista
    vetor1.append(numeros1)#armazena os numeros da primeira lista
limpa()#limpa

for i in range(0,10):#cria um laço de repetiçao
    numeros2 = float(input(f"Informe o {i+1}º numero do vetor2: "))#pede os numeros da segunda lista
    vetor2.append(numeros2)#armazena os numeros da segunda lista
limpa()#limpa

for a in range(0,10):#cria um laço de repetiçao
    vetor3.append(vetor1[a]+vetor2[a])#faz o calculo e armazena na terceira lista a soma das duas listas
    print(vetor3[a])#escreve os numeros da terceira lista
