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

#### Realted problem sets
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
