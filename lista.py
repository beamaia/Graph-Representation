from sys import version_info
from grafo import Grafo

class VerticeDestino:
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

    def str(self, valorada):
        if valorada:
            return f"{self.vertice} [label = {self.peso}];"
        else:
            return f"{self.vertice};"            

class Lista(Grafo):
    def __init__(self, vertices=0, arestas=0, direcionado=False):
        super().__init__(vertices, arestas, direcionado)

        self.vertices = []
        
        for vertice in range(self.num_vertices):
            self.vertices.append([])

    def adiciona_aresta(self, origin, destino, peso):
        vertice_destino = VerticeDestino(destino, peso)
        self.vertices[origin - 1].append(vertice_destino)

        if not self.direcionado:
            vertice_origin = VerticeDestino(origin, peso)
            self.vertices[destino - 1].append(vertice_origin)

    def __str__(self):
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