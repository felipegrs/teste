import os
def limpa():
    os.system('cls')
limpa()

#9- Elaborar um função em Python para ordenar uma lista utilizando a ordenação por
#inserção(Insertion Sort).
def insertion_sort(lista):
    
    for i in range(1, len(lista)):#percorre cada elemento da lista
        chave = lista[i]#cria uma nova lista
        j = i - 1
        while j >= 0 and chave < lista[j]:#cria um laço que se repete ate acabar os elementos da lista
            lista[j + 1] = lista[j]
            j -= 1 
        lista[j + 1] = chave
lista=[]#inicia uma lista vazia
i=1
while i<=10:#cria im laço que se repete 10 vezes
 elem = int(input('Digite um elemento da lista:'))#pede um numero para ser adiciconado na lista
 lista.append(elem)#armazena cada numero na lista
 i+=1
 print(lista)#imprime a lista
 insertion_sort(lista)#chama a funçao para organizar a lista
 print(lista)#Imprimie a lista organizada
