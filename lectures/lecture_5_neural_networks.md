# Neural Networks

## Artificial Neural Networks
Artificial neural networks are data structures that try to emulate a human
neural networks, in other words, they are an attempt to copy the way our brain
works and thinks. A neural network can be represented graphically in a similar
manner as a graph, in which each node of the graph represents a neuron (more
technically, a unit), and units are joined together via edges, this represents
the connection between units.

The most basic neural network consists of multiple nodes on the input layer and
one node on the output layer. For example, and keeping continuity with the
previous lectures, one can create a neural network to predict if a day will be
sunny or rainy, depending on the variables of pressure and temperature for a
given day, this can be achieved with a network with two nodes in the input
layer (one for each variable of the problem), and one unit in the output layer,
a boolean value (1 or 0) that tells us wether the day will most likely be rainy
or sunny.

In this sense, a neural network can achieve the same results that the
algorithms discussed in the previous lecture, such as a classification task. As
it has been stated above, nodes are connected between them via edges, each edge
has a particular weight associated with it, this is analogous to the perceptron
rule, where each variable is multiplied by a weight (x1 · w1 + x2 · w2...) and
an additional weight w0 (also known as bias) is added, in order to get a
classification boundary. In the neural network each variable x is represented
by its own unit, and connected to the output layer with its associated weight,
the bias (w0) is added at the end directly to the output layer. Weights are
initially picked at random, and must be updated in order to get accurate
results. The most famous technique to update the weights is to perform a
gradient descent operation.

### Gradient Descent
In calculus, the gradient returns a vector with the direction of fastest
increase of a particular variable. By analizing it in the inverse manner we can
obtain the direction in which the decrease is the fastest. Applying this
concept to our neural networks understanding
- all data points vs stochastic gradient descent (one data point at a time) vs
    mini-batch gradient descent (small batch)

- multiple outputs
- multiple layers

- supervised learning, reinforcement learning
- perceptron (analogous to layers)

- backpropagation (piedra angular of neural networks)
- deep neural networks (deep learning)
- overfitting
    - dropout
