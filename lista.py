from sys import version_info
from grafo import Grafo

class VerticeDestino:
    '''
    Classe destinada para armazenar o valor do vertice destino
    e o custo do peso da aresta
    '''

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

    def str(self, valorada):
        if valorada:
            return f"{self.vertice} [label = {self.peso}];"
        else:
            return f"{self.vertice};"            

class Lista(Grafo):
    '''
    Classe destinada para armazenar lista de adjacencia.
    Por padrao, a lista inicializa com vertices e arestas
    igual a zero e a flag direcionado como False caso nao
    for fornecido parametros.
    '''
    def __init__(self, vertices=0, arestas=0, direcionado=False):
        super().__init__(vertices, arestas, direcionado)

        self.vertices = []
        
        # Inicializa lista do tamanho de verticies com cada
        # inidice uma lista vazia
        for vertice in range(self.num_vertices):
            self.vertices.append([])

    def adiciona_aresta(self, origin, destino, peso):
        # Cria vertice destino + peso
        vertice_destino = VerticeDestino(destino, peso)

        # Cria a aresta de origin->destino
        self.vertices[origin - 1].append(vertice_destino)

        # Se o grafo nao for direcionado, precisa adicionar
        # a aresta destino -> origin
        if not self.direcionado:
            vertice_origin = VerticeDestino(origin, peso)
            self.vertices[destino - 1].append(vertice_origin)

    def __str__(self):
        # String auxiliar para impressao
        if self.direcionado:
            divisor = "->"
        else:
            divisor = "--"
        
        resposta = "{\n"

        # Anda pelos vertices
        for i, conjuntos in enumerate(self.vertices):

            # Anda pelas arestas
            for j in range(len(conjuntos)):
                if self.direcionado or (not self.direcionado and i + 1 <= conjuntos[j].vertice):
                    resposta += f"  {i + 1} {divisor} {conjuntos[j].str(self.valorado)}\n"
        
        resposta += "}"

        return resposta