# Requisitos

Retirado do enunciado (Tema nº 17 – Game of Life, e "Projeto – enunciado geral").

## Etapa 1 – até à 1ª aula de acompanhamento

- [x] Menu na shell para navegar entre as funcionalidades, com opção para sair
- [x] Pedir a dimensão da grelha em nº de células: horizontal (`xCells`) e vertical (`yCells`)
- [x] Pedir o tamanho da célula em píxeis (`dCell`), quadrada
- [x] Janela `turtle` com área de impressão `screensize`: altura = `yCells * dCell`, largura = `xCells * dCell`
- [x] Janela ligeiramente maior com `setup`: altura + 30, largura + 30
- [x] Origem do sistema de coordenadas no canto inferior esquerdo (`setworldcoordinates`)

## Etapa 2 – até à 2ª aula de acompanhamento

- [ ] Variável estruturada que representa a grelha, com um elemento por célula
- [ ] Pedir a probabilidade inicial de uma célula estar viva
- [ ] Preencher a grelha com essa probabilidade: `True` = viva, `False` = morta
- [ ] Desenhar o estado inicial da grelha

## Até à entrega final

- [ ] Pedir o número de iterações da simulação
- [ ] Realizar o ciclo de simulação
- [ ] Depois da simulação, permitir gravar os parâmetros e o mapa inicial
- [ ] Antes da simulação, permitir carregar um ficheiro com os parâmetros e o mapa inicial, em alternativa a introduzir novos
- [ ] Pelo menos 2 funções no programa
- [ ] Créditos extra: mostrar os mapas das iterações anteriores em níveis de cinzento

## Regras do jogo (Conway)

Cada célula olha para as 8 vizinhas e conta quantas estão vivas.

| Célula | Vizinhas vivas | Resultado |
|---|---|---|
| viva | menos de 2 | morre |
| viva | 2 ou 3 | continua viva |
| viva | mais de 3 | morre |
| morta | exatamente 3 | nasce |

Todas as células mudam ao mesmo tempo: a nova geração calcula-se a partir da antiga, sem a alterar pelo caminho.

## Regras gerais do projeto

- [ ] Boa interação: menus claros, mensagens claras sobre o que se pede e o que se mostra
- [ ] Dados do teclado validados, só aceitar valores realistas
- [ ] Somas, contagens, máximos e mínimos feitos por nós, sem funções prontas (`sum`, `max`, `min`, `count`...)
- [ ] Usar estruturas de decisão e repetição do Python
- [ ] Interação com o utilizador em modo texto

## Métodos sugeridos no enunciado

- `turtle`: `setup()`, `screensize()`, `setworldcoordinates()`, `speed()`, `hideturtle()`, `goto()`, `penup()`, `pendown()`, `begin_fill()`, `end_fill()`, `clear()`, `done()`, `tracer(0,0)`, `update()`, e os de desenho (`left`, `right`, `forward`)
- `random`: `randint()` ou outro, para o estado inicial aleatório
- `time`: `sleep()`, para uma pausa entre iterações

## Notas do enunciado sobre o `turtle`

- Com a janela aberta, a shell fica suspensa.
- No fim dos gráficos usar `turtle.done()` para a janela ficar aberta até o utilizador a fechar.
- A shell só volta depois de fechar a janela.
- Antes de reabrir a janela:
  ```python
  turtle.Turtle._screen = None
  turtle.TurtleScreen._RUNNING = True
  ```

## O que se entrega (até 3 jan 2027, 23:59)

- [ ] 1º componente: estrutura de dados e algoritmo (linguagem natural ou fluxograma), atualizados com a versão final
- [ ] 2º componente: programa em Python e ficheiro com dados para uma demonstração
- [ ] 3º componente: relatório (ver `relatorio.md`)
- [ ] Depois: apresentação e discussão oral
