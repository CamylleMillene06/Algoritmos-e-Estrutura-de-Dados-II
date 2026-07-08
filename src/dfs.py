class DFS:

    def __init__(self, grafo):
        self.grafo = grafo
        self.tempo = 0
        self.entrada = {}
        self.saida = {}
        self.pai = {}

    def buscar(self, inicio):

        self.tempo = 0
        self.entrada = {}
        self.saida = {}
        self.pai = {}

        visitados = set()
        ordem = []
        
        self.pai[inicio] = None
        
        self._dfs(inicio, visitados, ordem)

        return ordem

    def _dfs(self, vertice, visitados, ordem):

        visitados.add(vertice)

        self.tempo += 1
        self.entrada[vertice] = self.tempo

        ordem.append(vertice)

        if vertice in self.grafo.adj:

            for vizinho in self.grafo.adj[vertice]:

                if vizinho not in visitados:

                    self.pai[vizinho] = vertice

                    self._dfs(vizinho, visitados, ordem)

        self.tempo += 1
        self.saida[vertice] = self.tempo
