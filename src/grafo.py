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
