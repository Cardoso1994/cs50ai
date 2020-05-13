Lecture 2 - Probability

# Probability

## Probability
Probability brings the capacity to try to predict or make inferences on
wether an event might happen or not, in other words it tells us how likely
is an event to occur.

We express probability distributions in terms of random variables, where a
random variable is a variable that can get multiple values depending on the
possible outcomes of a particular event. For example, let R be the random
variable for rain, this variable may take a value from a sample of three
possible outcomes: no, light, heavy, meaning that there is no rain, light rain
or heavy rain, and can be written as:

    R = <no, light, heavy>
    P(R) = <0.6, 0.3, 0.1>
it is worth noticing that the sum of all the probabilities of a probability
distribution MUST ALWAYS be equal to 1. In the example above we can infere that
there is a 0.6 prob of having no rain, a 0.3 chance of light rain and finally
a 0.1 probability of heavy rain, which all sum to 1.

### Conditional and unconditional Probability
There are multiple kinds of probability, but it can basically be split into two
kinds, unconditional and conditional probability. When a given event has an
uncoditional probability means that the event might as well be independent of
other events, this is the same as to say that the probabilities of other things
happening does not have an impact in this particular event ocurring or not.

A unconditional probability might be when a coin is flipped, there is a 0.5
chances of getting aguila and 0.5 chances of getting sol, and this is not
influenced by any other factor, assuming everything is fair. Taking it further,
without getting into distributions, if you flip the coin two, three or more
times, the probabilities on every flip do not depend on the result of previous
flips, this means the probability of getting aguila in the second flip does not
change if you get or didn't get an aguila in the first one, it will remain 0.5.

On the other hand, conditional probability is a way to express the chances of
something happening based on the evidence that other thing already (or not)
happened. For example we can express the probability that it will rain in the
afternoon when we already know that it was cloudy in the morning, this
particular example would be written as:
    P(rainy_afternoon | cloudy_morning)
and it is read as "the probability of rainy_afternoon GIVEN cloudy_morning".
There are some points to make emphasis on, the first one is that
P(rainy_afternoon | cloudy_morning) is a new probability distribution and as
such it must add up to one, the second point derives from that firts aspect,
it has to be a new probability distribution because HAVING MORE EVIDENCE SHOULD
UPDATE OUR BELIEFS on something happening or not, and this is true because if
we already have evidence, our range of possible outcomes is restricted to only
the space where the evidence is true, giving this a new whole on which to 
compute the next combinations of outcomes.

For instance, in P(rainy_afternoon | cloudy_morning) we update our space of
possible result because we already know that it was cloudy in the morning so 
we NEGLECT the cases where it was not cloudy, having a new sample space where
the morning was in fact cloudy, and with this new space we compute new
probabilities of having rain in the afternoon.

To emphazise a little more, we may have a unconditional probability
distribution for a rainy afternoon:

    P(rainy_afternoon) = <yes, no>
    P(rainy_afternoon) = <0.2, 0.8>
which might be an average of data for some past days, and does not include
information about the morning, but these must change if we have a cloudy
morning, which makes logical sense, since we can deduce without computations
that if it was cloudy in the morning, there are more chances of having rain in
the afternoon, and so, this new distribution given that we have new evidence
could be as follows:

    P(rainy_afternoon | cloudy_morning) = <yes, no>
    P(rainy_afternoon | cloudy_morning) = <0.8, 0.2>

Other thing that we might want to know is the probability that it is a
cloudy_morning AND a rainy_afternoon, this can be obtained as the product of
the probability P(rainy_afternoon | cloudy_morning) times P(cloudy_morning),
which again can be derived with common sense, we can see it as the result
of the chances of having a rainy_afternoon given a cloudy_morning, multiplied
by the chances that it was in fact cloudy, and it is written as:

    P(rainy_afternoon ^ cloudy_morning) = P(rainy_afternoon | cloudy_morning)
                                            * P (cloudy_morning)
and this also can be the other way around, since
P(rainy_afternoon ^ cloudy_morning) is the exact same thing as
P(cloudy_morning ^ rainy_afternoon)

    P(cloudy_morning ^ rainy_afternoon) = P(cloudy_morning | rainy_afternoon)
                                            * P (rainy_afternoon)

