import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import collections
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


def draw_tree(tree_root: Optional[Node], colors: Dict[str, str]) -> None:
    tree = nx.DiGraph()
    pos: Dict[str, Tuple[float, float]] = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Apply colors, if a node ID is not in the colors dict, default to skyblue
    node_colors = [colors.get(node_id, "skyblue") for node_id in tree.nodes()]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
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


def dfs_visualize(root: Optional[Node], total_steps: int) -> Dict[str, str]:
    """
    Depth-First Search (DFS) using stack (LIFO) and assigns colors based on visit order.
    Returns a dictionary mapping Node IDs to colors
    """
    if root is None:
        return {}

    visited_colors: Dict[str, str] = {}
    stack: List[Node] = [root]
    step = 0
    while stack:
        node = stack.pop()

        if node.id not in visited_colors:
            visited_colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited_colors


def bfs_visualize(root: Optional[Node], total_steps: int) -> Dict[str, str]:
    """
    Breadth-First Search (BFS) using queue (FIFO) and assigns colors based on visit order.
    Returns a dictionary mapping Node IDs to colors
    """
    if root is None:
        return {}

    visited_colors: Dict[str, str] = {}
    queue: collections.deque[Node] = collections.deque([root])
    step = 0
    while queue:
        node = queue.popleft()

        if node.id not in visited_colors:
            visited_colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited_colors


def generate_color(step: int, total_steps: int) -> str:
    """
    Generates a Hex color code of a gradient from dark blue to light blue
    Args:
        step (int): The current step index (0 to total_steps-1).
        total_steps (int): Total number of nodes to visit.
    """
    # Dark Blue: #1296F0 (RGB: 18, 150, 240)
    start_rgb = (18, 150, 240)
    # Pastel Blue: #CCEEFF (RGB: 204, 238, 255)
    end_rgb = (204, 238, 255)

    if total_steps <= 1:
        ratio = 0
    else:
        ratio = step / (total_steps - 1)

    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)

    return f'#{r:02x}{g:02x}{b:02x}'


def count_nodes(node: Optional[Node]) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    print(f"Heapified list: {heap_list}")

    heap_tree_root = list_to_heap_tree(heap_list)
    total_nodes = count_nodes(heap_tree_root)

    print("Visualizing DFS...")
    dfs_colors = dfs_visualize(heap_tree_root, total_nodes)
    draw_tree(heap_tree_root, dfs_colors)

    print("Visualizing BFS...")
    bfs_colors = bfs_visualize(heap_tree_root, total_nodes)
    draw_tree(heap_tree_root, bfs_colors)
