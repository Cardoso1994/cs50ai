Lecture 3 - Optimization

# Optimization Problems
Choosing the best option out of a set of possible options.

A first approach to this kind of algorithms was first introduced in
adversarial search problems, where the AI has to pick its next movement based
on the set of possible movements it can make, based on the knowledge that it
has of what could the the best option might be in accordance of the goal set
for the AI.

## Local Search
It differs from other search algorithms such as BFS or DFS in the sense that
DFS and BFS explore multiple paths at once in order to get to a GOAL that is
previously known. In other words the GOAL is always known and the purpose of
the these algorithms is to find the optimal path to that GOAL.

On the other hand, Local Search algorithm is more suited to solve problems in
which we do not care at all about the path taken, but instead the heart of
the problem is to find the goal itself.

Local search algorithms are used for problems where we want to maximize or
minimize a solution. A simple example can be the optimal positions of two
hospitals in a particular city, in that case we shall want to minimize the
distance of all the houses in the city to one of the two hospitals. [This can
be done for example, with the MANHATTAN DISTANCE].

Usually the set of possible solutions can be represented in a "state-space
landscape", which is basically a bar graph in which each bar represents a
node (a particular solution) and its height represents the cost of that
solution.

In the case where we want to maximize the solution i.e. find a global
maximum, it is said that we want to **maximize an objective function**
whereas in the case where the solution is trying to be minized i.e. find a
global minimum, it is said that we want to **minimize a cost function**.

In general, in local search algorithms we stay in a current state, and move to
a neighbouring node in the "state-space landscape".

### Hill Climbing
Hill climbing is a type of algorithm for local search where given that we are
in a current node (or state), we next consider and compute the values of the
neighbouring states, and based on that values we pick the most convenient node
and move to it, making it now our new current state.

In cases where we want to maximize the objective function, hill climbing must
pick the node with the highest value and move to it, and keep going
recursively picking the highest neighbour until we find the peak, i.e. a state
where every of its neighbors has a lower value.

In cases where we want to minimize the cost fucntion the algorithms works in
the same manner but this time we are going to move to the node with the lowest
value instead. This will keep going on until we reach a valley, where all of
the neighbouring nodes have higher values.

```python
    function hill_climbing(problem):
        current = initial state of problem
        repeat:
            neighbor = highest valued neighbor of current
            if neighbor not better than current:
                return current

            current = neighbor
```

The main problem that we can have with Hill Climbing algorithm is that we may
end up in "local" maximums or minimums. This is because this kind of algorithm
just looks in the neighbors, so we will get stocked in a case where a node has
a higher value than its neighbors but there might be a global maximum that we
are not aware of, and we will not have a way to reach it because the algorithm
will stop in that local maximum. The same but in opposite direction is true for
local minimums.

There are some variants of the Hill climbing algorithm, and are listed in the
table below.

Variant             | Definition
------------------------------------------------------------------------------
steepes-ascent      | chooses highest valued neighbor
stochastic          | chooses randomly from the set of higher valued neighbors
first-choice        | choose the first higher values neighbor
random-restart      | conduct hill climbing multiple times
local beam search   | chooses the k-highest values neighbors


### Simulated Annealing
As we have seen, Hill Climbing algorithms have a particular issue which is the
possibility of getting stucked in local solutions. Simulated annealing comes to
picture to try to solve this problems, and its form of doing so is by having
the possibility of choosing from time to time a "worse" neighbor node. This
idea needs to be controlled in some manner, a first thing to take into
account is that the probability of getting a worse node should decrease as the
solutions advances, this is, it has to be more likely for the algorithm to
chose a worse neighbor in the early states, this is known as a state of High
Temperature, and as the time goes by the Temperature starts to decrease which
results in lower probability of getting a bad a node.

One more thing to take into account is that the probability of chosing a worse
neighbor should be a function of the temperature state (T), and the change in
the energy (deltaE). deltaE gives a numerical relation about how much better a
neighbor is with respect to another node.

```python
def SIMULATED_ANNEALING(problem, max):
    current = initial_state_of_problem
    for i in max:
        T = temperature(t)
        neighbor = random_neighbor_of_current
        deltaE = neighbor_with_respect_to_current
        if deltaE > 0:
            current = neighbor
        else:
            current = neighbor * probability(e ** (deltaE / T))
```


## Linear Programming
Until now, we have only talked about algorithms that can find a solution for
discrete states (many of them can be represented using graphs), but we may find
problems that require the manipulation of all of the real numbers, and this is
where Linear Programming comes into play, it is basically a technique which
uses Linear Algebra to solve the problem. It has 3 main aspects:

