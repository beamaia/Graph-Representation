class Grafo:
    """
        Classe destinada para armazenar informações sobre o grafo

        `atributos` 
            :num_vertices, num_arestas (int)
            :direcionado, valorado (bool)
    """
    def __init__(self, vertices, arestas, direcionado):
        """
            Construtor de Grafo

            `param` vertices: numero de vertices 
            `param` arestas: numero de arestas
            `param` direcionado: flag que identifica se o grafo eh direcionado
        """
        self.num_vertices = vertices
        self.num_arestas = arestas
        self.direcionado = direcionado
    
    def eh_valorado(self, valorado):
        """
            Método que dá valor ao atributo valorado

            `param` valorado: flag que identifica se o grafo eh valorado
        """
        self.valorado = valorado

    def __str__(self):
        """
            Representacao string do objeto Grafo

            `return`: string representativa do objeto
        """
        if self.direcionado:
            return f"grafo com {self.vertices} v e {self.arestas} a, direcionado, {self.valorado}"
        elif not self.direcionado:
            return f"grafo com {self.vertices} v e {self.arestas} a, não direcionado, {self.valorado}"