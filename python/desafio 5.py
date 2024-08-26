import os 
def limpa():
    os.system('cls')
limpa()
#DESAFIO 5
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
#R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
#preço total

#pede o tamanho da area a ser pintada
area = float(input("Informe a area em metros² que vai ser pintada: "))

#faz o calculo de quantas latas sao necessarias
coberturaPorLitro = 3
litroPorLata = 18
coberturaPorLata = coberturaPorLitro*litroPorLata
precoLata = 80
quntidadeDeLatas =  1
while area>coberturaPorLata:
    quntidadeDeLatas+= 1
    coberturaPorLata += coberturaPorLitro*litroPorLata

#faz o calculo do valor total das latas
precoTotal = precoLata*quntidadeDeLatas

#mostra as informaçoes finais
print(f"Area a ser pintada: {area}m²")
print("Quantidade de latas necessaria: ", quntidadeDeLatas)
print("Preço total pago pelas latas: R$", precoTotal)