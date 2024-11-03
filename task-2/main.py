import matplotlib.pyplot as plt
import networkx as nx


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


def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(reversed(list(graph[vertex])))
    return path


def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(graph[vertex])
    return path


def dijkstra(graph, start, end):
    return nx.dijkstra_path(graph, source=start, target=end)


if __name__ == "__main__":
    G = create_graph()

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    start_node = 'Kyiv'
    dfs_path = dfs(G, start_node)
    bfs_path = bfs(G, start_node)

    start, end = 'Kyiv', 'Odessa'
    shortest_path = dijkstra(G, start, end)

    with open("readme.md", "w") as f:
        f.write("# Порівняння алгоритмів DFS і BFS\n\n")
        f.write(
            "У цьому проекті реалізовано граф міст України та алгоритми для пошуку шляхів у цьому графі. Алгоритми, які використовуються: DFS (пошук у глибину), BFS (пошук у ширину), та алгоритм Дейкстри для знаходження найкоротшого шляху між двома вершинами.\n\n")
        f.write("## Результати виконання алгоритмів\n\n")
        f.write(f"- Шлях, знайдений алгоритмом DFS з вершини 'Kyiv': {dfs_path}\n")
        f.write(f"- Шлях, знайдений алгоритмом BFS з вершини 'Kyiv': {bfs_path}\n")
        f.write(f"- Найкоротший шлях від 'Kyiv' до 'Odessa' за алгоритмом Дейкстри: {shortest_path}\n\n")
        f.write("## Порівняння DFS і BFS\n\n")
        f.write(
            "- DFS (пошук у глибину): Алгоритм йде якнайглибше від початкової вершини, тому шлях може бути довшим або менш оптимальним для деяких цілей.\n")
        f.write(
            "- BFS (пошук у ширину): Алгоритм йде рівнями, тому знаходить найкоротший шлях (за кількістю вершин) від початкової вершини до будь-якої іншої.\n\n")
        f.write(
            "Алгоритм BFS має перевагу у знаходженні найкоротшого шляху у графах без ваги або коли ваги всіх ребер однакові. У той час як DFS може знайти будь-який шлях, але не обов'язково найкоротший.")
