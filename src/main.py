from grafo import Grafo


grafo = Grafo()

grafo.carregar_csv("../data/D2_prereqs-nicen.csv")

print("Quantidade de vértices:", len(grafo.vertices))
print("Quantidade de arestas:", grafo.arestas)
