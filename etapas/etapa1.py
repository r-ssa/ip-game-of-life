import turtle

opcao = -1

#MENU

while opcao != 0:
    print("1 - Abrir janela de simulação")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        xCells = 0
        yCells = 0
        dCell = 0
        while xCells <= 0 or yCells <= 0 or dCell <= 0:
            xCells = int(input("Indique a largura da grelha (nº de células): "))
            yCells = int(input("Indique a altura da grelha (nº de células): "))
            dCell = int(input("Indique o tamanho da célula (em píxeis): "))

        altura = yCells * dCell
        largura = xCells * dCell

        turtle.setup(largura + 30, altura + 30)
        turtle.screensize(largura, altura)
        turtle.setworldcoordinates(0, 0, largura + 10, altura + 10)

        turtle.done()

    elif opcao != 0:
        print("Opção inválida.")