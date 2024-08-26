import os
def limpa():
    os.system('cls')
limpa()
#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
#estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
#quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média escrever a
#mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quantidadeAtual = int(input("Informe a quantidade atual em estoque: "))
quantidadeMaxima = int(input("Informe a aquantidade maxima em estoque: "))
quantidadeMinima = int(input("Informe a quantidade minima em estoque: "))

quantidadeMedia = (quantidadeMaxima+quantidadeMinima)/2

print(f"\nQuantidade media necessaria em estoque: {quantidadeMedia}")
if quantidadeAtual<quantidadeMedia:
    print("Precisa comprar mais")
else:
    print("Nao precisa comprar mais")