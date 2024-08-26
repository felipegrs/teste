import os
def limpa():
    os.system('cls')
limpa()

#pede um numero para fazer a tabuada
tabuada = int(input("Informe um numero para saber sua tabuada de 1 ate 10: "))
print(f"Tabuada do {tabuada}:\n")
for i in range(1,11):
    print(f"{tabuada} x {i} = {tabuada*i}")