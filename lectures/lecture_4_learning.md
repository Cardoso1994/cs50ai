Lecture 4 - Learning

# Learning
In general, what is to be understood as learning (machine learning) in computer
science is the technique in which we no longer provide our computers with
a set of instructions to perform a task, but instead we provide them with a set
of "training" data, from which the computer will start to detect patterns and
make assumptions based on those patterns.

## Supervised Learning
Supervised learning is a technique in which the training data is labeled, in
other words we are telling the computer the right answer for each piece of
data we are passin to it, so it by itself can figure it out how the data is
related, what are the patterns that govern it.

### Classification
The simplest and most common example of supervised learning is the task of
classification. In this tasks we offer the AI a data set, a so called Training
Data, the training data is data that we know in advance its results, and it is
used by the computer to determine the similitudes and patterns that are in
common between data points with the same label. Once the AI has been trained,
we will be able to pass a data point to it, for which we do not know its label
and be confident of the result given by our program.

There are several types of algorithms developed to solve this kind of problems,
some of those are listed and explained below.

#### Nearest-neighbor classification
In the nearest-neighbor classification, the label given to the data point
received is assigned to be the same as the nearest neighboring point in the
data set.

Visually this can be seen as a plot (in 2D), where we plot the data points
given two parameters, now when we receive a new point, our goal is to place it
in the same graphic and assign its label to whatever label the nearest point
has.

#### k-nearest-neighbor calssification
One can easily spot a very common problem when applying the nearest neighbor
technique, it is the case when we have a point that is some sort of outliers,
in which case the nearest point may have a different label, thus assigning it
to the data point that is being analyzed which in turn, will result in the AI
giving erroneous results.

This can be solved by taking into account more points in order to make
predictions, and assigning to the data point the label that is more concurrent
between the K points selected.

The main problem that these algorithms have is that it is very time consuming
to iterate all the points in the data set when we are trying to find out which
ones are the nearest. There exist some data structures that help to make this
task faster, but it still is a factor to take into account.

#### linear regression
Another technique that can be applied is linear regression, if we continue the
plot example, we can find the equation for a line that divides our data set in
two, expecting to split it into the two labels. In a weather situation, for
example, this line could separate the data set between rainy and sunny days.
Rainny days would be on one side of the line, whereas sunny days would be on
the opposite side. There are many techniques available to find a line that
accomplishes this purpose, one of them is the perceptron learning rule.

#### perceptron learning rule
In order to understand this rule there are some parameters that need to be
defined. The idea of the perceptron rule is to have for each variable (in this
explanation 2) a weight that modifies each variable. In the weather example:
- x1 --> sunny
- x2 --> rainy
this is because we are assuming that there exist a function `f(x, x2)` that
matches exactly the data set labels, and with this technique we are defining a
function `h(x, x2)` (hypotheses function) which we are trying to get as close
as possible to the function f, this is accomplished by modifying the weights
of the equation.

    w0 + w1·x1 + w2 ·x2

the purpose of `w0` is to have an additional constant in order to be able to
move around the line. The equation above can be described as the dot product
of two vectors
    - weight vector:    (w0, w1, w2) = *w*
    - input vector:     ( 1, x1, x2) = *x*

The hypotheses function can then, be established as:
```python
                 1 if *w*·*x* >= 0
                /
    h(x1, x2) =
                \
                 0 otherwise

    h(x1, x2) = 1 if *w*·*x* >= 0 else 0
```

The key aspect here is how to determine the value of those weights, since a bad
assignment will lead to bad outcomes, and this is where perceptron learning
rule comes into play. This is a technique occupied to update the weights during
the training stage, this is done by

    wi = wi + alpha (y - h(x)) · xi
where
    - wi    -> weight for the ith variable ([left, updated], [right, current])
    - alpha -> amplification factor (how much we want to take into account the
                    the differences between the actual output [y] and the
                    hypotheses function result)
    - y     -> the actual label of the data point
    - h(x)  -> the value obtained from the hypotheses function for the given
                    data point

#### trheshold function (hard - soft)
What we have after the perceptron rule is a so called threshold function, that
can be plotted by placing in the `X` axis the dot product `w · x` and on the
`Y` axis the result of the hypotheses function (in our example, from 0 to 1).
In this particular case we will end up with a hard threshold function, since
we have a hard threshold value for which, everything before it has a value of 0
and as soon as we pass that threshold value, everything is labeled as 1.

