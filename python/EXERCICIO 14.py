import os
def limpa():
    os.system('cls')
limpa()

#14- Elaborar um programa Python que leia uma 
#lista com 10 inteiros e imprima a soma emédia dos números
numeros = []#cria uma lista vazia
for i in range(10):#faz um loop 10 vezes
    try:
        numero = int(input("Digite um número inteiro: "))#pede para o usuario digitar um numero
        numeros.append(numero)#armazena o numero na lista
    except ValueError:
        print("Entrada inválida!!!")#imprime uma mensagem de erro caso a entrada seja invalida
soma = sum(numeros)#calcula a soma dos sumeros
media = soma / len(numeros)#calcula a media dos numeros
print("Soma:", soma)#imprime  a soma dos numeros
print("Média:", media)#imprime a media dos numeros