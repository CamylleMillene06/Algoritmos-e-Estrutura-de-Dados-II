# Trabalho - Algoritmos e Estruturas de Dados II

## Objetivo

Este projeto tem como objetivo implementar algoritmos clássicos de grafos em Python, utilizando como estudo de caso a rede de pré-requisitos do dataset D2 (NICEN). A implementação inclui algoritmos de busca, identificação de componentes fortemente conexas e análises sobre a estrutura da rede.

## Dataset

O projeto utiliza o dataset **D2 - Pré-requisitos do NICEN**, composto pelos arquivos:

```
data/
├── D2_prereqs-nicen.csv
└── D2_prereqs-nicen-nodes.csv
```

## Integrantes

- Camylle Millene
- Tawanny Tácyla

---

# Estrutura do projeto

```
.
├── data/
│   ├── D2_prereqs-nicen.csv
│   └── D2_prereqs-nicen-nodes.csv
│
├── src/
│   ├── main.py
│   ├── grafo.py
│   ├── bfs.py
│   ├── dfs.py
│   └── componentes.py
│
├── requirements.txt
└── README.md
```

## Descrição dos arquivos

- **main.py**: arquivo principal responsável por executar o programa.
- **grafo.py**: implementação da estrutura do grafo e funções auxiliares.
- **bfs.py**: implementação da Busca em Largura (BFS).
- **dfs.py**: implementação da Busca em Profundidade (DFS).
- **componentes.py**: implementação do algoritmo de Kosaraju para identificação das componentes fortemente conexas.

## Funcionalidades implementadas

- Representação do grafo por lista de adjacência;
- Leitura do dataset CSV;
- Estatísticas da rede (vértices, arestas e grau médio);
- Busca em Largura (BFS);
- Reconstrução do menor caminho;
- Busca em Profundidade (DFS);
- Árvore da DFS;
- Componentes fortemente conexas (Kosaraju);
- Identificação do vértice de maior grau;
- Verificação de ciclos.

## Como executar

O programa deve ser executado a partir da pasta `src`. Para isso, basta abrir um terminal nessa pasta e executar o arquivo `main.py`:

```bash
python main.py
```

Em alguns programas, pode ser necessário utilizar:

```bash
python3 main.py
```

## Requisitos

- Python 3.10 ou superior.
