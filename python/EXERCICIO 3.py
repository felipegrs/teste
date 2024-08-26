import os
def limpa():
    os.system("cls")
limpa()

#3- Elaborar um programa Python para ler uma temperatura em Fahrenheint e converter
#para Celsius.
#pede  temperatura em fahrenheit
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
#faz o calculo da conversao
celsius = (fahrenheit - 32) * 5/9
#exibe o resultados
print('Temperatura em Celsius é:', celsius)