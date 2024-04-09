import networkx as nx
import matplotlib.pyplot as plt

def DFS(grafo, no, explorado):
    if no not in explorado:
        explorado.add(no)
        print(no)
        for neighbor in grafo[no]:
            if neighbor not in explorado:
                DFS(grafo, neighbor, explorado)

def buscaEmProfundidade(grafo):
    explorado = set()
    for no in grafo:
        if no not in explorado:
            DFS(grafo, no, explorado)

def desenhar_grafo(grafo):
    G = nx.Graph()
    for no, vizinhos in grafo.items():
        for vizinho in vizinhos:
            G.add_edge(no, vizinho)
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold") 
    plt.title("Grafo de Profundidade")
    plt.show()

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

buscaEmProfundidade(grafo)
desenhar_grafo(grafo)
