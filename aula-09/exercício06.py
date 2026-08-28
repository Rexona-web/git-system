calculo_notas = True
media = 0
contador = 0

while calculo_notas:
    print("1 - para adicionar notas")
    print("2 - sair")
    opcao = int(input("Digite uma opção entre 1 e 2: "))
    if opcao == 1:
        nota = float(input("Digite a nota do aluno: "))
        media = media + nota
        contador = contador + 1

    elif opcao == 2:
        print("Saindo!")
        print("Total de alunos:", contador)
        print("Media da turma:", media/contador)
        calculo_notas = False
    else:
        print("Opção inválida!")