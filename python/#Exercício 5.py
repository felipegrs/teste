#Exercício 5 - Faça um programa que peça a base e a altura de um triângulo e, em
#seguida, exiba a área desse triângulo. 
import os
def limpa():
    os.system('cls')
limpa()

#pede as medidas do triangulo
altura = float(input("informe a altura do triangulo em centimetros: "))
base = float(input("informe a base do triangulo em centimetros: "))

#faz o calculo da area do triangulo
area = (base*altura)/2

#exibe a area do triangulo
print(f"A area do triangulo é: {area}cm²")