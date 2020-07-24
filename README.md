# cs50ai
Projects of CS50 introduction to atificial intellingence with python

## Lecture 0 - Search
Search algorithms explained

### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/0/)

### Related Notes
[Lecture 0 - Search](./lectures/lecture_0_search.md)

### Related problem sets
- Degrees
- Tic-Tac-Toe

#### Degrees
- [Degrees source code](./degrees)
- [Degrees project](https://cs50.harvard.edu/ai/2020/projects/0/degrees/)


Based on the "Six Degrees of Kevin Bacon" which states that any hollywood actor
can be connected to Kevin Bacon within a chain of six movies.

This project finds the shortest path between two actor of a data base, and the
condition is that they have to be connected in between by Kevin Bacon.

This implementents a BFS search algorithm which is suitable for cases where the
shortest path is key

#### Tic-Tac-Toe
- [Tic-Tac-Toe source code](./tictactoe)
- [Tic-Tac-Toe project](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)


Implements a minimax algorithm to play the classic
Tic-Tac-Toe game against an AI.

The minimax algorithm has no depth limit because the game does not have many
branches


## Lecture 1 - Knowledge
Knowledge based algorithms based on propositional logic as well as first
order logic

### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/1/)

### Related Notes
[Lecture 1 - Knowledge](./lectures/lecture_1_knowledge.md)

### Related problem sets
- Knights
- Minesweeper

#### Knights
- [Knights source code](./knights)
- [Knights project](https://cs50.harvard.edu/ai/2020/projects/1/knights/)

Solves puzzles via propositional logic. It is a game in which each character
can be either a Knight or a Knave. A knight always tells the TRUTH whereas a
knave always lies.

The point is that for the AI to find out who is a Knight and who is a Knave,
based on the rules of the game, as well as the sentences that each character
"says", this sentences must be expressed in terms of propositional logic.

#### Minesweeper
- [Minesweeper source code](./minsweeper)
- [Minesweeper project](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/)

An AI must be capable of playing the minesweeper game, an ideally winning.
The "knowledge" obtained in every move comes from the rules of the games, in
which each cell discovered yells a number that represents how many mines are in
the neighbouring cells.

The AI then, saves information about the neighbouring cells represented in a
sum, where the sum of all the cells is equal to the value given by the
discovered cell. As the game goes by, the AI must be capable of produce NEW
KNOWLEDGE based on previous and recently discovered knowledge.


## Lecture 2 - Uncertainty
Algorithms based on probability. Bayesian Networks as well as Markov Chains.
Revision of probability concepts such as:
- Conditional Probability
- Unconditional Probability
- Baye's Theorem
- Joint Probability

### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/2/)

### Related Notes
- [Lecture 2 - Probability](./lectures/lecture_1_probability.md)
- [Lecture 2 - Uncertainty](./lectures/lecture_1_uncertainty.md)

### Related problem sets
- PageRank
- Heredity

#### PageRank
- [PageRank source code](./pagerank)
- [PageRank project](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/)

Uses google's PageRank algorithm to determine which page is more valuable than
the others given a set of web pages. In this case the `importance` of a
particular website has a value between `0` and `1`, and this result is analogous of
thinking about the probability of a given user ending up on a certain site.

It has two approaches, it is solved via a Markov Chain for `n` given states. It
can also be solved with an iterative process that ends when certain convergence
criteria is met, for example, when the values of importance for each page
changes in no more that `0.02` in relation with those of the previous
iteration.

#### Heredity
- [Heredity source code](./heredity)
- [Heredity project](https://cs50.harvard.edu/ai/2020/projects/2/heredity/)

Computes the likelihood of a person having a particular genetic trait by
stablishing a bayesian network that contains the relationships between family
members, the unconditional probabilities of having a particular gene, the
conditional probabilities of having the trait given that a person has `n`
copies of the gene. And the probabilities of passing a bad gene to a child
given that a person has `n` copies of the gene.

## Lecture 3 - Optimization
Algorithms:
- Local search
- Constraint satisfaction problems
- Backtracking

### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/3/)


### Related Notes
- [Lecture 3 - Optimization](./lectures/lecture_3_optimization.md)

### Related problem sets
- Crossword

### Crossword
- [Crossword source code](./crossword)
- [Crossword project](https://cs50.harvard.edu/ai/2020/projects/3/crossword/)

## Lecture 4 - Learning
Algorithms:
- Supervised Learning
    - Nearest Neighbor classification
    - k-nearest neighbor classification
    - linear regression
    - perceptron learning rule
    - support vector machines
    - Evaluation Hypotheses
        - 0-1 loss function
        - l1 loss function
        - l2 loss function
    - Validation
        - Holdout cross validation
        - k-fold cross validation
    - Reinforcement Learning
      - Markov decision chains
      - Q-learning
      - epsilon greedy
- Unsupervised Learning
    - Clustering
        - k-means clustering


### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/4/)


### Related Notes
- [Lecture 4 - Learning](./lectures/lecture_4_learning.md)

### Related problem sets
- Shopping
- Nim

### Shopping
- [Shopping source code](./shopping)
- [Shopping project](https://cs50.harvard.edu/ai/2020/projects/4/shopping/)

### Nim
- [Nim source code](./nim)
- [Nim project](https://cs50.harvard.edu/ai/2020/projects/4/nim/)

## Lecture 5 - Neural Networks
Algorithms:
- Articial Neural Networks
- Gradient Descent
- Deep Learning
- Backpropagation
- Convolutional Neural Networks (computer vision)
- Recurrent Neural Networks

### CS50 Resources
- [Whole Resources](https://cs50.harvard.edu/ai/2020/weeks/5/)

### Related Notes
- [Lecture 5 - Neural Networks](./lectures/lecture_5/neural_networks.md)
- [Lecture 5 - Convolution and Pooling](./lectures/lecture_5/convolution_pooling.md)
- [Lecture 5 - Activation Functions](./lectures/lecture_5/activation_functions.md)

### Related problem sets
- Traffic

### Shopping
- [Traffic source code](./traffic)
- [Traffic project](https://cs50.harvard.edu/ai/2020/projects/5/traffic/)

