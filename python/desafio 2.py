import os
def limpa():
    os.system('cls')
limpa()

#DESAFIO 2
#Uma concessionária pediu para que você crie uma solução para calcular o valor final
#de salário de seus colaboradores. Por momento, eles farão isso individualmente.
#ortanto, você não precisa se preocupar ainda em calcular vários salários de uma
#só vez. Vamos ao cálculo repassado por eles:
# O salário fixo é de R$1500,00;
#• Para cada carro vendido, o vendedor recebe R$250,00;
#• O vendedor recebe 5% do valor de todas as vendas da loja.
#Portanto, você precisará pedir ao usuário algumas informações:
#• Nome do vendedor
#• Quantidade de carros vendidos pelo vendedor
#• Total vendido pela concessionária
#Ao final, você deve informar um relatório contendo:
#• Nome do vendedor
#• Valor total de comissão
#• Salário total do vendedor

#define o valor do salario  das comissoes
salarioFixo = float(1500.00)
comissaoCarroVendido = float(250.00)
comissaoBonus = float(0.05)

#pede as informaçoes do trabalhador
nome = input("informe o nome do vendedor: ")
comissaoCarroTotal = float(input("Informe quantos carros o trabalhador vendeu nesse mes: "))
vendasTotalLoja = float(input("Informe quanto que a loja vendeu nesse mes: R$"))

#faz o calculo das comissoes
comissaoCarroTotal = comissaoCarroVendido*comissaoCarroTotal
comissaoBonus = vendasTotalLoja*comissaoBonus
comissaoTotal = comissaoCarroTotal+comissaoBonus
salarioFinal = salarioFixo+comissaoTotal
#mostra as informaçoes final
print("Nome: ", nome)
print("Comissao dos carros vendidos: R$", comissaoCarroTotal)
print("Comissao bonus: R$", comissaoBonus)
print("Comissao total: R$",comissaoTotal)
print("Salario inicial: R$",salarioFixo)
print("Salario final: R$",salarioFinal)