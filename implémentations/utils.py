import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


from math import factorial, comb

def poisson(l):
    return lambda k: ((l**k)/(factorial(k)))*np.exp(-l)

def binomial(n,p):
    return lambda k: comb(n,k) * p**k * (1-p)**(n-k)

def geo(p):
    return lambda k: p*((1-p)**(k-1))


def my_plot_graph_mat(trans_mat: np.ndarray) -> None:
    G = nx.DiGraph()

    # ajout des arcs avec poids
    num_states = trans_mat.shape[0]
    edges, weights = [], [] 
    for i in range(num_states):
        for j in range(num_states):
            if trans_mat[i, j] > 0:
                G.add_edge(i, j, weight=trans_mat[i, j])
                edges.append((i, j))
                weights.append(trans_mat[i, j])

    # normalization des poids pour la coloration
    norm = mcolors.Normalize(vmin=min(weights), vmax=max(weights))
    cmap = plt.cm.Blues  
    edge_colors = [cmap(norm(w)) for w in weights]

    pos = nx.spring_layout(G)

    # affichage des noeuds
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, arrowsize=20)

    # affichages des arcs
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, edge_cmap=cmap, width=2, arrows=True)

    # ajout de l'échelle des couleurs
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, label="probabilité de transition") # @CorentinVaillant !ERROR HERE !!

    plt.show()
