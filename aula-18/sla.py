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

nomes: list[str] = ["Gustavo", "Letycia", "Julia"]

pesquisa = "Gustavo"
encontrado = False

for i in range(len(nomes)):
    if(nomes[i]== pesquisa):
        encontrado = True
        print("Encontrado: ", pesquisa)

pesquisa = "Julia"
posicao = -1

for i in range(len(nomes)):
    if (nomes[i] == pesquisa):
        posicao = i
print("Posição do nome pesquisado: ", posicao)

numeros: list[int] = [8, 3, 15, 6, 10]

maior = numeros[0]

for i in range(len(numeros)):
    if(numeros[i]>maior):
        maior=numeros[i]

        print("maior valor:", maior)