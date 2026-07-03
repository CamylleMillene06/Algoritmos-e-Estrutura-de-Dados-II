class DFS:

    def __init__(self, grafo):
        self.grafo = grafo

    def buscar(self, inicio):

        visitados = set()
        ordem = []

        self._dfs(inicio, visitados, ordem)

        return ordem

    def _dfs(self, vertice, visitados, ordem):

        visitados.add(vertice)
        ordem.append(vertice)

        if vertice in self.grafo.adj:

            for vizinho in self.grafo.adj[vertice]:

                if vizinho not in visitados:

                    self._dfs(vizinho, visitados, ordem)
