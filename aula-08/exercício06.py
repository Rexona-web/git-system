distancia_metros = float(input("Insira uma distância em metros: "))

opcao_conversao = int(input("\n1-Centímetros \n2-Quilometros \n3-milímetros \nEscolha uma opção de conversão:"))

match opcao_conversao:
    case 1:
        calculo_centimetros = distancia_metros * 100
        print("Distância calculada: ", calculo_centimetros)
    case 2:
        calculo_km = distancia_metros / 1000
        print("Distância calculada: ", calculo_km)
    case 3:
        calculo_ml = distancia_metros * 1000
        print("Distância calculada: ", calculo_ml)
    case _:
        print("Conversão inválida")

