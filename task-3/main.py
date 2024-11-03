import heapq

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


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = create_graph()

    all_distances = []
    for city in graph.nodes:
        distances = dijkstra(graph, city)
        all_distances.append([distances[other_city] for other_city in graph.nodes])

    table = [[city] + distances for city, distances in zip(graph.nodes, all_distances)]
    headers = ["Місто"] + list(graph.nodes)
    print(tabulate(table, headers=headers, tablefmt="grid"))
