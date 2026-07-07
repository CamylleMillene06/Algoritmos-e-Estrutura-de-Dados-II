class Componentes:

    def __init__(self, grafo):
        self.grafo = grafo

    def encontrar_componentes(self):

        visitados = set()
        ordem = []
        componentes = []

        for vertice in self.grafo.vertices:

            if vertice not in visitados:

                self._dfs_ordem(vertice, visitados, ordem)

        return componentes
        
    def _dfs_ordem(self, vertice, visitados, ordem):

        visitados.add(vertice)

        for vizinho in self.grafo.adj.get(vertice, []):

            if vizinho not in visitados:

                self._dfs_ordem(vizinho, visitados, ordem)

        ordem.append(vertice)
