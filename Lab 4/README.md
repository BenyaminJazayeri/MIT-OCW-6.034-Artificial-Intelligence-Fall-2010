# Constraint Satisfaction with Forward Checking and Propagation

CSP solver enhancements with forward checking and BFS-style singleton domain propagation that prunes variable domains after each assignment.

## Implementation

- `forward_checking(state)` — after each variable assignment, prunes the domains of all unassigned neighboring variables by removing values inconsistent with the assignment. Returns False immediately if any domain becomes empty, triggering backtracking
- `forward_checking_prop_singleton(state)` — extends forward checking with singleton propagation. When a variable's domain is reduced to a single value, that constraint is propagated to its neighbors in a BFS-style loop. Uses a visited set to avoid infinite propagation cycles

---

# k-Nearest Neighbors and Information Entropy

k-NN classification using Hamming and Euclidean distance, and a Shannon information entropy function for decision tree split quality. Applied to congressional voting records.

## Implementation

- `euclidean_distance(list1, list2)` — standard L2 distance for k-NN classification
- `information_disorder(yes, no)` — entropy-based split quality metric using Shannon information theory (`-p * log2(p)`), measuring the weighted average disorder of a binary partition
- `limited_house_classifier` — tuned k-NN parameters: N=44 for classifying 430+ House representatives, N=67 for 90+ senators, N=23 for 95+ previous-year senators
- `my_classifier` — nearest neighbor classifier using Hamming distance (k=1)
