class DFS:

    def __init__(self, grafo):
        self.grafo = grafo

    def buscar(self, inicio):

        visitados = set()
        ordem = []

        self._dfs(inicio, visitados, ordem)

        return ordem
