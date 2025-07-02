import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def plot_event_graph(influence_matrix, threshold=0.05):
    n = influence_matrix.shape[0]
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if influence_matrix[i, j] > threshold:
                G.add_edge(i, j, weight=influence_matrix[i, j])
    pos = nx.spring_layout(G)
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, edge_color=weights, edge_cmap=plt.cm.viridis, node_color='skyblue')
    plt.title("Event Graph (TIM Influence)")
    plt.show()

# 👇 Пример: создаём синтетическую матрицу влияния
if __name__ == "__main__":
    influence = np.random.rand(10, 10) * np.tri(10, 10, k=-1)  # нижнетреугольная
    plot_event_graph(influence)
