import os
def limpa():
    os.system('cls')
limpa()

#8- Elaborar uma função para dobrar os elementos de uma lista.
def dobrar_lista(lista):
    nova_lista = []#cria uma nova lista vazia
    for elemento in lista:#percorre cada elemento da lista
        novo_elemento = elemento * 2#faz o calculo x2 para dobrar os elementos da lista
        nova_lista.append(novo_elemento)#guarda os elementos na nova lista
    return nova_lista#retorna a nova lista
lista=[]#inicia uma lista vazia
i=1
while i<=10:#cria um laço de repetiçao de 10 vezes
    elem = int(input('Digite um elemento da lista:'))#pede os elementos da lista
    lista.append(elem)#armazena os elementos na lista
    i+=1#i+=1
print(lista)#mostra a lista
nova_lista = dobrar_lista(lista)#chama a funçao para dobrar os elementos da lista
print(nova_lista)#imprime a nova lista