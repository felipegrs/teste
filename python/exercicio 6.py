import os
def limpa():
    os.system('cls')
limpa()
#Exercício 6 - Crie um programa que solicite a distância percorrida (em km) e o
#tempo de viagem (em horas). Calcule e mostre na tela a velocidade média.

#pede as informaçes da distancia e do tempo
distancia = float(input("Informe a distancia percorrida em km: "))
tempo = float(input("Informe o tempo gasto em horas: "))

#faz o calculo da velocidade media
velocidadeMedia = distancia/tempo

#exibe a velocidade media
print(f"A velocidade media foi de {velocidadeMedia}km/h")