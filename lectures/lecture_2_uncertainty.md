Lecture 2 - Uncertainty

**In this particular lecture the python module used is pomegranate**

## Bayesian Networks
A bayesian network is just a Graph structure that represents a particular
random variable as a node of the graph, and the relations between variables are
represented with arrows where an arrow from X to Y means that X is a parent of
Y.

    X ---> Y
    X is a parent of Y

This is an important relationship, because in a bayesian network we will often
have conditional probabilities for our random variables.

    P(X | Parents(X))

which gives us the probability of X happening, given that we already have in
our posession  some evidence about the parents nodes of X.

The whole idea of a bayesian network is that once we have created the network
and provided all the probability distributions, we can start to make
predictions about the possible status of a variable, or maybe we would want to
know the probability of a combination of events happening.

This process is done via Inference by Enumeration, in which we compute the
conjuction probability of all the random variables in our bayesian network. The
Inference by Enumeration is a technique to compute the probability of, for
example P(X | e) is computed as:

    P(X | e) = alpha * P(X, e) = alpha * SUM_OF (P(X, e, y))

    where:
    - X is the query
    - e is the evidence we already know
    - y ranges over values of hidden variables
    - alpha is a normalization variable (makes all to add up to 1)

The hidden variables are all those variables that are not explicitely stated in
the query X, but are part of the bayesian network and hence, the distribution
probability for that query needs to take into account the effect of those 
hidden variables in our final probability distribution.

In an example where a bayesian network takes into account:
- P(rain) --> Probability of rain (none, light, heavy)
- P(track_maintenance) --> Maintenace of rails of train (yes, no)
- P(train_delayed) --> Train_delayed (on_time, delayed)
- P(appointment) --> You made it to the appointment (true, false)

            ---P(rain)----
            |            |
            |            |
            |            |
            V            |
      P(maintenance)     |
            |            |
            |            |
            --------------
                   |
                   |
                   V
            P(train_delayed)
                   |
                   V
             P(appointment)

Given this bayesian network we might want to know the probability of having:
- rain: none
- track_maintenance: no
- train_delayed: on_time
- appointment: false

In this particular case we are only to compute the probability of this
particular series of events happen.

In other cases, we would want to predict the probabilities of the random
variables, given some evidence that we already know about the state of one or
more nodes in the bayesian network. For example, we can obtain the probability
of the random variables given that we know for a fact that the train is
delayed, this is, given some evidence.

An example of a case where we will have a hidden variable (in the network
above) is if we would want to compute:

    P(Appointment | light ^ no)

this is, the probability of making it to the appointment given that there is
light rain and no track maintenance. In this case the hidden variable is
train_delayed, and it in fact needs to be computed since it is the Parent Node
of the variable Appointment, this is done via Inference by enumeration, and
we must compute all the conjuction probabilities for all the possible states
that the random variable train_delayed can have.

### Approximate Inference
Inference by enumeration, as estated above is a technique in which every
conjuction probability needed for predictions needs to be computed, which in
the long term will cause an unnecessary use of time and computational resources
because in many cases we will find ourselves computing the same probabilities
multiple times.

This problem was first solved by approximate inference methods, in this
approach the program will first compute as much samples as required of
different probability distributions, in each sample we will start at the root
of the graph and start sampling by randomly selecting one of the possible
states for the corresponding random variable, then we need to continue the road
of the graph and compute the conjunction probabilities for the next random
variables by randomly selecting between the possible values that take into
account the states previously selected for the parents nodes.

Whith this in mind, now every time we will want to make predictions our program
only needs to gather all samples that fits the evidence that has been passed
into the program. Once the samples are gathered the prediction probability is
computed by dividing the ammount of samples that fits the prediction by the 
total ammount of samples that fit the evidence.

For example, having the same bayesian network as above, if we have:
- 10 sammples
- 8 samples resulted in the train on time

the probability P(train_delayed = on_time) would be:
        P(train_delayed = on_time) = 8 / 10

This is also true for conditional probabilities, where we must first gather all
the samples that fit the evidence, and then divide the ammount of them that fit
the criteria we want. For example, to compute
P(train_delayed = on_time | rain = light) we first gather all the samples where
rain = light holds true, and the we check if in those, how many result in a
train being delayed.

It is worth to say that this is NOT and EXACT METHOD, it only gives
approximations, but in many case this approximation is enough.

### Likelihood Weighting
Very small section, check video:
- [Lecture 2](https://youtu.be/D8RRq3TbtHU?t=5367)


## Markov Chains
This concept should be used when we want to compute the probability of
something happening given a time lapse.

Markov Chains are based on the Markov Assumption, this states that the current
state only depends on a fixed number of previous states. A Markov Chains then,
is a sequence of random variables where the distribution of each variable
follows that Markov Assumption.

One example might be the weather, for example we assume that tomorrow's weather
only depends on today's weather. This gives place to a Transition Model, which
tells us how we might transition from one state to the next, its visualization
can be seen as a matrix

|          | Sunny_t+1 | Rainny_t+1 |
|----------|-----------|------------|
| Sunny_t  |    0.8    |    0.2     |
| Rainny_t |    0.3    |    0.7     |


Predictions via Markov Chains depend on knowing the actual state of some point,
so with that information we will have what is needed to make predictions about
the future. For example, if we want to know the weather in 5 days, we must know
the state of the weather for today, and with this information and a defined
transition model we can start to make predictions.

This won't always be the case, a particular machine may not have access to the
real state of interest, but it might have access to some other data that is
related to the actual state, which will help us make conclussions.

| Hidden State     | Observation          |
|------------------|----------------------|
| robot's position | robot's sensor data  |
| words spoken     | audio waveform       |
| user engagement  | web or app analytics |
| weather          | umbrella             |


This gives plave to a Hidden Markov Model, and appart of the actual transition
model, in this lecture the weather, there's a need to have a Hidden Transition
Model, which gives us a probability distribution of what the actual state might
be, given the observations made.

|          | Umbrella_yes | Umbrella_no |
|----------|--------------|-------------|
| Sunny_t  |      0.2     |      0.8    |
| Rainny_t |      0.9     |      0.1    |

The table above is the Hidden (Sensor) Transition Model for the original
transition model for weather, and it tells us the probability of being sunny or
rainny TODAY, given the fact that we observed if people brought an umbrella or
not to the space that we have access to.
