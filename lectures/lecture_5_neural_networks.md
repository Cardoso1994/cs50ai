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
concept to our neural networks gives us an understanding about in which
directions the weights should be updated in order to minimize the loss function
the fastest way possible.

This is an iterative process, so in every iteration the weights of every edge
are modified in a little ammount in the direction specified by the gradient

There are many kinds of gradient descent algorithms, the original one computes
the gradient descent for ALL DATA POINTS in the data set, this kind of
algorithm can consume a lot of time since it works for every data point in
every iteration, because of that there might be other algorithm that might work
better for us. The first example is Stochastic Gradient Descent, in this form
of the algorithm we take one data point for every iteration to compute the
gradient, this is less exact but on the other hand works faster. A second
example is the Mini-Batch Gradient Descent which tries to give a balance
between the 2 previous methods, by selecting in every iteration a small batch
of the data points to comput the gradient.

### Multiple outputs
Until now, we have only talk about neural networks with one unit in the output
layer, but this is not a rigid fact, we can in fact have multiple outputs. This
is useful in for example classification tasks for more than two classes, it
also has been found useful in reinforcement learning, where each output unit
represents a given action from the set of actions available for a particular
state, and the value of every output unit specifies a value of how good an
action is.

A neural network with more than one output can be seen, and trained, as if
there were n(n == numer of outputs) independent neural networks, each one of
them with its particular edges and weights that connect the inputs with the
output.

### Deep Learning
So far, neural networks with two layers, one for inputs and one for outputs,
have been discussed. These neural networks work fine, but have some
limitations, for example in a classification task, say for example the weather
for a particular day, we might want to know if it is gonna be rainy or sunny, 
a neural network with only an input and output layers will only be able to
classify stuff when there is a linear boundary relation that separates the
groups of classification. This is analogous to the perceptron rule.

In conclussion, a neural network with just an output and input layer can only
work with linear relationships, which in turns, is not ideal since most data in
real world does not behave linearly. There might be for example, some data
where the boundaries are in form of circles.

In order to overcome this, deep neural networks were developed, the
particularity of DNN are that they have one or more hidden layers between the
input and output layers, giving us the ability to analyze more complex data.
This technique is commonly known as Deep Learning.

The basic idea is that in every hidden layer the neural network learns some
particular pattern(s) and delegates the rest of the work to the next layers.

#### Backpropagation
In deep learning the gradient descent algorithm is still a valid approach. But
it becomes a more complex problem, since every layer connects to the next one
with edges that come out of its units with a particular weight, so we have much
more weights to update. It is also important to remark that the loss function
is only computed for the output layer, which only gives us the ability to
update based on that information the weights of the last hidden layer.

Therefore it is necessary to found a way to update appropiately the weights
involved in the hidden layers, and this is where Backpropagation comes to
picture, it is a technique in which we try to compute wich percentage / amount
of the error comes from which unit on the previous layer, and keep doing the
same to the previous unit and so on, until we reach the input layer, this way
we can know which edges (for every layer) and in which ammount need to be
updated.

#### Overfitting
As we saw in the machine learning lecture (lecture 4), overfitting may become a
huge problem for our algorithms as they start to work with test data.
Overfitting is what happens when our model was trained to fit "very well" the
data set, which sometimes lead to a point where the AI is no longer available
to generalize its predictions to other data sets.

When working with neural networks, the way to prevent overfitting is via a
technique called DROPOUT that consists in dropping out some random units of the
neural network in every iteration and do the training process in that iteration
as if those dropped units weren't part of the network at all. At the next
iteration those units are restored and new randomly picked units are dropped
out, and so on. The general idea is that by dropping out units at random, we
eliminate the risk of relaying too much in one particular unit, which in turn
results in a better generalization of the neural network.

### Computer Vision
#### Image Convolution
- kernel
- feature map

#### Pooling
- max pooling

#### Convolutional Neural Networks


### Recurrent neural network
