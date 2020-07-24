# Lecture 5 - Neural Networks

## Activation Functions
An activation function is a function applied to every unit on a given layer. It
can be seen as a functions that turns on or off in some ammount the value of
the unit (neuron), before it is passed to the next layer. Locally, in every
neuron, the process is as follows:

  receive_input_data      apply activation function --> pass value to next layer
          |                        / \
          |                         |
          V                         |
  apply the neuron weight --> apply a bias

Activations functions are largely studied since they are a key part of a neural
network training process, specially in the steps involving backpropagation.
Backpropagation is a process that is going to be computed for a big ammount of
times, thus it is important that an activation function (as well as its
derivative) are computed the fastest possible way.

### Threshold Functions
There are many types of activation functions, among the most common ones are
threshold functions and linear functions. A threshold function is also known as
a step function, since it has a big step between a value after the threshold
and one just before.

        ________
       |
       |
       |
-------

This sort of functions are good to binary classification problems, where only
two labels are enough to describe the problem. But for other, more complex,
problems, where more than two states (categories) are involved in the task,
this kind of functions result not that useful.

### Linear Functions
An alternative for those cases, are linear activation functions, which have the
form y = mx + b. This kind of functions allow the activation for multiple
values, which can be translated to the clasiffication of multiple labels. One
main disadvantage regarding linear functions, is that there is no capability to
do backpropagation during the training phase, this because backpropagation is
achieved by gradient descent, which requires the derivative of the activation
function, since surprisingly the equation of a linear functions is a LINE, its
derivative will end up being a constant, and this constant has no dependency on
the training data.

Another disadvantage of linear functions comes into picture in a neural network
that has only linear activations along all its layers, this is the inability of
analyzing more complex problems, this is because at the end, the values passed
to the output layer will only be a linear combination of the input layer, since
a linear combination of functions, is still a linear function. Thus, a neural
network with only linear activation functions acts as a linear regression
classifier.


### Non Linear Activation Functions
The last kind of activation functions are non linear functions, this category
of functions allow the analysis of complex, real world data, since not many
problems can be computed with linear regressions. The main benefits of these
functions are:
- The allow back propagation. The derivative of the function is another
function, which holds a relation with the input data.
- Useful for deep neural networks

## Examples

### ReLU (Rectified linear units)
This functions may seem as a linear function but it is not. It is important to
be aware of this fact because it states that ReLU allows backpropagation. In
its most basic form, ReLU behaves linearly for positive values, whereas for
negative ones, the become zero.

            ReLU = max(x, 0)

The next code tries to expose this behaviour:
```python
    from tensorflow.keras.activations import relu 
    import numpy as np
    a = np.array(([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]))
    relu(a).numpy()

    Out[8]: array([0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6])
```


## Resources
- https://missinglink.ai/guides/neural-network-concepts/7-types-neural-network-activation-functions-right/
