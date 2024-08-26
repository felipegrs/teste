import os
def limpa():
    os.system('cls')
limpa()
#Exercício 7 - Agora vamos criar um programa que simula uma venda de uma loja
#para um cliente final. Então, precisamos de duas informações: valor final da compra
#e a quantidade de parcelas
#pede o valor inicial e a quantia de parcelas e informa que compras acima de 6 parcelas tera juros
valorInicial = float(input("Informe o valor do produto: R$"))
print("Para compras com parcelas acima de 6 sera cobrado um juros de 8%")
parcelas = int(input("Informe a quantia de parcelas: "))
#define um valor para o valor final e juros
valorFinal = valorInicial
juros = 0.08
#faz o calculo do valor final e o valor de cada parcela
if parcelas>=6:
    valorFinal = (valorInicial*juros)+valorInicial

valorParcelas = valorFinal/parcelas
#mostra as informçoes do valor final, a quantia de parcelas e o valor de cada parcela
print("\nO valor final do produto é: R$", valorFinal)
print("A quantia de parcelas foi: ", parcelas)
print("O valor de cada parcela foi de: R$", valorParcelas)