### BAYE'S Theorem
The fact that we can compute the probability of "one thing AND other thing" is
a wonderful statement, since it gaves place to a famous, widely used equation,
the BAYE'S THEOREM, that comes from some algebraic manipulation of the two
equations above, and finally can be seen as:

    P(rainy_afternoon | cloudy_morning) = P(cloudy_morning | rainy_afternoon)
                                            * P(rainy_afternoon)
                                            / P(cloudy_morning)

this equation is very useful in real applications since some data might be hard
to get from direct experiments or data gathering, and other some might be
easier, so BAYE'S THEOREM allows us to get other kind of insight (the opposite
direction, so to speak) from information already known.

Which is more important is the whole meaning that this equation holds, it can
be seen as a tool that lets us update our predictions or beliefs on something
happening based on new evidence. If, for example, we want to know the
probability of A happening, given we know some new evidence E, we can write the
equation as:

    P(A | E) = P(E | A) * P(A) / P(E)

where these terms mean:
    - P(E | A) = this restrict the whole possible outcomes where A is true,
                    to those where the EVIDENCE HOLDS
    - P(A) = is called the "prior", and represents the belief we had previous
                    to the adquisition of the new evidence, of A happening.
    - P(E) = restricts  the whole original sample to those cases where E
                    is true, this includes P(E | A) * P(A) since those cases
                    represent (E ^ A) and also includes the outcomes of
                    (E ^ ¬A), because together they add up to all the possible
                    cases where E is true.
    - 3blue1brown has an excelent [video](https://www.youtube.com/watch?v=HZGCoVF3YvM)

### Negation
Until now, we have only talked of probabilities of something happening, but
the idea of negation gives us the opportunity to compute the chances of
something NOT happening. This is important because it gives a relation between
something happening or not, and results useful because sometimes it will be
easier to compute some probability and then via negation, we can obtain what we
ultimately wanted to compute. Negations is expressed as:

    P(¬A) = 1 - P(A)

### Intersections (AND) and Unions (OR)
For instersections we can define two types of relations between two events,
dependent an independent events, where MUTUALLY EXCLUSIVE events is a special
case dependent events. We have already stated that the probability of A and B
is written as:

    P(A ^ B) = P(B | A) * P(A) ---> General rule

this holds true for every case, no matter their relations, and the formulas for
more specific cases are derived from this one.For instance, if we had the case
where that A and B are mutually exclusive, we can safely assume that
P(B | A) = 0, since we already know there are no chances of B happening once A
has already happened, thus, P(A ^ B) is also zero

    P(A ^ B) = 0    ---> For MUTUALLY EXCLUSIVE events.

On the other hand, when we are dealing with independent events, we can fairly
assume that P(B | A) = P(B), since we know that A happening does not affect
the probabilities for B, which is the same as saying that the probability of B
remains the same no matter the state of A, and this is what that simplification
says. Thus, P(A ^ B) is:

    P(A ^ B) = P(B) * P(A) ---> For INDEPENDENT events.

In the case of unions, the logic behind the formulas results quite similar than
that for intersections, but here our focus is diveded in MUTUALLY AND NOT
MUTUALLY EXCLUSIVE events. The general ADDITION RULE is written as:

    P(A v B) = P(A) + P(B) - P(A ^ B) ---> General rule

this equation holds true for all possible cases, and the derivation of the
formulas for the other cases are simplification of this general rule. For the
case of mutually exclusive events, we already know that P(A ^ B) = 0, and
therefore we can simplify the general rule to:

    P(A v B) = P(A) + P(B)

### Marginalization
Sometimes we might want to know the unconditional probability of some event A,
but there is no available information about it but the conjutnion probability
of this even A with other event B. Given this, the unconditional probability of
A can be computed with:

    P(A) = P(A ^ B) + P(A ^ ¬B)

This is true for an event B that has only two possible outcomes, like a boolean
event, but holds in the case of more outcomes where the only thing to do is to
sum all the conjuction probabilities for all the outcomes of B.

### Conditioning
The same logic for marginalization holds true for the case where the only
data avalible is the conditional probability between A and B. If we want the
unconditional probability P(A), the equation used will be:

    P(A) = P(A | B) * P(B) + P(A | ¬B) * P(¬B)

It is clear that this is true since it really is the same formula of
marginalization, but we replace the conjuction probability with a conditional
one, via the general rule of addition.

It is worth say that Conditioning is a very useful tool, for example when
applying the BAYE'S THEOREM, because the data from the denominator will mostly
appear in terms of conditional probability.
