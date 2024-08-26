import os
def limpa():
    os.system('cls')
limpa()

#7- Elaborar uma função em Python para computar o maior e o menor elemento de uma
#lista.
#define listas para armazenar o menor e menor numero
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    #define o calculo do maior e menor numero
    for elemento in lista:
        if elemento > maior:#se o elemento for maior que o elemento armazenado na lista ele ocupa a posiçao como maior
            maior = elemento
        elif elemento < menor:#se o elemento for menor que o elemneto armazenado na lista ele ocupa a posiçao como menor
            menor = elemento
    return maior, menor
lista=[]
i=1
while i<=10:#cria um laço de repetiçao para repetir 10 vezes
    elem = int(input('Digite um elemento da lista:'))#pede um numero
    lista.append(elem)#armazena na lista
    i+=1
print(lista)#mostra a lista
maior, menor = maior_menor(lista)#chama a funçao para descobrir o maior e menor numero
print('Maior:', maior)#mostra o maior numero
print('Menor:', menor)#mostra o menor numero