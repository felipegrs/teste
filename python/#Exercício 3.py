#Exercício 3- Elabore um programa que solicite o comprimento do lado de um
#quadrado e, em seguida, exiba a área desse quadrado.

import os
def limpa():
    os.system('cls')
limpa()
#pede a medida do quadrado
comprimento = float(input("Informe o comprimento do lado do quadrado: "))

#calcula da area do quadrado
area = comprimento*comprimento

#exibe a area do quadrado
print(f"a area do quadrado é:  {area}cm²")