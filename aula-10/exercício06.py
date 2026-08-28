alunos = int(input("Quantidade de alunos: "))
total = 0

for i in range(alunos):
    nota = float(input("Digite a nota do aluno: "))
    total += nota

print("Media da nota da turma é:", total/alunos)