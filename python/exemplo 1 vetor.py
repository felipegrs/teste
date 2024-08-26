import os
def limpa():
    os.system('cls')
limpa()

#exemplo 1: construir uma lista e imprimir seus elementos
#python 2 para 'print' sem pular linha: print("x", end="";

n=10

#definir vetor/lista com: (10,11,12,13,....10+n-1)
vet = []#define um vetor vazio
for i in range(0, n, 1): #ou mais simples neste caso "for i in range(n)"
    vet.append(10+i); #anexe mais um elemento a lista
#imprime o vetor/lista de so vez(na mesma linha)
print("\nO vetor: ",end=""); #informe o que vira impresso a seguir(na mesma linha devido ao parametro end="")
print(vet)

#imprimir vet em linha unica na forma "(0, 0)(1, 1)...."
print("\n novamente o vetor impresso de 2 modos: ")#informar o que vira impresso a seguir(e "quebre" a linha)
i=0
for item in vet: #"item in vet" e um iterador, item começa em vet[0], depois vet[1] e assim or diante
    print('(%2d, %2d)'%(item, vet[i]), end="")
    i += 1
print() #quebre a linha