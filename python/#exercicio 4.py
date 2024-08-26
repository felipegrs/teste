#Exercício 4- Crie um programa que peça o raio de um círculo e, em seguida, exiba
#a área desse círculo.

import os
def limpa():
    os.system('cls')
limpa()
#pede a medida do circulo
raio = float(input("Informe o raio do circulo em centimetros: "))

print("considerando π(pi) = 3,14")
pi = float (3.14)

#calculo da area do circulo
area = pi*(raio*raio)

#exibe a area do circulo
print(f"A area do circulo é: {area}cm²")