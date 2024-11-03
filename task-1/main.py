import matplotlib.pyplot as plt
import networkx as nx
from tabulate import tabulate


def create_graph():
    G = nx.Graph()

    cities = ["Kyiv", "Lviv", "Odessa", "Kharkiv", "Dnipro", "Vinnytsia", "Poltava"]
    G.add_nodes_from(cities)

    G.add_edge("Kyiv", "Lviv", weight=540)
    G.add_edge("Kyiv", "Odessa", weight=480)
    G.add_edge("Kyiv", "Kharkiv", weight=470)
    G.add_edge("Kyiv", "Vinnytsia", weight=270)
    G.add_edge("Vinnytsia", "Lviv", weight=310)
    G.add_edge("Vinnytsia", "Odessa", weight=280)
    G.add_edge("Kharkiv", "Dnipro", weight=210)
    G.add_edge("Dnipro", "Odessa", weight=450)
    G.add_edge("Poltava", "Kharkiv", weight=140)
    G.add_edge("Poltava", "Kyiv", weight=340)

    return G


if __name__ == "__main__":
    G = create_graph()

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degree_centrality = nx.degree_centrality(G)

    data = [["Кількість вершин", num_nodes], ["Кількість ребер", num_edges]]
    print(tabulate(data, headers=["Характеристика", "Значення"], tablefmt="grid"))

    degree_data = [[node, f"{degree:.2f}"] for node, degree in degree_centrality.items()]
    print("\nСтупінь вершин:")
    print(tabulate(degree_data, headers=["Вершина", "Ступінь"], tablefmt="grid"))

    pos = nx.spring_layout(G, seed=42)  # розміщення графа на площині
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Модель транспортної мережі міст України")
    plt.show()
