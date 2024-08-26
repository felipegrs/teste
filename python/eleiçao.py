import os
def limpa():
    os.system('cls')
limpa()

#define a quantidade de votos de cada um
candidato1 = 0
candidato2 = 0
candidato3 = 0
branco = 0
nulo = 0
i = 1

votos = int(input("Informe quantos votos foram no total: "))
print("Os votos são: 1) candidato1, 2) candidato2, 3) candidato3, 4) branco, 5)nulo")

for i in range(votos):
    votos2 = int(input(f"Informe qual foi o {i+1}º voto: "))
    if votos2 == 1:
        candidato1 += 1
    elif votos2 == 2:
        candidato2 += 1
    elif votos2 == 3:
        candidato3 += 1
    elif votos2 == 4:
        branco += 1
    else:
        nulo += 1

print(f"Votos para o candidato 1: {candidato1}")
print(f"Votos para o candidato 2: {candidato2}")
print(f"Votos para o candidato 3: {candidato3}")
print(f"Votos em branco: {branco}")
print(f"Votos anulados: {nulo}")