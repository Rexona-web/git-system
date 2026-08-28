print("Dias da semana\n 1-Domingo\n 2-Segunda\n 3-Terça\n 4-Quarta\n 5-Quinta\n 6-Sexta\n 7-Sabado")

opcao = int(input("Selecione um dia da semana:"))

match opcao:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sabado")
    case _:
        print("Dia invalido")