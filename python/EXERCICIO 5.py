import os
def limpa():
    os.system('cls')
limpa()

#5- Elaborar uma função recursiva em Python para calcular o MDC de dois números.
#define o calculo do mdc
def mdc(a, b):
 if b == 0:
    return a
 else:
    return mdc(b, a % b)
#pede os numeros
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
resultado = mdc(num1, num2)
#imprime os resultados
print('MDC:', resultado)