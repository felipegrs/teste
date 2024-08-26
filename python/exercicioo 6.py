import os
def limpa():
    os.system('cls')
limpa()
#Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou
#não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: - Ter no
#mínimo 65 anos de idade. - Ter trabalhado no mínimo 30 anos. - Ter no mínimo 60 anos
#e ter trabalhado no mínimo 25 anos. Com base nas informações acima, faça um
#algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano
#de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho
#do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.
codigo = int(input("Informe o seu codigo de funionario: "))
anoNacimento = int(input("Infome em que ano você nasceu: "))
anoEmpresa = int(input("Informe em que ano você entrou na empresa: "))
aposentadoria = 0
idade = 2024 - anoNacimento
tempoEmpresa = 2024 - anoEmpresa

if idade >= 65:
    aposentadoria = 1
elif idade >= 60 and tempoEmpresa >=25:
    aposentadoria = 1
elif tempoEmpresa >= 30:
    aposentadoria = 1
else:
    aposentadoria = 0
limpa()
print(f"Codigo do funcionario: {codigo}")
print(f"Idade do funcionario: {idade} anos")
print(f"Tempo na empresa: {tempoEmpresa} anos")
if aposentadoria == 1:
    print("Precisa de aposentadoria")
else:
    print("Nao precisa de aposentadoria")
