import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, List, Dict, Tuple


class Node:
    def __init__(self, key: int, color: str = "skyblue"):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val: int = key
        self.color: str = color
        self.id: str = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: Dict[str, Tuple[float, float]],
              x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """
    Recursively adds nodes and edges to the graph
    Returns the modified graph
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root: Optional[Node]) -> None:
    tree = nx.DiGraph()
    pos: Dict[str, Tuple[float, float]] = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Tree Visualization")
    plt.show()


def list_to_heap_tree(heap_list: List[int]) -> Optional[Node]:
    """
    Converts a list (representing a binary heap) into a tree of Node objects
    Logic:
    - Index i: Parent
    - Index 2*i + 1: Left Child
    - Index 2*i + 2: Right Child
    """
    if not heap_list:
        return None

    nodes = [Node(val) for val in heap_list]
    for i, current_node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        # left child
        if left_index < len(nodes):
            current_node.left = nodes[left_index]

        # ight child
        if right_index < len(nodes):
            current_node.right = nodes[right_index]

    # return the root
    return nodes[0]


def draw_heap(heap_list: List[int]) -> None:
    root = list_to_heap_tree(heap_list)
    if root:
        draw_tree(root)


if __name__ == '__main__':
    data = [10, 4, 5, 1, 3, 0, 2, 15]
    print(f"Original Data: {data}")

    heapq.heapify(data)
    print(f"Heapified Data: {data}")

    print("Visualizing Heap Tree...")
    draw_heap(data)
