from sys import version_info
from grafo import Grafo

class VerticeDestino:
    """
        Classe destinada para armazenar o valor do vertice destino
        e o custo do peso da aresta.
    """

    def __init__(self, vertice, peso):
        """
            Construtor de VerticeDestino. 

            :param vertice: valor do vertice 
            :param peso: valor do peso 
        """

        self.vertice = vertice
        self.peso = peso

    def str(self, valorada):
        """
            String representativa do vertice destino e peso.
            Eh necessario saber se o grafo eh valorado ou nao. 

            :param valorada: Flag que indica se uma aresta eh valorada. 
            :return: string representativa do vertice destino + peso
        """

        if valorada:
            return f"{self.vertice} [label = {self.peso}];"
        else:
            return f"{self.vertice};"            

class Lista(Grafo):
    """
        Classe destinada para armazenar lista de adjacencia.
        Por padrao, a lista inicializa com vertices e arestas
        igual a zero e a flag direcionado como False caso nao
        for fornecido parametros.
    """

    def __init__(self, vertices=0, arestas=0, direcionado=False):
        """
            Construtor de Lista. Inicializa uma lista vazia do 
            tamanho do numero de vertices

            :param vertices: numero de vertices 
            :param arestas: numero de arestas
            :param direcionado: flag que identifica se grafo eh direcionado
        """

        super().__init__(vertices, arestas, direcionado)

        self.vertices = []
        
        # Inicializa lista do tamanho de verticies com cada
        # inidice uma lista vazia
        for vertice in range(self.num_vertices):
            self.vertices.append([])

    def adiciona_aresta(self, origin, destino, peso):
        """
            Adiciona aresta para lista.  

            :param origin: valor do vertice origin
            :param destino: valor do vertice destino
            :param peso: peso da aresta
        """

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
        """
            Representacao string do objeto Lista.

            :return: string representativa do objeto Lista
        """
        
        # String auxiliar para apresentacao
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