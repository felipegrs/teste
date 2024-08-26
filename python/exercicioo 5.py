import os
def limpa():
    os.system('cls')
limpa()
#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o
#preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço
#unitário), o desconto e o total a pagar (total a pagar = total - desconto)
# , sabendo-se que:
#- Se quantidade <= 5 o desconto será de 2% - Se quantidade > 5 e quantidade <=10 o
#desconto será de 3% - Se quantidade > 10 o desconto será de 5%

produto = str(input("Informe qual produto deseja comprar: "))
quantidade = int(input("Informe quantos produtos deseja comprar(tera desconto se comprar mais de 5 produtos): "))
preco = float("Informe o precço do produto: R$")

total = preco*quantidade
if quantidade>5 and quantidade<= 10:
    descontoPorcentagem = 0.02
elif quantidade>=10:
    descontoPorcentagem = 0.05
else:
    descontoPorcentagem = 0

desconto = total*descontoPorcentagem
totalPagar = total - desconto

print(f"Preço total: R${total}")
print(f"Total de desconto: R${desconto}")
print(f"Total a pagar: R${totalPagar}")
