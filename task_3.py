import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple


def dijkstra_algorithm(graph: nx.Graph, start: str) -> Dict[str, float]:
    """
    Implements Dijkstra's algorithm to find the shortest paths from
    starting node to all other nodes in a weighted graph using a binary heap.
    Returns a dictionary where keys are nodes and values are
    the shortest distances from the start node.
    """
    shortest_paths: Dict[str, float] = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0

    priority_queue: List[Tuple[float, str]] = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes.get("weight", 1)
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge("A", "B", weight=4)
    G.add_edge("A", "C", weight=2)
    G.add_edge("B", "C", weight=1)
    G.add_edge("B", "D", weight=5)
    G.add_edge("C", "D", weight=8)
    G.add_edge("C", "E", weight=10)
    G.add_edge("D", "E", weight=2)
    G.add_edge("D", "F", weight=6)
    G.add_edge("E", "F", weight=3)

    start_node = "A"
    shortest_paths = dijkstra_algorithm(G, start_node)

    print(f"Shortest paths from node '{start_node}':")
    for node, distance in shortest_paths.items():
        print(f"To {node}: {distance}")

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 5))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.title(f"Weighted Graph (Start: {start_node})")
    plt.axis("off")
    plt.show()
