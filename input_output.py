import sys
from lista import Lista
from matriz import Matriz

def eh_direcionado(entrada):
    """ 
        Função que verifica se o grafo passado como entrada é direcionado 
        
        :param entrada: arquivo de entrada contendo a descrição do grafo
        :returns: True se é direcionado, False se não
    """

    if "digrafo" in entrada.lower():
        return True
    elif "grafo" in entrada.lower():
        return False
    else:
        print("Esse arquivo não está dentro dos padrões esperados!")
        print("Terminando o programa")
        sys.exit() 


def le_entrada(entrada, representa_lista):
    """ 
        Função que le o arquivo de entrada e cria o grafo 

        :param entrada: arquivo de entrada contendo a descrição do grafo
        :param representa_lista: forma que será representado o grafo
        :returns: a representação do grafo em lista ou matriz de adjacencia
    """
    try: 
        arquivo = open(entrada, "r")
    except:
        print("Esse arquivo não está dentro dos padrões esperados!")
        print("Terminando o programa")
        sys.exit()
        
    inicio = True
    prim_aresta = True
    grafo = ""

    direcionado = eh_direcionado(entrada)

    for line in arquivo:

        # Ignora linhas de comentario
        if line[0] != "c":
            if inicio:
                line = line.split()
                
                if representa_lista:
                    grafo = Lista(int(line[0]), int(line[1]), direcionado)
                else:
                    grafo = Matriz(int(line[0]), int(line[1]), direcionado)
                inicio = False

            else:
                line = line.split()
                if prim_aresta:
                    if int(line[2]) == 0:
                        grafo.eh_valorado(False)
                    else:
                        grafo.eh_valorado(True)
                    prim_aresta = False
                grafo.adiciona_aresta(int(line[0]), int(line[1]), int(line[2]))
    
    arquivo.close()
    return grafo


def escreve_grafo(grafo):
    tag = ""
    if grafo.valorado:
        tag = "v"

    if not grafo.direcionado:
        arquivo = open(f"grafo{tag}_{grafo.num_vertices}_{grafo.num_arestas}.dot", "w")
        arquivo.write("graph G\n")

    else:
        arquivo = open(f"digrafo{tag}_{grafo.num_vertices}_{grafo.num_arestas}.dot", "w")
        arquivo.write("digraph G\n")

    arquivo.write(grafo.__str__())
    arquivo.close()