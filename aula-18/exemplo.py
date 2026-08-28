alunos: list[str] = ["ana", "bruno", "Carlos"]

for i in range(len(alunos)):
    print(alunos[i])

frutas: list[str] = ["Maçã", "Banana", "Laranja"]

for i in range(len(frutas)):
    print("Índice: ", i)
    print("Fruta: ", frutas[i])

produtos: list[str] = ["Arroz", "Feijão", "Frango"]

for i in range(len(produtos)):
    print(i + 1, "-", produtos[i])

nomes: list[str] = []

for i in range(5):
    nome = input("Digite um nome: ")

    nomes.append(nome)

print(nomes)

nomes: list[str] = []

for i in range(5):

    nome = input("Digite")

alunos: list[str] = []

for i in range(3):
    nome = input("Digite o nome do aluno")
    print(i+1, "-", nome)

print("======ALUNOS======")

for i in range(len(alunos)):
    print(i+1,"-", alunos(i))

idades: list[int] = [15, 18, 21, 12, 30]

maioresidade = 0
menoresidade = 0

for i in range(len(idades)):
    if(idades[i] >=18):
        maioresidade+=1

else:
    (idades[i] <=18)
    menoresidade+=1


print("Maiores de idade: ", maioresidade)
print("Menores de idade: ", menoresidade)