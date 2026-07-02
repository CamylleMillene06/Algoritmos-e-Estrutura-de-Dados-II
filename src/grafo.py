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
                
    def mostrar_informacoes(self):

        print("Número de vértices:", len(self.vertices))
        print("Número de arestas:", self.arestas)
