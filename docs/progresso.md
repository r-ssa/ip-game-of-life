# Registo de progresso

Uma entrada por sessão de trabalho: o que fizemos, o que decidimos e porquê, e o que ficou por resolver.
Isto é a matéria-prima da secção "Trabalho desenvolvido" do relatório.

---

## 31 out 2026 – Etapa 1

**Feito**
- `etapas/etapa1.py`: menu com as opções 1 (abrir janela) e 0 (sair); pede `xCells`, `yCells` e `dCell` e volta a pedir se algum for 0 ou negativo; abre a janela com `setup`, `screensize` e `setworldcoordinates`.

**Decisões**
- `setworldcoordinates(0, 0, largura + 10, altura + 10)` em vez de `(0, 0, largura, altura)`.
  O `setworldcoordinates` estica as coordenadas sobre a janela menos 20 píxeis, ou seja, largura + 10.
  Com + 10, 1 unidade = 1 píxel e o ponto (0, 0) fica no canto inferior esquerdo da área de impressão, com 15 píxeis de margem.
  Com os valores "óbvios", o desenho sai cerca de 5% mais pequeno.

**Testado**
- Grelha de 20 x 15 células de 20 píxeis: janela de 430 x 330, escala 1 píxel por unidade.

**Por resolver**
- [ ] Abrir a janela uma segunda vez (escolher 1 outra vez no menu) dá erro `turtle.Terminator`. Faltam as duas linhas do enunciado antes de reabrir a janela (ver `requisitos.md`).
- [ ] Escrever uma letra no menu ou nos tamanhos dá erro `ValueError`. O enunciado pede dados validados.
