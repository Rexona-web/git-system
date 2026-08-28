alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
print(alunos[3])

notas = [7, 8, 14, 15, 16]
print(notas[3])

nomes: list[str] = ["Ana", "Bruno", "Carlos"]

notas: list[int] = [7, 8, 15]

notas[1] = 17
print(notas)

frutas: list[str] = ["Maçã", "Banana", "Laranja"]
print(len(frutas))

nomes: list[str] = ["Ana", "Bruno"]
nomes.append("Carlos")
print(nomes)

nomes: list[str] = ["Bruno", "Carlos"]
nomes.insert(0,"Ana")
print(nomes)

nomes: list[str] = ["Ana", "Bruno", "Carlos"]

nomes.pop()
print(nomes)

nomes: list[str] = ["Ana", "Bruno", "Carlos"]

nomes.remove("Ana")
print(nomes)