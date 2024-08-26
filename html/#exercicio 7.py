import os
def limpa():
    os.system('cls')
limpa()
#Exercício 7 - Agora vamos criar um programa que simula uma venda de uma loja
#para um cliente final. Então, precisamos de duas informações: valor final da compra
#e a quantidade de parcelas
#pede o valor inicial e a quantia de parcelas
valorInicial = float(input("Informe o valor do produto: R$"))
parcelas = int(input("Informe a quantia de parcelas: "))
print("Para compras com parcelas acima de 6 sera cobrado um juros de 8%")
#define um valor para o valor final e juros
valorFinal = valorInicial
juros = 0,08
if parcelas>=6:
    valorFinal = (valorInicial*juros)+valorInicial

valorParcelas = valorFinal/parcelas

print("O valor final do produto é: R$")
print("A quantia de parcelas foi: ")
print("O valor de cada parcela foi de: R$")