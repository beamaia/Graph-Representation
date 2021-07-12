# Representação de grafo

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

### Lista de adjacência

A classe `Lista` do arquivo `lista.py` apresenta a implementação de uma lista de adjacência de um grafo. 


### Matriz de adjacência

A classe `Matriz` do arquivo `matriz.py` apresenta a implementação de uma matriz de adjacência de um grafo. 

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

O arquivo de entrada deve seguir um dos senguintes padrões:
```
grafo_n_m.txt
digrafo_n_m.txt
```
No qual `n` é o número de vértices e `m` é o número de arestas do grafo.