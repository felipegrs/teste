import os
def limpa():
    os.system('cls')
limpa()

#10- Elaborar um função para retornar o último elemento de uma lista.
def obter_ultimo_elemento(lista):
    if lista:#define o que retorna na lista
        return lista[-1]
    else: 
        return None
lista=[]#inicia uma lista vazia
i=1
while i<=5:#cria um laço de repetiçao de 5 vezes
 elem = int(input('Digite um elemento da lista:'))#pede um elemento da lista
 lista.append(elem)#armazena os elementos na lista
 i+=1
 print(lista)#imprime a lista
 ultimo_elemento = obter_ultimo_elemento(lista)#chama a funçao para obter o ultimo elemento da lista
 print('Último elemento da lista:', ultimo_elemento)#imprime o ultimo elemento da lista