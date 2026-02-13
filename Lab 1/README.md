# Backward Chaining Engine for Rule-Based Systems

A backward chaining engine that recursively builds AND/OR goal trees from production rules with pattern-variable unification. Applied to family relationship inference and poker-hand transitivity.

## Implementation

### Rule Systems (`lab1.py`)

- A transitive rule for poker-hand ordering: `IF( AND('(?x) beats (?y)', '(?y) beats (?z)'), THEN('(?x) beats (?z)') )`
- 9 family relationship rules (same-identity, sibling, brother, sister, father, mother, son, daughter, cousin, grandparent) tested against the Simpsons family and the Harry Potter Black family tree

### Backward Chainer (`backchain.py`)

- `backchain_to_goal_tree(rules, hypothesis)` — recursively matches the hypothesis against rule consequents, builds an OR node of all matching rules, and recursively expands each antecedent into its own goal tree
- `rule_match_goal_tree(rule, hypothesis)` — attempts to unify a single rule's consequent with the hypothesis using pattern variables (`(?x)`, `(?y)`)
- `antecedents_goal_tree(rule, bindings)` — substitutes bindings into the rule's antecedents and recursively expands them
