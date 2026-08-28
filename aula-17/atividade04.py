compras: list[str] = []

produto1 = input("Digite o primeiro produto: ")
produto2 = input("Digite o segundo produto: ")
produto3 = input("Digite o terceiro produto: ")

compras.append(produto1)
compras.append(produto2)
compras.append(produto3)



print("====LISTA DE COMPRAS====")

print("produtos: ", compras)
print("Quantidade de produtos: ", len(compras))
print("Primeiro Produto: ", compras[0])
print("Último produto: ", compras[2])