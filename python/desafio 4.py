import os
def limpa():
    os.system('cls')
limpa()

#DESAFIO 4
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
#e 5% para o sindicato, faça um programa que nos dê:
#• o salário bruto.
#• quanto pagou ao INSS.
#• quanto pagou ao sindicato.
#• o salário líquido. 

#pede o valor da hora trabalhada e de quantas horas foram trabalhas
valorHora = float(input("Informe o valor da hora trabalhada: R$"))
horasTrabalhadas = int(input("Informe quantas horas você trabalhou esse mes: "))

#faz o calculo do salario e dos impostos
impostoDeRenda = 0.11
inss = 0.08
sindicato = 0.05
salarioBruto = horasTrabalhadas*valorHora
impostoDeRenda = salarioBruto*impostoDeRenda
inss = salarioBruto*inss
sindicato = salarioBruto*sindicato
salarioLiquido = salarioBruto-impostoDeRenda-inss-sindicato

#mostra as informaçoes finais
print("Salario bruto: R$",salarioBruto)
print("Valor pago para o imposto de renda: R$",impostoDeRenda)
print("Valor pago para o INSS: R$",inss)
print("Valor pago para o sindicato: R$",sindicato)
print("Salario liquido: R$",salarioLiquido)
