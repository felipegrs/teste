import os
def limpa():
    os.system('cls')
limpa()

qtd = 0
soma = 0
media = 0
valor = float(input("Informe um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1 
    #entrada de valores
    valor = float(input("Informe um valor: "))

#caso digite um valor negativo o laço encerra
media = soma/qtd
print("\nTotal da Soma: ",soma)
print("Quantidade de valores digitados: ",qtd)
print("Media dos valores: ",media)
