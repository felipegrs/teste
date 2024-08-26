import os
def limpa():
    os.system('cls')
limpa()
notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

#calcular media
mediaFinal = (notaA + notaB)/2

#verificaçao
if mediaFinal >= 7.0:
    print("A media: %.1f - Aprovado"% mediaFinal)
else:
    print("A media: %.1f - Reprovado"% mediaFinal)
limpa()

idade = int(input("Informe a idade da pessoa: "))

if idade >= 18:
    print("Já é um Adulto")
elif idade >= 16:
    print("Infanto Juvenil")
else:
    print("Menor de Idade")
