import os
def limpa():
    os.system('cls')
limpa()
idade = int(input("Informe a idade da pessoa: "))

if idade >= 18:
    print("maior idade")
else:
    print("menor idade")
limpa()

A = input("informe um valor para a variável A: ")
B = input("informe um valor para a variavel B: ")

if A>B :
    aux=A
    A=B
    B=aux

print("o valor da variavel A agora é: ", A)
print("o valor da variavel B agora é: ", B)
