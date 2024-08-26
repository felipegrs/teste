import os
def limpa():
    os.system('cls')
limpa()
#Exercício 8 Vamos começar a fazer alguns cálculos um pouquinho mais robustos
#nessa atividade. Vamos solicitar a compra e a revenda de um produto. Como uma
#loja por exemplo. Assim, você solicitará o valor de compra de um produto. Em
#seguida, fará o cálculo do valor de venda, acrescentando 35% de lucro no valor
#original. Lembremos que 35% representam 0,35 ou 35/100 de um valor ou uma
#quantidade.
 
#pede o valor da compra e informa a quantia em porcentagem de lucro
valorCompra = float(input("Informe o valor de compra do produto: R$"))
print("considerando um lucro de 35%")
lucro = 0.35
#faz o calculo do lucro
valorRevenda = (valorCompra*lucro)+valorCompra

#mostra o preço de revenda do produto
print("O valor de revenda do produto é de: R$", valorRevenda)