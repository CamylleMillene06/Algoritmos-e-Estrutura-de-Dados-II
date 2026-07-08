import csv


class Grafo:

    def __init__(self):
        self.adj = {}
        self.vertices = set()
        self.arestas = 0

    def adicionar_aresta(self, origem, destino):

        self.vertices.add(origem)
        self.vertices.add(destino)

        if origem not in self.adj:
            self.adj[origem] = []

        self.adj[origem].append(destino)
        self.arestas += 1

    def carregar_csv(self, arquivo):

        with open(arquivo, newline="", encoding="utf-8") as csvfile:

            leitor = csv.DictReader(csvfile)

            for linha in leitor:

                origem = linha["Source"]
                destino = linha["Target"]

                self.adicionar_aresta(origem, destino)

    def grau_medio(self):

        if len(self.vertices) == 0:
            return 0

        return self.arestas / len(self.vertices)

    def maior_grau(self):

        graus = {}

        for vertice in self.vertices:
            graus[vertice] = 0

        for origem in self.adj:

            graus[origem] += len(self.adj[origem])

            for destino in self.adj[origem]:
                graus[destino] += 1

        maior_no = None
        maior_grau = -1

        for vertice in graus:

            if graus[vertice] > maior_grau:

                maior_no = vertice
                maior_grau = graus[vertice]

        return maior_no, maior_grau

    def verificar_ciclo(self):

        visitados = set()
        pilha = set()

        for vertice in self.vertices:

            if vertice not in visitados:

                if self._dfs_ciclo(vertice, visitados, pilha):

                    return True

        return False

    def _dfs_ciclo(self, vertice, visitados, pilha):

        visitados.add(vertice)
        pilha.add(vertice)

        for vizinho in self.adj.get(vertice, []):

            if vizinho not in visitados:

                if self._dfs_ciclo(vizinho, visitados, pilha):

                    return True

            elif vizinho in pilha:

                return True

        pilha.remove(vertice)

        return False

    def grafo_transposto(self):

        transposto = Grafo()

        for origem in self.adj:

            for destino in self.adj[origem]:

                transposto.adicionar_aresta(destino, origem)

        return transposto

    def mostrar_informacoes(self):

        print("Número de vértices:", len(self.vertices))
        print("Número de arestas:", self.arestas)
        print("Grau médio:", round(self.grau_medio(), 2))
