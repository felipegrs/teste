import os
def limpa():
    os.system('cls')
limpa()

#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
#Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$
#1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário
#total.

salarioFixo = float(input("Informe o salario fixo do vendedor: R$"))
vendasTotais = float(input("Informe qual foi o valor das vendas totais: R$"))
print("O vendedor recebera uma comissao de 3% do valor das vendas ate 1.500R$ e 5% do valor que ultrapassar 1.500R$")

if vendasTotais<=1.500:
    comissao = vendasTotais*0.03
else:
    comissao = 1.500*0.03+(vendasTotais-1.500)*0.05
salarioFinal = salarioFixo+comissao
print(f"O valor da comissao foi de R${comissao}")
print(f"O salario final do vendedor foi de R${salarioFinal}")
