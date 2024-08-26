import os
def limpa():
    os.system('cls')
limpa()
#DESAFIO 3
#Você é responsável das soluções tecnológicas para o setor de Atendimento ao
#Cliente de sua empresa. Então, seu chefe comentou que, para ele, é mais fácil e
#perceptível saber quantos segundos um atendente dedicou dando suporte para um
#cliente. Para solucionar esse problema, ele quer que você crie uma solução que seja
#capaz de converter horas, minutos e segundos apenas para segundos. 

#pede as horas, minutos e segundos
horas = int(input("Informe quantas horas foram dedicadas ao atendimento ao cliente: "))
minutos = int(input("Informe quantos minutos foram dedicados ao atendimento ao cliente: "))
segundos = int(input("Informe quantos segundos foram dedicados ao atendimento ao cliente: "))

#faz o calculo de horas e minutos para segundos
minutos = (horas*60)+minutos
segundos = (minutos*60)+segundos

#mostra o total de segundos 
print(f"O total de segundos dedicados ao atendimento ao cliente foi de: {segundos}s")