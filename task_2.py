import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np


def draw_pythagoras_tree(x: float, y: float, angle: float,
                         length: float, depth: int, ax: Axes) -> None:
    """
    Recursively draws a binary fractal tree (Pythagoras Tree) using matplotlib
    Args:
        x (float): Starting x-coordinate
        y (float): Starting y-coordinate
        angle (float): Current angle of the branch in radians
        length (float): Length of the current branch
        depth (int): Current recursion depth (stops at 0)
        ax (plt.Axes): Matplotlib axes object to draw on
    """
    if depth == 0:
        return

    # end coordinates of the branch
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # color and line width based on depth
    color = "black" if depth > 4 else "green"
    line_width = max(1, depth * 0.7)  # ensure width is at least 1

    ax.plot([x, x_end], [y, y_end], color=color, lw=line_width)

    new_length = length * 0.7  # reduce branch length
    delta_angle = np.pi / 4  # 45 degrees branch split

    # left branch
    draw_pythagoras_tree(x_end, y_end, angle + delta_angle, new_length, depth - 1, ax)
    # right branch
    draw_pythagoras_tree(x_end, y_end, angle - delta_angle, new_length, depth - 1, ax)


if __name__ == "__main__":
    try:
        user_input = input("Enter the recursion depth (recommended 2-12): ")
        recursion_depth = int(user_input)
        if recursion_depth <= 1:
            print("Level must be <= 1. Defaulting to 2.")
            recursion_depth = 2
        elif recursion_depth > 12:
            print("Too high a recursion level. Defaulting to 12.")
            recursion_depth = 12
    except ValueError:
        print("Invalid number. Using default value: 8.")
        recursion_depth = 8

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis("off")
    ax.set_title(f"Pythagoras Tree (Depth: {recursion_depth})")

    draw_pythagoras_tree(0, 0, np.pi / 2, 100, recursion_depth, ax)
    plt.show()
