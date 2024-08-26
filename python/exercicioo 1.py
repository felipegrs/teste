import os
def limpa():
    os.system('cls')
limpa()
#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo
#por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor
#das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por
#ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por
#carro vendido. Calcule e escreva o salário final do vendedor.

salarioFixo = float(input("Informe o salario fixo do vendedor: R$"))
comissaoPorCarro = float(input("Informe quanto o vendedor ganha por cada carro vendido: R$"))
carrosVendidos = int(input("Informe quantos carros foram vendidos: "))
vendasTotal = float(input("Informe qual foi o valor total que o vendedor vendeu(o vendedor ira ganhar 5% do valor das vendas): R$"))
comissao = 0.05

carrosVendidosTotal = comissaoPorCarro*carrosVendidos
comissaoVendas = vendasTotal*comissao
salarioFinal = salarioFixo+comissaoVendas+carrosVendidosTotal
limpa()
print(f"Comissao pelos carros vendidos: R${carrosVendidosTotal}")
print(f"Comissao pelas vendas totais: R${comissaoVendas}")
print(f"O salario final do vendedor é de: R${salarioFinal}")
