Lecture 1 - Knowledge

This week's lecture focuses in "knowledge based agents"

Main topics are:
- Propositional Logic
- First order logic

## Propositional Logic
Based on the logic of propositions

### Propositional symbols
Each symbol represents a "sentence" in human language. Symbols are represented
as upper case letter, for example P, Q, R.

A symbol in propositional logic can only have one of two values, these values
are:
- TRUE (1)
- FALSE (0)

And their meanning is the same as it is in English or any other language

But having those symbols is not enough, we need a certain way to connect these
ideas, the symbols in order to construct bigger ideas, to reason in a more
complex manner.

### Logical connectives
Logical connectives are operators, these operators connect propositional
symbols in order to get a bigger picture of the world those symbols represent.

The main logical connectives (although there are more of them) are:
- not (¬)
- and (^)
- or  (v)
- implication (->)
- biconditional (<->)

Each one of these connectives affects a symbol (or a group of symbols) in its
own way. If we want to understand how they affect the logic of the statement,
we first need to dig in in their truth tables. The truth tables are tables that
tell us the result of applying each of the connectives to a symbol (or group
of).

#### NOT (¬)
The not connective is a negation, a complete change of meanning, and it is
applied and understood as in human language. That means that it something is
TRUE, the "NOT that something" is false.

For Example: P: Humans are intelligent. --> TRUE

Then: Not P (¬P) ---> False

The truth table for the NOT connective is

P | ¬P
------
true | false
flase | true

The table only contains 2 rows because the NOT connective applies to only one
symbol, and each symbol can only have two possible states.


### AND (^)
The AND connective works with at least two symbols. In this section it is
analyzed with two symbols.

The AND connective indicates if the symbols implied in the statement are true.
It works the same way as in human language, so in order to get TRUE from an AND
connective, both symbols must be TRUE, otherwise AND will return FALSE.

Its truth table is as follows

P | Q | P ^ Q
-------------
true | true | true
true | false | false
false | true | false
false | false | false

### OR (v)
The OR connective works with at least two symbols. In this section it is
analyzed with two symbols.

The OR connective evaluates whether one of the two operators is true, if this is
the case it return TRUE, otherwise it returns false.

The truth table for the OR connective is

P | Q | P v Q
-------------
true | false | true
true | true | true
false | true | true
false | false | false

### Implication (->)
The implication connective is almost the same as in English.
Something implies another statement.
It is difficult to get this idea right since it can only be FALSE when the
second symbol is FALSE and the first one is TRUE.

In english it could be represented as "if ... then ...". An easier way to get
this right is in thinking of implication as a promise, for example
"If it is sunny, i will use suncream". Here the promise is that "i will use
suncream", the only way that i could lie to someone (and hence it will be 
FALSE) is the case whe it is in fact sunny but i don't use suncream. In the
case that it is not sunny it doesn't matter whether i use suncream or no, since
my promise was based on the fact of a suny day, hence it will return TRUE,
because there is no broken promise.

The implication truth table is as follows

P | Q | P -> Q
--------------
true | true | true
true | false | false
false | true | true
false | false | true

### Biconditional (<->)
A condition that goes in both directions, it can be read as a
"if and only if" statement.

This connective only evaluates to TRUE when P and Q are both the
same.

An example of this could be the phrase:
"if and only if it is raining, i will be indoors".
In this case it is easy to say that if it is raining, i will be indoors.
But it is also safe to assume that if i am indoors, it is raining.

The Biconditional truth table looks like

P | Q | P -> Q
--------------
true | true | true
true | false | false
false | true | false
false | false | true

## Model
A model assigns a truth value (TRUE or FALSE) to a pair of symbols, in order
to do this, a "knowledge base is needed".

A knowledge can be seen as a set of sentences that we know in advance if they
are TRUE or FALSE

### Entailment ⊨
If we read P ⊨ Q, this means that in every model where P is TRUE, then Q is
also TRUE.


## Model Checking Algorithm
We want to determine if KB ⊨ A (knowledge base [KB] entails A), and in order to
do that, we need to check every model in which our knowledge base holds TRUE
and check if A is also TRUE, if that is the case, we can conclude that KB
ENTAILS A, otherwise it does not entail A.