A hard threshold function is hard to deal with, and in cases where we would
want to compute derivatives, it makes it even harder. Also there is no space
for certainty, it is 0 or 1 exclusively, there is no notion of confidence of
the output given. In order to overcome this, we may want to use a logistic
function, which in a plot would look like a soft curve, hence giving us a soft
threshold. Now we are able to get any real value between 0 and 1, which can be
interpreted as the probability of, for example, a day being sunny or rainy.

#### Support Vector Machines
Nevertheless, it turns out that there is a huge amount of lines that can be
obtained, and many of them would manage to separate (even exactly) the points
for each label, but there won't be an ideal fit in the moment of generalizing
and start to test the AI.

This is where support vector machines come in handy, they try to compute the
"maximum margin separator", which in easier terms means that we are trying to
maximize the vectors that describe the distance between the data point and our
threshold boundary. This means that we are trying to get a line that is the
furthest possible of the majority of the point while still making a good job in
separating the labels.

Support vector machines can work in higher dimenssions, for which these
algorithms are not limited to a line boundary, they can achieve different forms
in order to separate the different labels.

### Regression
There are cases when we don't want lo label a reuslt as a discrete value
(label), but we might want to map our function to a real number, for example if
we want to make predictions of how many sales a company does depending on how
much it spends on advertising.

This can be done by drawing a line that is the closest to all the points of the
data set, for example. This is not limited to one or two dimensions, hence it
can work with many variables.

### Evaluation Hypotheses
Now, after understanding the main goals and processes of Machine Learning, we
need to define a way in which to compute how good our hypotheses function
performs, this is done with a loss function. There are many loss functions
available for us to use, the most common are listed below
- 0-1 loss function
- L1 loss
- L2 loss

#### 0-1 loss function
This is a very straightforward way of evaluating the performance of the AI,
whenever we assign a label erroneously we say that it has a cost of one, on the
other hand if we assign the label correctly the cost is zero, in the end the
cost of the loss function for each point are added together and what we get is
the result of the 0-1 loss function.

#### L1 loss
This scheme shines against 0-1 loss function in that it has the ability to tell
how good the prediction was, how far it was from the actual value. This is good
in cases like the company advertising-sales example, since we do not have
labels but real values.

```python
    L1 = sum(|y - h|) for each point
```

#### L2 loss
Similar to L1, but the worse the prediction, the more it is penalized, this is
achieved by squaring the difference of the actual value and the prediction.

```python
    L2 = sum((y - h) ** 2) for each point
```

### Overfitting
Overfitting is a very common issue in machine learning, this happens as its
name suggest, when we are forcing our model to fit too exactly our training
data, which might lead to the scenario where we cannot longer generalize to
data that was not in the training data.

This can be taken into account via the cost of the function, which is nothing
more than the sum of the loss function and some assigned value for the
complexity of the model, with this we are now able to penalize a more complex
model (this is good since we want to avoid overfitting).

```python
    cost(h) = loss(h) + lambda · complexity(h)
```
where `lambda` is a constant that the programmer assigns and influences in how
much we penalize the complexity of the model. This is known as regularization.

#### Holdout cross validation and k-fold cross validation
An approach that will let us know how well is the generalization of our model
to future data sets that the AI hasn't seen is the holdout cross validation
technique, in which we separate our entire data set in two sets, one training
set and one testing set. The main problem with this approach is that we are
neglecting from the training process data that might be useful in this part of
the problem.

And for that reason, the k-fold validation technique was born, the logic of
this is to separate a much smaller part of the set, and make a holdout cross
validation, and then repeat this action k number of times with different
trainting and testing data sets. For example we can divide our data set in
10(k) parts, do the training with 9 of these parts and test with the last set,
then we select another part as the testing set and repeat the process, and so
on, for 10 (k) times.

## Reinforcement Learning
Reinforcement learning is another paradigm in machine learning, this one
differs from classification tasks because in this kind of paradigm the computer
isn't provided with any labels, instead the provide the model with a set of
instructions, a set of actions it can perform. Every time the AI performs a
movement based on this set of instructions it should receive some sort of
"reward", which in turn will help the AI to "learn", since the algorithm will
be based on maximizing the reward.

