import os
def limpa():
    os.system('cls')
limpa()
# Lista para armazenar as informações das pessoas
pessoas = []

# Entrada de dados para 10 pessoas
for i in range(10):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ").upper()
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

# Impressão dos nomes das pessoas do sexo masculino com mais de 21 anos
print("\nPessoas do sexo masculino com mais de 21 anos:")
for pessoa in pessoas:
    if pessoa['sexo'] == 'M' and pessoa['idade'] > 21:
        print(pessoa['nome'])
