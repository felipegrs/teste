import os
def limpa():
    os.system('cls')
limpa()

#4- Elaborar uma função para calcular o maior de três números.
#define o calculo para o maior numero
#define o calculo do maior numero
def maior3(a, b, c):
 if a >= b and a >= c:
    return a
 elif b >= c:
    return b
 else: return c
#pede  valor de cada numero
n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
resultado = maior3(n1,n2,n3)
#exibe o resultado
print(resultado)