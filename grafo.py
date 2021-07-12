class Grafo:
    def __init__(self, vertices, arestas, direcionado):
        self.num_vertices = vertices
        self.num_arestas = arestas
        self.direcionado = direcionado
    
    def eh_valorado(self, valorado):
        self.valorado = valorado

    def __str__(self):
        if self.direcionado:
            return f"grafo com {self.vertices} v e {self.arestas} a, direcionado, {self.valorado}"
        elif not self.direcionado:
            return f"grafo com {self.vertices} v e {self.arestas} a, não direcionado, {self.valorado}"