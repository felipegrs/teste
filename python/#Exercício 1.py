#Exercício 1 - Desenvolva um programa que receba o salário de um funcionário e a
#porcentagem de aumento. O programa deve calcular e exibir o novo salário. 

import os
def limpa():
    os.system('cls')
limpa()
#pede o salario e a porcentagem de aumento
salarioInicial = float(input("Informe o valor do salario inicial: R$"))
aumentoPorcentagem = float(input("Informe a porcetagem de desconto: "))

#passa a porcentagem para o valor decimal para fazer o calculo
aumentoPorcentagem = aumentoPorcentagem/100
#faz o calculo do aumento
aumento = salarioInicial*aumentoPorcentagem
#faz o calculo do salario+aumento para saber o salario final
salarioFinal = salarioInicial+aumento
#exibe o salario final
print("o salario final com o aumento e de: R$",salarioFinal)