One problem of model checking will become more and more obvius as soon as the
knowledge base starts to grow, and this is the execution time grows
exponentially, since the number of possible worlds that model check will look
through in order to see if the knowledge base entails A is in the order of
2^n.

Remember that Model Checking algorithm needs to check all possible worlds in
order to determine in which of those worlds the knowledge base holds TRUE and
then it will check if also A holds true.


## Inference Rules
Is the process of determining new knowledge based of previous knowledge we
already have.

### Modus Ponens
If we have the query "a -> b" (a implies b), and we know that a is TRUE, then
it is safe to conclude that b is also TRUE.

### And Elimination
If we have a proposition "a ^ b" (a and b) and it is in fact TRUE, then we
know for a fact that a is TRUE, and that B is TRUE, each by their own.

### Double Negation Elimination
If we have a double negation, we can remove them from the query and keep with
the original values of the symbol.

¬(¬A) then we can conclude A. (if not not A, is the same as A). The first
not (¬) turns everything to false, whereas the second not(¬) returns everuthing
to TRUE.

### Implication Elimination
It is a formal manner to change implication (->, if ... then ...) to or
statements.

For example the phrase: "If it is raining, then Marco is inside", can be
expressed in other way without losing meaning, "it is not raining or Marco is
inside".

More formaly, 

    (A -> B) can be converted to (¬A v B)

### Biconditional
As its names suggests it is a condition in both directions, that can be written
as

    A <-> B
    then
    (A -> B) ^ (B -> A)

### De Morgan's Law
De Morgan's Law is used to turn an ^ (AND) into an v (OR)

    ¬(A ^ B)
    changes to
    ¬A v ¬B

It can also go in the other direction

    ¬(A v B)
    changes to
    ¬A ^ ¬B

### Distributive Law
The operators can be distribued in a similar fashion than they do in math.

    (A ^ (B v C))
    changes to
    (A ^ B) v (A ^ C)

    in the same way
    (A v (B ^ C))
    changes to
    (A v B) ^ (A v C)

## Conjuction Normal Form
A conjuction is what happens when someone joins two clauses with an ^ (AND)
operator. A clause can be a symbol, a ¬symbol, or a group of many of them.
This can be achieved via the application of the inference rules described
above.

The process to convert a logic formula to a conjuction normal form:
- eliminate Biconditionals
- eliminate Implications
- move all ¬ symbols inwards, so the only affect a particular symbol
    (De Morgan's)

For example:
- (P v Q) -> R turns into ¬(P v Q) v R
- ¬(P v Q) v R turns into (¬P ^ ¬Q) v R
- (¬P ^ ¬Q) v R turns into (finally) (¬P v R) ^ (¬Q v R)

**(¬P v R) ^ (¬Q v R)** is the conjuctive normal form

## Inference by Resolution
All the inference rules described above are of use in the inference by
resolution algorithm, this algorithm tries to solve a knowledge base problem in
the oposite direction that Model Checking goes, this is, while Model checking
checks every posible world to see if KB entails A, this algorithm checks if
(KB ^ A) is a contradiction.

A contradiction is what happens when we have for exmaple P and ¬P, this is a
contradiction since there is no posible way in which both can hold true.
Whenever this happens the result is an empty clause "()", and this always
evaluates to false.

This is important because the way that Inference by resolution works to see if
something (a query) is TRUE, is by first making it FALSE and probe that it is
in fact a contradiction.

The whole process, or algorithm of Inference by resolutions, to check if a
query is True, is as follows:
- we want to know if KB ⊨ A
- We turn into (KB ^ ¬A), to see if we can get a contradiction
- We resolve the Knoledge Base, via the inference rules in order to produce new
    clauses from the previous one in order to reduce terms. We do this process
    recursively until we get either a contradiction, or there are no more
    possible clauses to get.
- If we got a contradiciton the we can assume that KB ⊨ A, otherwise KB does
    not entail A.

## First Order Logic

### Universal Quantification
For all possible values of X, a statement is TRUE.


### Existencial Quantification
There's at least one value X, for which a statemtent is TRUE.
