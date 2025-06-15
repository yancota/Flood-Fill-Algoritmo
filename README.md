# Algoritmo Flood-Fill

### Alunos
- Lucas Henrique Chaves de Barros
- Yan Mariz Magalhães Cota

## Descrição

Este projeto implementa o algoritmo Flood-Fill para identificar e preencher todas as regiões conectadas em uma matriz (grid) 2D. O algoritmo colore regiões distintas de zeros (`0`) com cores diferentes, permitindo visualizar claramente as áreas conectadas e separando-as dos obstáculos.

## Introdução

O problema resolvido consiste em identificar e preencher regiões conectadas em um grid 2D, onde cada célula pode ser navegável (`0`) ou um obstáculo (`1`). O algoritmo Flood-Fill é amplamente utilizado em editores gráficos (como a ferramenta "balde de tinta") e em processamento de imagens para segmentação de regiões.

Neste projeto, o algoritmo percorre o grid a partir de uma célula inicial, identifica todas as células navegáveis conectadas (horizontal e verticalmente), e as preenche com uma cor específica (um número inteiro diferente de zero e um). Após preencher a região inicial, o algoritmo continua buscando e preenchendo outras regiões não conectadas, atribuindo cores diferentes para cada uma. Obstáculos (`1`) nunca são alterados.

## Como rodar o projeto

1. Instale a última versão do Python disponível em: https://www.python.org/downloads/
2. Baixe ou clone este repositório.
3. No terminal, navegue até a pasta do projeto e execute:
```bash
python main.py
```

## Versão do Python
Este projeto foi desenvolvido na versão 3.13.2 do Python.

## Funcionamento do Algoritmo Flood-Fill

O algoritmo Flood-Fill implementado funciona da seguinte forma:

- **Percurso inicial:** A partir de uma célula inicial fornecida pelo usuário, o algoritmo verifica se ela é navegável (`0`). Se for, inicia o preenchimento dessa região.
- **Preenchimento:** Utilizando uma abordagem iterativa (com pilha), o algoritmo visita todas as células conectadas (cima, baixo, esquerda, direita) que também são navegáveis, preenchendo-as com uma cor específica (um número inteiro).
- **Identificação de novas regiões:** Após preencher a primeira região, o algoritmo percorre todo o grid em busca de outras células navegáveis não preenchidas, repetindo o processo com uma nova cor para cada nova região encontrada.
- **Respeito aos limites e obstáculos:** O algoritmo nunca ultrapassa os limites do grid e nunca preenche células marcadas como obstáculo (`1`).

### Funções

#### flood_fill(grid, x, y, color)
- Preenche a região conectada de zeros (`0`) a partir da posição `(x, y)` com a cor especificada.

#### fill_all_regions(grid, start_x, start_y)
- Preenche todas as regiões de zeros na matriz, começando pela posição inicial e depois continuando para as demais regiões não conectadas.

#### print_grid(grid)
- Exibe a matriz no terminal de forma legível, mostrando as regiões preenchidas com cores diferentes.

---

## Exemplos de Entrada e Saída

### Exemplo 1

**Grid inicial:**
```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```
**Coordenadas iniciais:** (0, 0)

**Grid preenchido:**
```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```
Cada número diferente de `1` representa uma região conectada de zeros preenchida com uma cor diferente.

### Exemplo 2

**Grid inicial:**
```
0 1 0 0
1 1 1 0
0 0 1 0
0 1 0 0
```
**Coordenadas iniciais:** (0, 0)

**Grid preenchido:**
```
2 1 3 3
1 1 1 3
4 4 1 3
4 1 5 5
```
Neste exemplo, há múltiplas regiões separadas por obstáculos (`1`), cada uma recebendo uma cor diferente.

---

## Observações

- O algoritmo considera apenas movimentos ortogonais (cima, baixo, esquerda, direita).
- Obstáculos ou células já preenchidas são representados por `1` e não são alterados pelo algoritmo.
- O preenchimento é feito com números inteiros a partir de `2`, para diferenciar das células navegáveis originais (`0`) e dos obstáculos (`1`).
