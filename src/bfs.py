from collections import deque


class BFS:

    def __init__(self, grafo):
        self.grafo = grafo

    def buscar(self, inicio):

        visitados = set()
        fila = deque()
        ordem = []
        pai = {}

        fila.append(inicio)
        visitados.add(inicio)
        pai[inicio] = None

        while fila:

            atual = fila.popleft()
            ordem.append(atual)

            if atual in self.grafo.adj:

                for vizinho in self.grafo.adj[atual]:

                    if vizinho not in visitados:

                        visitados.add(vizinho)
                        pai[vizinho] = atual
                        fila.append(vizinho)

        return ordem, pai
