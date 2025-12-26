# goit-algo-fp

## Content

- **`task_1.py`**: Implements a linked list with insertion, deletion, search, printing, in-place reversal, merge sort and merging two sorted lists
- **`task_2.py`**: Recursively draws a Pythagoras fractal tree using `matplotlib` with configurable recursion depth
- **`task_3.py`**: Implements Dijkstra's shortest-path algorithm using a binary heap (`heapq`) and demonstrates it on a weighted graph
- **`task_4.py`**: Converts a list/heap representation into a binary tree of nodes and visualizes the resulting binary heap
- **`task_5.py`**: Builds a binary tree from a heap list and visualizes traversal orders (DFS and BFS) using color gradients to show visit order
- **`task_6.py`**: Compares a greedy and a dynamic programming solution to maximize calories under a budget
- **`task_7.py`**: Runs a Monte Carlo simulation of two-dice rolls, prints a comparison table against theoretical probabilities, and plots results for large sample sizes

## Task 7: Summary

This project simulates the rolling of two 6-sided dice to determine the probability of each possible sum (from 2 to 12) using **Monte Carlo method**.

### Comparison

The table below compares the results obtained from a simulation of 1,000,000 rolls against the analytical expectations.

| Sum | Analytical Probability | Monte Carlo Result | Deviation |
|:---:|:----------------------:|:-------------------------:|:---------:|
|  2  | 2.78% (1/36)           | 2.78%                     | < 0.01%   |
|  3  | 5.56% (2/36)           | 5.55%                     | < 0.01%   |
|  4  | 8.33% (3/36)           | 8.34%                     | < 0.01%   |
|  5  | 11.11% (4/36)          | 11.12%                    | < 0.01%   |
|  6  | 13.89% (5/36)          | 13.88%                    | < 0.01%   |
|  7  | 16.67% (6/36)          | 16.66%                    | < 0.01%   |
|  8  | 13.89% (5/36)          | 13.90%                    | < 0.01%   |
|  9  | 11.11% (4/36)          | 11.10%                    | < 0.01%   |
| 10  | 8.33% (3/36)           | 8.33%                     | < 0.01%   |
| 11  | 5.56% (2/36)           | 5.57%                     | < 0.01%   |
| 12  | 2.78% (1/36)           | 2.77%                     | < 0.01%   |

### Conclusions

1. The Monte Carlo method proved to be highly accurate. With 1,000,000 iterations, the difference between the experimental and theoretical values was generally less than 0.01%
2. During testing with smaller numbers of rolls (e.g., 100 or 1,000), the results fluctuated significantly. However, as the number of experiments increased to 100,000 and 1,000,000, the probabilities stabilized and matched the theoretical table almost perfectly
