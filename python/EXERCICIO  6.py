import os
def limpa():
    os.system('cls')
limpa()

#6- Elaborar uma função para converter de quilômetros para metros.
#define o calculo da conversao
def converter_quilometros_para_metros(quilometros):
 metros = quilometros * 1000
 return metros
#pede os quilometros para a conversao
try:
    quilometros = float(input('Digite a distância em quilômetros: '))
    metros = converter_quilometros_para_metros(quilometros)
    #mostra os resultados
    print('metros:', metros)
#exibe erro caso o valor seja invalido
except ValueError:
    print('Entrada inválida!')