- Minimize a cost function
  - c1x1 + c2x2 + c3x3 + ... + cnxn
- constraints
  - a1x1 + a2x2 + ... + anxn <= b
  - a1x1 + a2x2 + ... + anxn = b
- bounds
  - li <= xi <= ui

This is, we have a problem which can be stated as a linear equation, then the
problem itsel gives us some constraints that need to be considered and we may
also have boundary limit values for the variables that are involved in the
problem.

Note that the constraints should always be expressed in the form of "less than"
or "less than or equal", in the case where we have a constraint with more than,
that constrinat should be multiplied by (-1) in order to present it into the
algorithm in the correct form.

Examples of this type of algorithms are:
- simplex
- Interior-Point


## Constraint-Satisfaction
- Set of variables {x1, x2, x3, ..., xn}
- set of domains for each variable {D1, D2, ..., Dn}
- set of constraints

A particular example example of this constraint-satisfaction problems is the
Sudoku game, in which the variables are all the cells in which one has to place
a value in order to solve the sudoku. The domains will be all the possible
values that a particular cell can take and finally the constraints will tell us
what values in the domain have to be neglected.

Keeping up with the sudo example:
- Variables {{0, 2}, {1, 1}, {1, 2}, ...}
- Domains {1, 2, 3, 4, 5, 6, 7, 8, 9}
- Constraints {{0, 2} != (1, 1) != (2, 0), ...}

It is worth noting that each variable will have its own particular set of
domain, at the beggining they may all look the same but as we dive deeper into
the solution the constraints will have the effect of updating the domains sets
since not all the constraints will apply to all variables.

There are two mainly kinds of constraints:
- Hard constraints: these are constraints that must be met.
- Soft constraints: these are constraints that express some sort of preference
    between options

We mostly deal with hard constraints which in turn, can be divided in two kinds
- Unary constraints: constraints that apply to one specific node
- Binary constraints: constraints that involve two variables of the problem,
    this kind of constraints are represented by an edge in a graph.

With these ideas in mind, a constraint satisfaction problem is reduced to be
solved by selecting a value from the domain set for a particular variable while
keeping the constraints in mind, and this can be achieved by making our graph
consisten. There are many kinds of consistency, the two explored in this course
are:
- Node consistency
- Arc consistency

### Node consistency
When we want to make our graph node consistent, we want to reduce our set of
domains to only those value which do not violate any Unary Constraint.

### Arc consistency
A graph is arc consistent when we reduce (for all variables) the set of domains
to those who do not violate any Binary Constraint.

For example, if we would want to make a node X arc consistent with respect to a
node Y, we want to reduce the domains set of X to only those values for which
there will be a valid value for Y, given the binary constraints that involve
both of the nodes.

### Backtracking Search
```python
def backtracking(assignment, csp):
    if assignment is complete:
        return assignment
    var = select_unassigned_var(assignment, csp)
    for value in domain_vlaues(var, assignment, csp):
        if value consisten with assignment:
            add(var, value) to assignment
            result = backtracking(assignment, csp)
            if result is succes:
                return result
        remove(var, value) from assignment
```

Backtracking is a search algorithm that tries to solve the problem by pincking a
variable and assigning a value from its domain to it, after that it then calls
itself recursively and this time it will assign a new value to a new variable
that hasn't been explored yet. It goes that way until we have nothing more to do
and the value assigned doesn't provide a solution, in which case we have go
"backtrack" and try a new value for the variable. In the other case, we finally
reach a solution which is in tur returned recursively to all the function calls
of backtracking until the main program itself.

Backtracking is a fine algorithm, though its performance can be improved via
several approaches, the first one is given a value assigned to a selected
variable we can make inferences on what values can be removed from the domains
of the rest of the varaibles by making the current node (assigned variable) arc
consistent, this in fact saves a considerable ammount of working by not
considering in advance cases that are forbidden by the constraints and the value
for the current node.

Other aspect that improves the performance of backtracking is to select the
"best" next variable possible, this in fact can be done in two ways:
- minimum remaining values (MRV): select the variable that has the smallest
    domain. This because there will be less paths to search.
- degree: select the variable with the highest degree. Take the degree as a
    value that expresses to how many nodes is a given node connected. This
    because modifying that particular node with the highest degree will
    propagate its results more abroad than the rest of the nodes.

The last aspect reviewed in this lecture is in reference to Domain values. We
will want to select the value that is the least constraining. This because we if
we chose a more constraining value, we might end up discarding a path that may
lead to a solution.
