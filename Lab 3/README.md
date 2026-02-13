# Minimax with Alpha-Beta Pruning for Connect Four

An adversarial game search engine using negamax-style alpha-beta pruning that prunes the game tree by maintaining alpha/beta bounds.

## Implementation

### Game Search (`lab3.py`)

- `alpha_beta_search(board, depth, eval_fn, ...)` — minimax search with alpha-beta pruning using a negamax formulation. At each recursion level, alpha and beta bounds are swapped and negated, exploiting the zero-sum property of the game. Prunes branches that cannot improve on the current best
- `focused_evaluate(board)` — evaluation function that scores boards by the difference in longest chain length between players

### Testing Infrastructure (`tree_searcher.py`)

Provides static game tree structures for verifying alpha-beta correctness independently of the Connect Four game logic.
