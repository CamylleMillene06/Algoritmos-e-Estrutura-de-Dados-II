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

## Commit 12: Implementando a estrutura básica da classe Grafo

### Objetivo

Neste commit foi iniciada a implementação da classe `Grafo`, responsável por representar a rede de pré-requisitos utilizada durante todo o projeto. Como todos os algoritmos seriam executados sobre essa estrutura, foi necessário definir uma forma eficiente de armazenar as disciplinas e as relações entre elas.

### Código implementado

```python
class Grafo:

    def __init__(self):

        self.adj = {}
        self.vertices = set()
        self.arestas = 0
```

### Explicação do código

A primeira etapa foi a criação da classe `Grafo`.

```python
class Grafo:
```

Essa classe passou a concentrar todas as operações relacionadas à construção e manipulação da rede. Em seguida foi implementado o método construtor.

```python
def __init__(self):
```

Esse método é executado automaticamente sempre que um novo objeto da classe é criado. Sua função é inicializar todas as estruturas necessárias para representar o grafo. A primeira estrutura criada foi a lista de adjacência.

```python
self.adj = {}
```

Foi utilizado um dicionário do Python para representar a lista de adjacência. Cada chave corresponde ao código de uma disciplina e o valor associado é uma lista contendo todas as disciplinas que podem ser alcançadas a partir dela. Essa representação foi escolhida porque a rede possui poucas conexões em relação ao número de disciplinas, tornando a lista de adjacência mais eficiente que uma matriz de adjacência tanto em memória quanto durante as buscas. Em seguida foi criado um conjunto para armazenar todos os vértices.

```python
self.vertices = set()
```

A utilização de um conjunto garante que cada disciplina seja armazenada apenas uma vez, mesmo que apareça em várias relações de pré-requisito. Além disso, conjuntos permitem consultas rápidas para verificar se determinado vértice já foi inserido. Por fim foi criado um contador de arestas.

```python
self.arestas = 0
```

Essa variável será incrementada sempre que uma nova relação de pré-requisito for adicionada ao grafo. Dessa forma, o número de arestas permanece sempre atualizado, sem necessidade de percorrer toda a estrutura para realizar essa contagem.

### Resultado

Ao final deste commit o projeto passou a possuir uma estrutura capaz de armazenar completamente uma rede representada por um grafo dirigido. Essa implementação serviu de base para todos os algoritmos desenvolvidos posteriormente.

## Commit 13: Leitura do grafo a partir de arquivo CSV

### Objetivo

Após definir a estrutura do grafo, o próximo passo foi permitir que a rede fosse construída automaticamente a partir do arquivo CSV fornecido para a atividade.

### Código implementado

```python
import csv
```

```python
def carregar_csv(self, caminho):

    with open(caminho, newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            origem = linha["Source"]
            destino = linha["Target"]

            self.adicionar_aresta(origem, destino)
```

### Explicação do código

Inicialmente foi importado o módulo `csv`, pertencente à biblioteca padrão do Python.

```python
import csv
```

Esse módulo permite realizar a leitura de arquivos separados por vírgulas sem necessidade de bibliotecas externas. Em seguida foi criado o método responsável por carregar os dados.

```python
def carregar_csv(self, caminho):
```

O parâmetro `caminho` recebe o endereço do arquivo CSV que será utilizado para construir o grafo. Depois disso o arquivo é aberto.

```python
with open(caminho, newline="", encoding="utf-8") as arquivo:
```

A instrução `with` garante que o arquivo será fechado automaticamente ao final da leitura. Foi definida também a codificação UTF-8 para evitar problemas com caracteres especiais. Na sequência foi utilizado o `DictReader`.

```python
leitor = csv.DictReader(arquivo)
```

Diferentemente da leitura tradicional, o `DictReader` transforma cada linha do arquivo em um dicionário, permitindo acessar diretamente cada coluna pelo seu nome. Assim tornou-se possível obter os valores das colunas `Source` e `Target`.

```python
origem = linha["Source"]
destino = linha["Target"]
```

Essas duas informações representam, respectivamente, a disciplina de origem e a disciplina de destino da relação de pré-requisito. Após obter essas informações, a aresta correspondente é adicionada ao grafo.

```python
self.adicionar_aresta(origem, destino)
```

Esse método realiza toda a atualização da estrutura interna da classe.

### Resultado

A partir deste commit deixou de ser necessário inserir manualmente todas as relações entre disciplinas. O programa passou a construir automaticamente toda a rede de pré-requisitos a partir dos arquivos fornecidos para a atividade.
