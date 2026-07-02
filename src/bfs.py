from collections import deque

class BFS:

    def __init__(self, grafo):
        self.grafo = grafo

    def buscar(self, inicio):

        visitados = set()
        fila = deque()

        fila.append(inicio)
        visitados.add(inicio)

        while fila:

            atual = fila.popleft()

            print(atual)
            
            if atual in self.grafo.adj:

                for vizinho in self.grafo.adj[atual]:

                    if vizinho not in visitados:

                        visitados.add(vizinho)
                        fila.append(vizinho)

                
