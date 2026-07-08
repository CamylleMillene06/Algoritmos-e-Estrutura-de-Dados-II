from grafo import Grafo
from bfs import BFS
from dfs import DFS
from componentes import Componentes

grafo = Grafo()

grafo.carregar_csv("../data/D2_prereqs-nicen.csv")

grafo.mostrar_informacoes()

bfs = BFS(grafo)

ordem, pai = bfs.buscar("MAT001")

print("\nOrdem da BFS:")

for disciplina in ordem:
    print(disciplina)

print("\nMenor caminho entre MAT001 e MAT004:")

caminho = bfs.menor_caminho("MAT001", "MAT004")

if caminho:
    print(" -> ".join(caminho))
else:
    print("Não existe caminho.")

print("\nOrdem de visita da DFS:")

dfs = DFS(grafo)

ordem_dfs = dfs.buscar("MAT001")

for disciplina in ordem_dfs:
    print(disciplina)

print("\nTempos da DFS:")

for vertice in ordem_dfs:
    print(
        f"{vertice}: entrada = {dfs.entrada[vertice]}, "
        f"saida = {dfs.saida[vertice]}"
    )

print("\nÁrvore da DFS:")

for vertice in ordem_dfs:

    if dfs.pai[vertice] is None:

        print(f"{vertice}: raiz")

    else:

        print(f"{vertice}: pai = {dfs.pai[vertice]}")
        
print("\nComponentes fortemente conexas:")

componentes = Componentes(grafo)

resultado = componentes.encontrar_componentes()

for i, componente in enumerate(resultado, start=1):

    print(f"Componente {i}: {' -> '.join(componente)}")

print("\nNó de maior grau:")

vertice, grau = grafo.maior_grau()

print("Vértice:", vertice)
print("Grau:", grau)

print("\nVerificação de ciclos:")

if grafo.verificar_ciclo():

    print("O grafo possui ciclo.")

else:

    print("O grafo não possui ciclos.")
    
