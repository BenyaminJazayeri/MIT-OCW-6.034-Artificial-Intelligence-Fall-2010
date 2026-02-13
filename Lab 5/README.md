# Neural Network Backpropagation from Scratch

Forward propagation with sigmoid activation and backpropagation implementing the chain rule through multi-layer networks. Built progressively deeper architectures, from a single neuron to a 6-neuron, 3-layer network.

## Implementation

### Forward Propagation

- `Neuron.compute_output()` — computes the weighted sum of inputs and applies the sigmoid activation function: `1 / (1 + exp(-z))`

### Backpropagation

- `Neuron.compute_doutdx(elem)` — implements the chain rule with two cases: direct weight connections and descendant weight connections. Computes `output * (1 - output) * sum(downstream gradients)`, the sigmoid derivative multiplied by the upstream gradient

### Loss Function

- `PerformanceElem.output()` — squared error loss: `-0.5 * (output - desired)²`
- `PerformanceElem.dOutdX(elem)` — loss gradient: `(desired - output) * input.dOutdX(elem)`

### Network Architectures

- `make_neural_net_basic()` — single neuron with 2 inputs
- `make_neural_net_two_layer()` — 3 neurons (A, B feed into C), 2 layers
- `make_neural_net_challenging()` — 6 neurons (A, B, C → D, E → F), 3 layers

---

# AdaBoost Ensemble Classifier

An AdaBoost implementation with weighted voting, weight updates based on classification error, and best-classifier selection. Applied to congressional voting data.

## Implementation

- `BoostClassifier.classify()` — weighted vote of base classifiers, where each classifier's vote is weighted by its accuracy
- `BoostClassifier.update_weights()` — AdaBoost weight update rule: correctly classified points receive weight `0.5 / (1 - error)`, misclassified points receive weight `0.5 / error`
- `BoostClassifier.best_classifier()` — selects the base classifier whose error rate is farthest from 0.5 (most informative)
- `most_misclassified()` — returns data points sorted by their final AdaBoost weight, identifying the hardest examples
