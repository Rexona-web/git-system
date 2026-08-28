print("1-Cadastrar")
print("2-Constulta")
print("3-sair")


opcao = int(input("Selecione uma opção: "))

match opcao:
    case 1:
        print("Cadastro")
    case 2:
        print("Consulta")
    case 3:
        print("Sair")
print("Programa encerrado")