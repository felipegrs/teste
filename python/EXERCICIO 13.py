import os
def limpa():
    os.system('cls')
limpa()

#13- Elaborar um programa Python para imprimir os números ímpares entre 1 e 100, inclusive.
for numero in range(1, 101):#cria um laço de repetiçao de 100 vezes
    if numero % 2 != 0:#verifica se o numero e impar
        print(numero,end="\n")#imprime o numero