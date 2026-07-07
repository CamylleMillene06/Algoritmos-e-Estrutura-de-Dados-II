class Componentes:

    def __init__(self, grafo):
        self.grafo = grafo

    def encontrar_componentes(self):

        visitados = set()  # Controla os vértices já percorridos
        ordem = []  # Armazenará a ordem de finalização da primeira DFS
        componentes = []  # Guardará as componentes fortemente conexas

        for vertice in self.grafo.vertices:  # Garante que todos os vértices do grafo sejam analisados, mesmo que existam partes desconectadas

            if vertice not in visitados:

                self._dfs_ordem(vertice, visitados, ordem)  # Executa a primeira DFS do algoritmo de Kosaraju

        return componentes
        
    def _dfs_ordem(self, vertice, visitados, ordem):

        visitados.add(vertice)

        for vizinho in self.grafo.adj.get(vertice, []):

            if vizinho not in visitados:

                self._dfs_ordem(vizinho, visitados, ordem)

        ordem.append(vertice)

    def _dfs_componente(self, grafo, vertice, visitados, componente):

        visitados.add(vertice)

        componente.append(vertice)

        for vizinho in grafo.adj.get(vertice, []):

            if vizinho not in visitados:

                self._dfs_componente(grafo, vizinho, visitados, componente)
