import os
def limpa():
    os.system('cls')
limpa()
#DESAFIO 1
#Você está desenvolvendo uma solução para uma loja de roupas. Num primeiro
#momento, eles só querem calcular o valor final de venda de um item a partir de seu
#custo, incidindo comissão para o representante e impostos do governo. Para isso, a
#gerente da loja explicou que para realizar esses cálculos você que o:
#• Usuário informe o valor de custo do item direto da fábrica (VLC);
#• Usuário informe a porcentagem de comissão que o representante receberá a partir do
#custo (CR);
#• Usuário informe a porcentagem de margem de lucro desejada a partir do valor
#acumulado entre custo e comissão (ML);
#• Usuário informe a porcentagem de impostos governamentais para o valor final
#acumulado de todos os itens anteriores (GOV).
#Assim, o usuário visualizará em sua tela o valor final do produto com todos esses itens
#acumulados e também discriminadamente, ou seja, item a item dos valores obtidos.
#Abaixo, deixamos a fórmula de cálculos a ser utilizada:
#VALOR COMISSÃO (VC) = VLC * CR
#VALOR MARGEM DE LUCRO (VM) = VLC * CR * ML
#VALOR DE IMPOSTOS GOVERNAMENTAIS (VG) = VLC * CR * ML * GOV
#VALOR FINAL (VF) = VC + VM + VG
#* Preste atenção nas siglas utilizadas

#pede o valor de fabrica do item, comissa do reperesentante, margem de lucro e impostos 
custoFabrica = float(input("Informe o valor do produto direto de fabrica: R$"))
comissaoRepresentante = float(input("Informe a quantia em porcentagem de comissao ganha pelo representante: "))
margemLucro = float(input("Informe o lucro desejado em porcentagem: "))
impostos = float(input("Informe a quantia em porcentagem dos impostos: "))

#passa o valor em porcentagem para decimal
comissaoRepresentante = comissaoRepresentante/100
margemLucro = margemLucro/100
impostos = impostos/100
#faz o calculo do valor final do item
valorComissao = custoFabrica*comissaoRepresentante
valorLucro = (custoFabrica+valorComissao)*margemLucro
valorImpostos = (custoFabrica+valorLucro)*impostos
valorFinal = custoFabrica+valorComissao+valorLucro+valorImpostos

#mostra as informaçoes final
print("\nCusto do produto: R$", custoFabrica)
print("Valor da comissao do representante: R$", valorComissao)
print("Valor do lucro recebido: R$", valorLucro)
print("Valor dos impostos: R$", valorImpostos)
print("valor final do produto: R$", valorFinal)