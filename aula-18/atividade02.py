produtos: list[str] = ["Produto1", "Produto2", "Produto3", "Produto4", "Produto5"]

for produto in range(len(produtos)):
    print(f"{produto} - {produtos[produto]}")
print("Total de produtos:", (produtos))