This can be seen as an agent (the AI) that is inmerse in an environment, this
environment provides a state for the agent, the AI then, based on the state
that has been passed to it, will perform an action from the set of actions
available, and after that the enviroment will return to the agent, a new state
after the given action has taken place and a reward (or punishment) that
results from taking that action.

Reinforcement learning is primarily applied in games, for example.

### Markov Decision Process
The agent has the ability to chose from a set of actions, each of those actions
might have associated with it a probability distribution (as in Markov chains)
to end up in a different state. Also it has a associated with it a reward of
punishment.

A Markov Decision Process is formed by
- Set of states S
- set of actions `actions(s)`
- Transition model `P(s' | s, a)`
- Reward function `R(s, a, s')`

### Q-learning
Q-learning is a reinforcement learning algorithm that determines the value of
a function `Q(s,a)` which evaluates the performance (via rewards or
punishments) of the action taken (a) in a given states (s), and based on that
knowledge inferred from the Q function, the agent can sort of understand its
environment and start taking better actions.

```python
    for all(s, a) -> Q(s, a) = 0
    when action is taken:
        estimate the value of Q(s, a) based on current reward and expected \
            rewards
        update Q(s, a) to take into account old and new estimates
```
The above pseudocode states that we must consider, for any given pair of
action-state that the initial Q values is zero, this is analogous as saying
"We do not know anything about the environment". Then, an action must be taken,
giving us a new reward, at this point we may want to go further an take more
actions after the initial one, and keep receiving rewards whihch will be added
to the current reward, this approach is a way to help us look into the future
of the path that is being taken. After all the new actions an rewards have
taken place, the value of the function Q must be updated, by adding to whatever
value Q already has, the new rewards that have been collected.
```python
    Q(s, a) <- Q(s, a) + alpha (new_estimate - old_estimate)
```
where `alpha` represents how much we value new estimates (high alpha) or how
much we value old estimates (low alpha). When `alpha == 0` it means that we
only value old information, whereas when `alpha == 1` we are only going to
consider new estimates.

### Exploration vs Exploitation
The last equation above gives enter to a very common issue in reinforcement
learning, exploration refers to the fact of not taking into account the new
rewards in the time of taking a new action, since we want to explore the
environment, on the other hand exploitation refers to the fact when we are only
considering the knowledge the system already has, and exploiting it in order to
get the (at the moment) best outcome possible. When training a model, the
programmer must balance its model between this two techniques.

When in the initial stages of the model training we may want to give preference
to exploration, but in latter stages, we would prefer to give more weight to
exploitation.

### Epsilon-greedy
Epsilon-greedy algorithm is a way to take into account the balance between
exploration vs exploitation, it is based on the logic that from time to time we
would want to make a random movement, instead of performing the best action
available in our knowledge base. This is useful since there will be times when
we know a particular set of actions direct us to a good outcome, but there
might be a better solution out there of which we do not know about, and then,
by taking random actions we can discover it.

Epsilon is a probability factor, whenever we want to perform an action, we will
do it with `(1 - epsilon)` probability of exploiting our knowledge base, and
we will take a random movement with probability `epsilon`.

### function approximation
Similar to minimax with depth limit. There will be cases (for example chess or
go) where computing the values of all Q for all combinations of state-action
is a waste of computational resources, if not impossible, in these cases we
will want to approximate what the outcome, and hence the reward, will be of
taking a particular action.

## Unsupervised Learning
Unsupervised Learning refers to techniques used in cases when there is no
information available (like labels, or rewards) for the data being analyzed by
the model. So it is the goal of the AI to detect and return some insight about
the given data.

### Clustering
One of the most basic techniques of unsupervised learning is clustering, in
this technique what we want is to separate the data in different clusters or
categories

#### k-means clustering
k-means clustering is an algorithm which divides the data into `k` different
clusters. Its operation works as follows
```python
    choose random positions for the centers of the clusters
    while (convergence_criteria):
        assign each point to the cluster which center is the nearest
        move the centers of the cluster to the mean of all the points that
            belong to the cluster at that particular moment
```

As we can see, this algorithm is an iterative process.
