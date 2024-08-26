import os
def limpa():
    os.system('cls')
limpa()

# Lista para armazenar as médias dos alunos
medias_alunos = []

# Coleta de dados para 20 alunos
for i in range(20):
    print(f"\nAluno {i+1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    
    # Calcula a média do aluno
    media_aluno = sum(notas) / len(notas)
    medias_alunos.append(media_aluno)
    print(f"Média do aluno {i+1}: {media_aluno:.2f}")

# Calcula a média da turma
media_turma = sum(medias_alunos) / len(medias_alunos)

# Conta o número de alunos aprovados
aprovados = sum(1 for media in medias_alunos if media >= 7.0)

# Exibe os resultados
print("\nResultados:")
print(f"Média da turma: {media_turma:.2f}")
print(f"Número de alunos aprovados: {aprovados}")
