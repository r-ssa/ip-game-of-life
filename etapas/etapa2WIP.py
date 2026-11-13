import turtle

import random

opcao = -1

grid=[]

#Para teste coloca, 100, 100,10

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

        altura = yCells * dCell #Altura da janela
        largura = xCells * dCell #Largura da janela
        
#desenhar a grid
        
        screen=turtle.Screen()
        turtle.setup(largura + 30, altura + 30)#largura + 30, altura + 30
        turtle.setworldcoordinates(0, 0, largura, altura) #Origem no canto superior esquerdo
        turtle.title("Conway's Game of Life - PythonTurtle.Academy")
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0,0)        
            
        turtle.pencolor('gray')
        turtle.pensize(3)
                    
# linhas verticais
        for x in range(xCells + 1):
            turtle.up()
            turtle.goto(x*dCell, 0)
            turtle.down()
            turtle.goto(x*dCell, altura)

# linhas horizontais
        for y in range(yCells + 1):
            turtle.up()
            turtle.goto(0, y*dCell)
            turtle.down()
            turtle.goto(largura, y*dCell)            

        screen.update()
        turtle.mainloop()
 
        
#valores da grid           

        for i in range(largura):
            n=largura
            
            lin= random.sample(range(0,100),n)            
            print(lin)
        for j in range(altura):
            grid.append(lin)
            print(grid)
    
    elif opcao != 0:
        print("Opção inválida.")
if opcao==0:
    print('Fim')