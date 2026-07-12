# Histórico de Commits

Este documento apresenta a evolução do desenvolvimento do projeto **Exploração de Grafos em uma Rede de Pré-requisitos do NICEN**. Para cada commit são descritas as principais alterações realizadas, acompanhadas de uma explicação sobre o código implementado. 
---

# 02/07/2026

## Commit 1: Initial commit

### Objetivo

Criar o repositório do projeto e iniciar o controle de versões utilizando Git.

### Alterações realizadas

Neste primeiro momento ainda não havia código implementado. O commit foi utilizado apenas para criar o repositório e iniciar o projeto.

### Resultado

A partir deste commit todas as alterações passaram a ser registradas, permitindo acompanhar a evolução do desenvolvimento.

---

## Commit 2: README

### Objetivo

Adicionar a documentação inicial do projeto.

### Alterações realizadas

Foi criado o arquivo `README.md`, responsável por apresentar informações gerais sobre o projeto.

Inicialmente o arquivo continha apenas uma breve descrição da atividade, sendo atualizado ao longo do desenvolvimento conforme novas funcionalidades foram implementadas.

---

## Commit 3: Criar pasta data

### Objetivo

Organizar os arquivos utilizados como entrada do programa.

### Alterações realizadas

Foi criada a pasta

```text
data/
```

Nela passaram a ser armazenados os arquivos CSV contendo a rede de pré-requisitos fornecida para o desenvolvimento do trabalho.

A separação dos arquivos de entrada facilita a organização do projeto e evita misturar os dados com o código-fonte.

---

## Commit 4: Criar pasta src

### Objetivo

Organizar o código-fonte do projeto.

### Alterações realizadas

Foi criada a pasta

```text
src/
```

Essa pasta passou a concentrar todos os módulos responsáveis pela implementação dos algoritmos.

Essa organização torna o projeto mais limpo e facilita futuras modificações.

---

## Commit 5: Adicionando dataset D2 ao projeto

### Objetivo

Adicionar o conjunto de dados utilizado durante todo o projeto.

### Alterações realizadas

Foram adicionados os arquivos

```text
D2_prereqs-nicen.csv
D2_prereqs-nicen-nodes.csv
```

O primeiro arquivo contém todas as relações de pré-requisitos entre as disciplinas.

O segundo contém todos os vértices presentes na rede.

Esses arquivos seriam utilizados posteriormente para construir automaticamente o grafo.

---

## Commit 6: Módulo grafo

### Objetivo

Criar o módulo responsável pela representação da rede.

### Alterações realizadas

Foi criado o arquivo

```text
grafo.py
```

Neste momento ainda não existia implementação.

Apenas foi criado o módulo que posteriormente receberia toda a estrutura da classe `Grafo`.

---

## Commit 7: Programa principal

### Objetivo

Criar o ponto de entrada da aplicação.

### Alterações realizadas

Foi criado o arquivo

```text
main.py
```

Esse arquivo passou a ser responsável por executar todas as funcionalidades implementadas durante o projeto.

---

## Commit 8: Módulo BFS

### Objetivo

Criar o módulo destinado à Busca em Largura.

### Alterações realizadas

Foi criado o arquivo

```text
bfs.py
```

Nesse momento apenas a estrutura inicial foi criada. A implementação da busca seria realizada nos commits seguintes.

---

## Commit 9: Módulo DFS

### Objetivo

Criar o módulo destinado à Busca em Profundidade.

### Alterações realizadas

Foi criado o arquivo

```text
dfs.py
```

Assim como ocorreu com a BFS, inicialmente apenas a estrutura da classe foi criada.

---

## Commit 10: Módulo componentes

### Objetivo

Criar o módulo responsável pelo algoritmo de Kosaraju.

### Alterações realizadas

Foi criado o arquivo

```text
componentes.py
```

Esse módulo seria utilizado posteriormente para identificar as componentes fortemente conexas da rede.

---

## Commit 11: Módulo utilitário

### Objetivo

Criar um espaço para possíveis funções auxiliares.

### Alterações realizadas

Foi criado o arquivo

```text
utils.py
```

Durante o desenvolvimento percebeu-se que todas as funções puderam ser implementadas diretamente nas classes principais. Por esse motivo o arquivo foi removido na versão final do projeto.

---
