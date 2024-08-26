#Exercício 2 - Crie um programa que solicite o preço original de um produto e a
#porcentagem de desconto. Calcule e exiba o valor do desconto e o preço final com
#desconto. 
import os
def limpa():
    os.system('cls')
limpa()
#pede o preço e a porcentagem de desconto
precoInicial = float(input("Informe o valor do produto: R$"))
descontoPorcentagem = float(input("Informe a porcentagem de desconto: "))
#calcula a quantia de desconto
desconto = (descontoPorcentagem/100)*precoInicial
#calcula o preço final
precoFinal = precoInicial - desconto

#exibe o preço final com desconto
print("O preço final do produto é: R$", precoFinal)