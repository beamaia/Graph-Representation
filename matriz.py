from grafo import Grafo

class Matriz(Grafo):
    '''
    Classe destinada para armazenar matriz de adjacencia.
    Por padrao, a matriz inicializa com vertices e arestas
    igual a zero e a flag direcionado como False caso nao
    for fornecido parametros.
    '''
    def __init__(self, vertices=0, arestas=0, direcionado=False):
        super().__init__(vertices, arestas, direcionado)

        self.matriz = []
        
        # Inicializa uma matriz num_vertices X num_vertices 
        # com os valores zerados
        for linha in range(self.num_vertices):
            aux_linha = []
            for coluna in range(self.num_vertices):
                aux_linha.append(0)    
            self.matriz.append(aux_linha)

    def adiciona_aresta(self, origin, destino, peso):
        # Se o grafo nao for valorado, o peso eh 1
        if not self.valorado:
            peso = 1

        # Adiciona aresta origin->destino
        self.matriz[origin-1][destino-1] = peso
        
        # Se grafo nao for direcionado destino->origin
        if not self.direcionado:
            self.matriz[destino-1][origin-1] = peso

    def __str__(self):
        # String auxiliar para impressao
        if self.direcionado:
            divisor = "->"
        else:
            divisor = "--"
        
        resposta = "{\n"
                
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                peso = self.matriz[i][j]

                if not self.direcionado and j < i:
                    continue
                elif peso != 0:
                    resposta += f"  {i+1} {divisor} {j+1}"
                    if self.valorado:
                        resposta += f" [label = {peso}]"
                
                    resposta += ";\n"

        resposta += "}"
        return resposta