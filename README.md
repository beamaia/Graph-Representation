# Representação de grafo

Implementação I1 feita por Beatriz Maia e Sophie Dilhon para a disciplina de Teoria dos Grafos.

O programa permite a leitura de um grafo tanto por matriz de adjacência, quanto por lista de adjacência. O usuário pode escolher qual representação ele quer utilizar através do menu de escolha.

## Sobre
### Menu de escolha

Para utilizar o menu de escolha, é preciso digitar `1` ou `2` de acordo com a representação escolhida. O programa apresenta a seguinte mensagem para auxiliar com a escolha:

```
(0) Terminar o programa
(1) Lista de adjacência
(2) Matriz de adjacência
```
O usuário também pode digitar `0` caso queira finalizar o programa. Caso for escolhido um valor diferente, o programa solicita que o usuário digite novamente.

O grafo é considerado valorado se o peso das arestas forem diferente de 0. Se uma aresta possuir valor nulo, o grafo é automaticamente considerado não valorado

### Lista de adjacência

A classe `Lista` do arquivo `lista.py` apresenta a implementação de uma lista de adjacência de um grafo. 

Para inicializar uma lista, é preciso informar o número de vértices, o número de arestas e se o grafo é direcionado. A lista é inicializada do tamanho do número de vértices com todos os seus indíces possuindo listas vazias.

Para adicionar uma aresta a lista de adjacência é preciso informar o vértice origin, o vértice destino e o peso da aresta. 


### Matriz de adjacência

A classe `Matriz` do arquivo `matriz.py` apresenta a implementação de uma matriz de adjacência de um grafo. 

Para inicializar uma Matriz é preciso informar a quantidade de vértices e arestas do grafo e este é ou não direcionado. A matriz é inicializada com a quantidade de linhas e colunas sendo igual a quantidade de vértices, e preenchida de zeros.

Para adicionar uma resta a matriz de adjacência é preciso informas os vértices de origem e destino dela, e também seu peso. Se o grafo é não valorado o valor registrado na matriz será 1, e não o peso da aresta.

### Apresentação
O arquivo é salvo com a extenção `.dot`. Um grafo não direcionado recebe o nome de `grafo G` e um digrafo recebe o nome de `digrafo G`.

Para grafos não valorados e não direcionados ele irá apresentar:
```
{
  u -- v;
}
```

Para grafos valorados e não direcionados ele irá apresentar:
```
{
  u -- v [label = custo];
}
```

Para grafos não valorados e não direcionados ele irá apresentar:
```
{
  u -> v;
}
```

Para grafos valorados e direcionados ele irá apresentar:
```
{
  u -> v [label = custo];
}
```

## Como utilizar
Para executar o programa é necessário ter a versão de python 3.6 ou superior. Para executar no linux é necessário escrever na linha de comando:

```
python3 main.py arquivo
```

### Entrada

O arquivo de entrada deve seguir um dos senguintes padrões:
```
grafo_n_m.txt
digrafo_n_m.txt
```

O nome é importante para identificar qual é o tipo de grafo que sera lido. 

O arquivo de entrada deve seguir o seguinte padrão:
```
n m 
x1 y1 z1
x2 y2 z2
...
xn yj zm
```

No qual `n` é o número de vértices e `m` é o número de arestas do grafo. O documento também pode ter comentário, representado pela letra `c`. O programa ignora as linhas que iniciam com `c`.

A primeira linha não comentário informará a quantidade de vértices e arestas. As `m` linhas seguintes são as arestas na seguinte ordem:

```
vertice_origin vertice_destino peso 
```

Um exemplo de entrada seria:
```
c grafo não valorado com arestas paralelas
c by: bea e sophie
7 10
c lista de arestas
1 2 0
1 2 0
1 3 0
2 4 0
3 4 0
3 5 0
4 7 0
5 6 0
5 7 0
6 7 0
```