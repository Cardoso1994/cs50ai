Lecture 0 - Search

### Concepts of the course
- Search
- Knowledge
- Uncertainty
- Learning
- Neural Networks
- Natural Language Processing


## Search Algorithms

### Agent
The agent is an entity that perceives its environment and acts in relation to
it.

### State
A configuration of the environment and the agent

### Initial State
As its name suggests, is the state that the environment has at the beginning of
the execution.


### Actions
choices that can be made. Are implemented as functions.
Action(s) return a set of possible choices to be made depending of the state.

### Transition model
Relation between states and actions. The state of the environment after an
action took place.


### Space State
The set of all the possible states that can be achieved based on a given
initial state, and a set of possible actions

### Node
A node is a data structure that contains all the necessary information about
the problem at a given state. It is, in general, formed by:
* A state. The state we are currently on.
* A parent node. This is the node that contains the state previous to the
    the current one.
* An action. This is the action taken to get from parent to node.
* A path cost. The cost that the action taken adds to the solution of the
    problem from the initial state.

## Pseudocode for Search in python. First Algorithm
```python
    add_initial_state_to_frontier()
    while True:
        if frontier_empty():
            return (no_solution)

        remove_node_from_frontier()
        if node_is_goal():
            return (node)

        expand_node()
        add_expanded_nodes_to_frontier()
```

In this case, we are not currently thinking in the way we are removing nodes
from the frontier. This varies depending on the algorithm, it could be depth
first search or breadth first search, among others.

## Pseudocode for Search in python. Second Algorithm
There are many inconvenients with the algorithm above, but one that may arise
very often is that when our nodes have 2 directions, this means that one can
go back and forth between two nodes. The best way to go around this situation
is to declare a so called **explored set**, this way we don't have to revisit a
state we have previously been on.

The pseudocode for this goes as:
```python
    add_initial_state_to_frontier()
    while True:
        if frontier_empty():
            return (no_solution)

        remove_node_from_frontier()
        if node_is_goal():
            return (node)

        add_to_frontier(node)
        expand_node()
        for node_ in expanded_nodes:
            if not node_ in_frontier and not node_ in explored:
                add_to_frontier(node_)
```

## Depth-First Search
This kind of search algorithm works with a **stack**, this kind of structure is
a last in first out structure, which means that we always remove from it the
last node appended.

The effect that it has on the solution is that it goes as deep a possible
finding a solution and when it reaches a dead point, it goes back to the
previous branching point and goes again as deep as possible, and so on, until
it finds a solution or traverses all possible paths without finding any
solution.

![DFS.jpg](resources/0476d2fef6fc481d8d77f0715a8d5faa.jpg)
Thsi picture shows a DFS visual example. We started from point A and
expanded B, from there we expanded C and D, decided to pick D and expanded
F. Since it was a dead end, we went back to the decision B in order to
pick C, and from there we will expand and find E.
The order of steps take can be seen in the "Explored Set".

## Breadth-First Search
This kind of search algorithm works with a **queue**, this structure is a first
in first out data structure. Acts like a line of people waiting to buy some
tool tickets.

Covers level by level, from one side to another. It expands until the
shallowest node of the level, then goes to the next level and so on.

![BFS.jpg](resources/38e0440ff07647a3982626025604cf6c.jpg)
In this picture we are trying to solve the same problem, but the essence on how we do it is a little bit different, we are
expanding all the nodes at the same level at the same time. In
this particular example we expanded A to find B, expanded B and found C and D, the we go to the next level and add to the fronier
E and F. In this example F won't be expanded as we found E before that happened. In the explored set it is visible the order of the
operations for the breadth first search algorithm.


## Comparison between DFS and BFS
DFS and BFS will always find a solution as long as the problem has a solution.

The main difference is that DFS may find a solution faster than BFS, but on the
other hand it may not be the optimal solution, as it will go deep into one
branch without considering other branches.
![DFS_not_opt.jpg](resources/7b6bf18064774c488fe62f3ef912142c.jpg)

BFS will find the optimal solution, as it explores the search tree one level at
a time looking for the solution, and going to the next level if needed. The
counterpart of this is that we will have some explored paths that lead us to
nowhere, so it may have a bigger computational cost.
![BFS_opt.jpg](resources/b3547ca2ed1640ecb5af6c2c5e186d74.jpg)

## Uninformed vs Informed Search
Until this point, we have only got into "uninformed" search algorithm. Both,
DFS and BFS are uninformed in the way that the code doesn't care about the
structure of the problem to be solved, the have no further information about it
other than the basic rules and the search tree. This will, the majority of
times, leave to an excess in computational time and space, since we will end up
looking through some paths that are not optimal.

On the other hand, informed search algorithms take into account some
"understanding" of the problem, some aspects that will make the algorithm to
make "better" choices whenever it finds itself in a decision point. They take
some specific knowledge of the problem.

In other words, in uninformed search algorithms the decisions are made
arbitrarily, there is no special reason in why the algorithm chose a particular
node instead of another one. This sometimes will lead to the exploration of
more paths and in the case of DFS maybe to find a not optimal solution.

Examples of informed search algorithms are:
- greedy best first search algorithm
- A* search

## Greedy best first search
This algorithm is similar in some way to DFS in the sense that when we pick
a node, it goes as deep as possible into it.

