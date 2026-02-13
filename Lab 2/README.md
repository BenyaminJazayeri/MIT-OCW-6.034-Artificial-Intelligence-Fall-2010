# Search Algorithm Suite: BFS, DFS, Hill Climbing, Beam, Branch & Bound, A*

A complete implementation of the major graph search algorithms, covering the full uninformed-to-informed search taxonomy. Also includes functions to verify heuristic admissibility and consistency.

## Implementation

### Search Algorithms

- `bfs(graph, start, goal)` — breadth-first search using a FIFO queue of paths
- `dfs(graph, start, goal)` — depth-first search using a LIFO stack of paths
- `hill_climbing(graph, start, goal)` — greedy search that sorts neighbors by heuristic distance to goal, always expanding the most promising node
- `beam_search(graph, start, goal, beam_width)` — beam search with configurable width, keeping only the best `beam_width` partial paths at each level
- `branch_and_bound(graph, start, goal)` — optimal search without heuristic, sorting the agenda by cumulative path cost
- `a_star(graph, start, goal)` — A* search sorting by cumulative cost plus heuristic estimate, with an extended list (closed set) to avoid revisiting nodes

### Utilities

- `path_length(graph, path)` — computes total edge weight along a path
- `is_admissible(graph, goal)` — checks that the heuristic never overestimates the true shortest-path cost to the goal for any node
- `is_consistent(graph, goal)` — checks the triangle inequality: for every edge (u, v), `h(u) ≤ cost(u, v) + h(v)`
