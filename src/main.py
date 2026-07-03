from grafo import Grafo
from bfs import BFS

grafo = Grafo()

grafo.carregar_csv("../data/D2_prereqs-nicen.csv")

grafo.mostrar_informacoes()

print("\nBFS iniciando em MAT001:\n")

bfs = BFS(grafo)

ordem, pai = bfs.buscar("MAT001")

print("\nOrdem da BFS:")

for disciplina in ordem:
    print(disciplina)