This algorithm shines against BFS and DFS in that it considers additional
information specific to the problem, so it can do a "conscious" pick on which
node to pick. For example if the problem is finding a path from point A to
point B, we should have a "heuristic" value that tells us for instance,
how far away of the goal is each of the nodes one can choose from. So if we
have two options, we should explore first the branch with the node of the
lower heuristic value.

![greedy_first.jpg](resources/8dda5c0681b84def90f18aa39df10bca.jpg)
Node in which we have to branches. According to the heuristic function it is best if we take the node with the heuristic value 11, since it is closer to the goal B.
![greedy_first_end.jpg](resources/1bc6d12004ac4008955a29f7ad20e600.jpg)

This algorithm is obviously an improvement, but it may take us to a no optimal
path, because it may pick a node that may seem that goes nearer than the
others but in the end it may be longer, and Greedy best first search has no
way to take this into account. This can be seen in the picture below where greedy finds a not optimal path
![greedy_first_not_opt.jpg](resources/2e31716b76c642e3aa5b6b8da7c63c49.jpg)

## A* search
In order to overcome the problems exposed with greedy best first search
we need to have in our power more information that helps us decide what the
best choice might be. In the same example of path finding, greedy only
considers the distance between the current point and the goal, whereas A*
considers also the cost to take to that point.

In the picture below we see that each node's value is the sum of two numbers, the first one is the cost (number of steps) that it takes to get there, and the other is the distance from there to the goal (as in greedy). At the beggining both algorithms took the same path since it has the lower value, but as it advances it there is a point when it gets more expensive to keep
going that way so it just goes back to the decision point and take the other branch.
![a*.jpg](resources/baf4fc624bfa443eaab72a554dde6466.jpg)

## Adversarial search
Search algorithms for games, or other problems when the actions to be taken depend on the decision made by and
adversary (or an external agent)
- minimax (adversarial search algorithm)
- Alpha Beta Pruning
- depth limited minimax

## minimax
This algorithm needs the game to have a final score, so it can decide the
movements to be made based on the score the application wants to
get. For example, in a tic tac toe (gato) game, we have three possible
outcomes, X wins (1), O wins (-1), and nobody wins (0), in other words, the
X player would want to MAXIMIZE the score, whereas the O player would want to
MINIMIZE the score.
![gato_scores.jpg](resources/ef98491df9064e13ad1e4b6cd14d626a.jpg)

So in order to make a decission, the functions used called each other
recursively so one can determine the possible outcome of the game after a
movement.

If the X player wants to maximize the score, it will have to look through all
possible movements and evaluate after that movement, what would the O player
do with the state given after the X play. The O player will want to minimize
the score, and for that it will check for possible movements of X after a
decission has been made. For all the possible movements it will check
the score of all the possible outcomes and pick de lowest score available,
backtracking to the original movement of X, X has to assume that in all
possible movements O will make the one that gives the lowest score, so X
should decide of all of this possible "lowest" values, the biggest since X's
job is to maximize the score.

![gato_tree.jpg](resources/1347fd1aa88646acba5969c06a6eca17.jpg)
In the picture above, it is the turn of the O player, which has 2 options, so
it evaluates the outcomes of each movement, based on what the X player would
do, this is to MAXIMIZE the score. The X player would make a score of 1 and 0
in each case, so the O player must pick the movement that only allows X to
get a score of 0, hence it is minimizing the score.
This tree could as well be a part of a bigger tree, where it is X player
that has to make a choice, and gets the minimum values from the O player, and
from this it will pick the biggest one.
![gato_tree_big.jpg](resources/062a00ad80004878aab47a4100874c9c.jpg)

## Alpha Beta pruning
The first CON that minimax shows is that it goes over every possibility, and
in many cases this will be a waste of memory and time. For example, a game that
has multiple final scores, it would make no sense to keep looking into a
branch of the tree if you already know that it cannot be a better outcome of
what you already have searched.

In the picture below, the green upwards arrows represent the player who
is trying to maximize the score, and the red downwars arrows the player that
is trying to minimize the score. So Green must have to pick a movement where
it can get the max value which is dependant on what Red would do, this is
MINIMIZE the score, taking the decision based on what would Green do next.
This picture represents the **minimax** algorithm.
As we can see, it goes over all the possible leaves of the tree.
![minimax_out.jpg](resources/249319b03d6f4c0283e09470d5425222.jpg)

A better aproach is to neglect all paths that we know in advance won't be
optimal. So in the example above, the biggest value is 4, so as soon as we get
a value lower that 4 we can stop searching that branch, since the Red
player will want to minimize the score, we know that that node will have a
score of, at most, 3 (for the second leaf), and so on. The image below shows
this logic and procedure in action. It can be seen that it will reduce
the computations needed and the result will be the same.

![alpha_beta.jpg](resources/d6d79f8070cb4eebb697aa67a2f40486.jpg)
Since the Green player wants to maximize the score, and this will depend on
the next moves of Red player, who is trying to minimize, whenever we
found a lower value than the maximum we already have, there is no need to keep
looking, because that node will be at most that new lower value which serves
of nothing to Red player.


## Depth Limited Minimax
Last but not least, there are games in which the total number of possible
outcomes is HUGE, and computers in some cases don't even have the
capabilities to simulate all of this computations. This is the need of a
depth limited approach, in which the algorithm only evaluates a certain
amount of computations, for example maybe 5 or 10 steps ahead, in order to
have a sense of what is gonna happen.
