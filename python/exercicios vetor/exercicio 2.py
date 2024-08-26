import os
def limpa():
    os.system('cls')#cria e define a funçao limpa
limpa()#limpa

num = []#cria uma nova lista

for i in range(10):#cria um laço de repetiçao
    elemento = float(input(f"Informe o {i+1}º elemento: "))#pede para informar os elementos da lista
    num.append(elemento)#armazena os elementos na lista
limpa()#limpa
print("Os valores do segundo vetor sao:\n")
for i in range(10):#cria um laço de repetiçao
    print(f"{i+1}º){num[i]*3}")#faz o calculo e escreve as informaçoes
    

