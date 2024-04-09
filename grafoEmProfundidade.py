def DFS(grafo, nó, explorado):
    if nó not in explorado:
        explorado.add(nó)
        print(nó)  
        for neighbor in grafo[nó]:
            if neighbor not in explorado:
                DFS(grafo, neighbor, explorado)

def buscaEmProfundidade(grafo):
    explorado = set()
    for nó in grafo:
        if nó not in explorado:
            DFS(grafo, nó, explorado)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

buscaEmProfundidade(grafo)