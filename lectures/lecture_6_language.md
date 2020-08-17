# Lecture 6 - Language

Natural Language Processing (NLP) is a subset of artificial intelligence which
main focus is, as its name suggests, to process and understand Natural Language
(human language) and act upon that understanding, to retrieve some information
or conclusions to the AI's user.

It differs from other topics in articial intelligence in the sense that in this
particular case, the main purpose is to provide the program a set of rules to
understand humans, and how we communicate, whereas in the previously discussed
topics, its the human who is trying to encode a particular problem in a way
that is easier for a computer to deal with it, this is, we come with some
numerical representations for a given problem so the machine can act, learn and
make conclussions based on that particular numerical representation.

## Main applications
There are many applications of natural language processing, the most common
ones are:
- automatic summarization -> the purpose of the AI is to provide a summary of a
        particular text that has been passed to it. One example would be to
        generate the Abstract of a scientific paper when the content of the
        paper is passed to the AI.
- information extraction -> This is somehow related to automatic summarization,
        but instead, the goal for this kind of AI is to tell what is the main
        topic presented in a text, is it about politics?, presidential
        elections?, is it a scientific paper?, maybe it has something to do
        with astrophysics?
- language identification -> As the name implies, the purpose here is to be
        able to identify the language in which the content is written in. This
        is useful for example when wen surfing, your browser may tell you that
        the page you are visiting is in a given language, and it might even
        suggest to translate it to your default language.
- machine translation -> This works hand in hand with language identification,
        it first need to know from what language and to what language the
        translation is going to take place. A first problem that may arise is
        the fact that not every language is structured in the same way, also
        there might be words that are not "one to one" translated from one
        language to another, and it may take a whole sentence to achieve the
        same meaning for a particular word. Also there will be words that have
        a particular differente meaning depending on the context in which they
        are used.
- named entitiy recognition -> This particular kind of algorithms tries to
        identify names of entities, the name of a person, etc.
- speech recognition -> This is a very special type of artificial intelligence,
        and it is also very special in the realm of natural language
        processing. While the other algorithms deal mostly with text, speech
        recognition deals with voice, sound waves, and its main purpose is to
        try to understand what people is saying. This kind of application is
        famous in software such as Siri or Alexa.
- text classification -> Classification of a particular text. What kind of text
        is it?
- word sense disambiguation -> Its purpose is to make conclussion about the
        exact meaning of a word given the context in which is being used.
- among others...

## Syntax and Semantics
### Syntax - Structure of a language
Syntax refers to the analysis of a language at its structure level, it mainly
deals with the right way a sentence or phrase should be structured to be a
valid sentence in a particular language. For example, in english a basic
structure for a prhase is:
- Noun - verb - noun
- "Just before nine o'clock Sherlock Holmes stepped briskly into the room"

which is a valid sentence. On the other hand, there are sets of words that do
not form a valid sentence, for example:
- "Just before Sherlock Holmes nine o'clock stepped briskly into the room"

There is also the case, when we encounter a sentence that has an ambiguous
meaning, but still it is a valid phrase, for example:
- I saw the man in the mountain with a telescope

this sentence is ambiguous because it can have one of two meanings, in one
meaning, "I saw the man in the mountain, and I am the one that is using the
telescope", on the other hand it could mean "I saw the man in the mountain, and
the man in the mountain is the one holding the telescope".

### Semantics - Meaning of a sentence
When talking about semantics, we refer wether a phrase has a particular well
defined meaning or not, given that it is syntacticly right, or in other words,
we are checking if a given phrase has some real meaning or it is just a set of
random words that although they are well structured, the don't give any
particular kind of meaning.

Example of Semanticly right sentences are:
- "Just before Sherlock Holmes nine o'clock stepped briskly into the room"
- "Sherlock Holmes stepped briskly into the room just before nine o'clock"
- "A few minutes before nine, Sherlock Holmes walked quickly into the room"
these three sentences are all valid, and even more, they have practically the
same meaning even though in the two first cases the words are the same just in
different order. The third one also maintains the same general idea, only
expressed with different words.

An example of a semanticly incorrect phrase is:
- "Colorless green ideas sleep furiously"

Now that some basic structure and ideas refering to Natural Language have been
provided, we can start to get into the ideas and algorithms that have been and
are being developed in order to give a machine the ability to understand human
language.

## Formal Grammar
Formal Grammar is a concept in which the basic idea is to divide sentences in
different parts, such as nouns, verbs, adjectives, prepositions, etc. Once this
concepts are defined, we can start to feed data to the machine learning
program. A particular algorithm for formal grammar is "Context-Free Grammar".

### Context-Free Grammar
Context-Free Grammar is a set of rules in which we relate every word to a
concept, for example a word like "she" will be related to the concept "Noun".
This allows us to divide the phrase into multiple subparts, and analyze it by
the components of it instead of the words that make the phrase. For example:

-She    saw     the     city
  |      |       |        |
- N      V       D        N

the example above translates every english word into a "concept". The formal
term to refer to concepts is _"Terminal Symbol"_, whereas we refer to a word as
a _"Non-Terminal Symbol"_. This allows to give to the AI the ability to
understand phrases in a general way by following this structure. There are many
kind of terminal symbols, for example:
- N -> Noun
- V -> Verb
- D -> Determinant
- ADJ -> adjective
- P -> preposition

In order to provide the machine with some "knowledge", we create some sort of
dictionary (in a pythonic sense):

N -> she | city | car | Marco | Harry | ...
V -> saw | ate | walked | run | ...
D -> the | a | an | ...
P -> to | on | over | ...
ADJ -> blue | busy | old | ...

We can also start to make more complex Terminal Symbols:

NP -> N | D N

where NP stands for "noun phrase" and it tells us that a noun phrase can be
formed by a noun, for example "car", or it can also be formed by a determinant
and a noun, for example "the city". This allows for more complex analysis of
the phrases, an a more accurate representation of natural language, in this
particular case english.

            NP                   NP
           /  \                  |
          /    \                 |
         /      \                |
        D        N               N
        |        |               |
        |        |               |
       the      city            she

From this, we start creating other ideas such as verb phrases and sentences:

VP -> V | V NP
S -> NP VP

### NLTK
Nltk is a python module developed with natural language processing in mind, and
it provides an easy use for Context-Free grammar, it even shows a graphic
representation of the te terminal symbols that make a given sentence.

This can be seen in the cs50 lectures.

## ngram
The n-gram is a technique in which we separate a given part of text into
subsets, or "n-grams". The "gram" could be a whole text, which is divided into
pargraphs, maybe it would be a complete sentence separated into words, or maybe
it is a simple word separated into characters.

When we separate a word into characters we are doing a _"character n-gram"_,
and when we separate a sentence into words it is calles _"word n-gram"_. There
is also another possible classification, which is by how many "grams" are we
taking to be analyzed, this could be a _"unigram"_ for one character/word, a
_"bigram"_ for two, _"trigram"_ for three and so on.

More formally, an N-GRAM is defined as:
- "A contiguous sequence of n items from a sample text"

An example for a trigram would be, from the sentence below:
"How often have I said to you that when you have eliminated the impossible
whatever remains, however improbable, must be the truth?"

for this expression, the trigrams would be groupped as follows:
- How often have
- often have I
- have I said
- I said to
- said to you
- ...

### tokenization
Tokenization is the result of splitting a given set of characters into
subpieces (tokens). There are many kinds of tokenization, for example word
tokenization, in which we divide a text into words, and character tokenization
in which we divide a word into characters.

There are many challenges that arise when dealing with tokenization, for
example, when doing word tokenization the first challenge is to determine where
we are splitting each word. The naive approach would be to separate words
whenever we find a blank space, but this may have some consequences, from the
example above, a word tokenization would be:

- ["How", "often", "have", "I", "said", ..., "whatever", "remains,", ...]

from this we see that the word "remains," has been splitted along with the
comma, which will result in the AI trating different this word "remains," as a
complete different word of "remains". So it is important to take into account
also punctuation signs.

In another example, let's say we want a sentence tokenization over a paragraph,
the naive approach would be to split sentences whenever we find a period ("."),
but this would also represents a problem, if we have a sentence:

- "I cannot waste time over this sort of fantastic talk, Mr. Holmes. If you can
chatch the man,catch him, and let me know when you have done it"

a problem will arise with the word "Mr." because in our naive approach the
senences would be
- "I cannot waste time over this sort of fantastic talk, Mr."
- "Holmes."
- "If you can chatch the man,catch him, and let me know when you have done it"

Ngrams are useful because they allow the AI to know which words usually come
after a particular word or a particular set of words, which in turn could be
modeled as a markov chain, in which the AI has a probability distribution of
which words is most proable to come after a single word, or maybe after a set
of two, three or even more words.

A library that allows the modeling of ngrams as markov chains is "markovify".
An application of this would be to generate text that looks like some
particular individual has written, maybe some lyrics that a rock band may have
written, or maybe some phrases that a famous author would write.

## Text Cateogrization
Another application of natural language processing is in text categorization,
in which the AI will attempt to give a concise result about a particular text
that has been passed to it. A good example is Sentiment Analysis. It is also a
useful tool to mail servers, the main application is to decide if a received
mail is spam or is it a legit email.

### Sentiment Analysis
Sentiment Analysis goal is to tell wether a text is about something happy,
something sad, maybe the people talking is angry, etc.

The most common algorithm for this task is the "bag-of-words model", which
gives a particular word a classification, then it analyzes some text word by
word, and if it encounters a word that has been classified as good, it will
output that this particular text is good. A good example of this is to classify
reviews in webpages such as amazon, ebay, etc. The reviews can be classified as
"good" or "bad".

A sample of reviews could be:
- "My grandson loved it! So much fun!"
- "Product broke after a few days"
- "One of the best games I've played in a long time"
- "Kind of cheap and flimsy, not worth it"

from these examples and with the "bag-of-words model" our AI would classify the
first review as good, since it has the words ["loved", "fun"] in it. The second
review would be classified as bad because the word "broke" is in it.

Another approach to make classification is the "Naive Bayes Algorithm", which
bases all of its logic in the application of the Baye's theorem, and its goal
is to give a probability distribution of wether a particular text is, in the
same "reviews" example, a good or a bad review.Or in other words, the AI will
tell us if it thinks a particular review is a good review, with a given level
of certainty.

- P[ :) ]
- P[ :( ]

The way Naive-Bayes approaches a problem is by taking every word in a sentence
as an independent event from the other words, this in realitiy might not be
true, but it gives a very good approximation in the results. For example, in
the sentence:

- "My grandson loved it!"

the Bayes Theorem would state:
`P[ ":)" | ["My", "grandson", "loved", "it"]]` -> probability of a good review
                                                given "My grandson..."
this is equal to
`P(["My", "grandson", "loved", "it"] | ":)") * P (":)") / P(["My", "grandson", "loved", "it"])`

which in turn is proportional to
`P(["My", "grandson", "loved", "it"] | ":)") * P (":)")`

The Naive Bayes algorithm takes this simplication one step further, by stating
that, all of this is proportional to
`P(":)" | "My") * P(":)" | "grandson") * P(":)" | "loved") * P(":)" | "it!") `

this is achieved, as stated before, by treating every word as an independent
event from the rest of the words.

The way to obtain the probability distributions with a provided data set, is as
follows:
```
    P(":)") = total_positive_reviews / total reviews
    P("given_word" | ":)") = total_positive_reviews_with_word /
                                    total_positive_reviews
```
the same formulas apply for the negative cases. The next table describes the
example discussed in the lecture, giving the probability distribution for the
example in question:

:) | :(
--------
0.49 | 0.51

            | :)    | :(
----------------------------
My          | 0.30  | 0.20
grandson    | 0.01  | 0.02
loved       | 0.32  | 0.08
it          | 0.30  | 0.40

From the above tables we get:
```
P(":)") * P("My" | ":)") * P("grandson" | ":)") * P("loved" | ":)") * P("it" | ":)")
    = 0.49 * 0.30 * 0.01 * 0.32 * 0.30 = 0.00014112
P(":(") * P("My" | ":(") * P("grandson" | ":(") * P("loved" | ":(") * P("it" | ":(")
    = 0.51 * 0.20 * 0.02 * 0.8 * 0.40 = 0.00006528
```

If we normalize the results (making them to sum up to 1) we get:
```
P(":)") = 0.6837
P(":(") = 0.3163
```

According to the Naive Bayes algorithm, and with the provided data set, tells
us that this review is positive with a probability of 68%.

Now, there might be ocassions when Naive Bayes will only crash, an example
could be when we rty to analize a word that didn't appear a single time in the
data set. If this should ever happen, the proability of that word will be zero,
hence making the conjunction probability also zero, there are many ways to make
front to this problem. The first one is called "Additive Smoothing" in which we
always add a value "\alpha" to each value in the distribution. The second one
is "Laplace smoothing", in this approach we add 1 to every value in our
distribution, this is like pretending we saw that word one more time than we
actually have.

## Information retrieval
This refers to the task to retrieve information about a given text to the user.
In this application, there are many kinds of algorithms, such as topic
modeling.


### Term frequency
Term frequency is technique in which we analyze a text word by word, and
retrieve the most common ones, with the hope of getting some insight of the
main theme of the text, or the most significan aspect of it. It simply return
the number of times the AI saw a particular term, it may return it as a integer
number, or maybe as a percentage.

The main difficulty one might encounter when developing a term frequency
program is that of retrieving "menaingless" terms, which are words with little
to no meaning on their own, but gramatically neceary to connect other words,
such words are called "Function Words". Examples of function words can be:
- "the"
- "a"
- "by"
- "an"
- "is"
- ...

On the other hand, there are words that carry most of the meaning of a given
phrase or text, this words are called "Content Words". These words are the ones
that we are looking for, example of these are:
- "algorithm"
- "category"
- "computer"
- "president"
- "impeachment"
- ...

A good way to eliminate the appearance of function words in the results
retrieved, is by providing a list of those function words, and have the AI to
check every possible result against that list, and only retrieve a given word
as a result if it does not appear in the function words list.

But still there are other problems that we need to take into account. For
example when analyzing many documents at a time.

### Inverse document frequency
An example given in lecture was that of trying to get the main topic about all
of the Sherlock Holmes stories, with the previous approach words like
`["Sherlock", "Holmes"]` will appear as one of the most important terms for all
of the stories, which may not be of big use since we know in advance that
Sherlock Holmes is the main character. With this in mind, "Inverse Document
Frequency" was developed.

The main idea of "idf" is that of checkin between the most important terms
obtained for a particular document, which ones of those DO NOT appear in the
rest of the documents. This is because an important term that does not appear
in other documents MUST be what makes a particular document unique.

```
idf = log [(docs with word) / (total docs)]
```

## Semantics
### Information extraction
Information extraction refers to the act of extracting knowledge from a text.
The idea is that given some particular template to the AI, the program can
parse a text in search for similar patterns and retrieving this found patterns
to the user, hence giving back some new knoledge.

An example for a template would be:
- "when {sth} was founded in {sth}"
for example:
- "when _Facebook_ was founded in _2004_"

by giving the AI this template, and providing a text data base to search in,
the AI may give us back results such as:
- "when _Amazon_ was founded in _1994_"

This kind of algorithms work, not only with this particular template, one, for
example, can give a template such as:
- {Athens, 2004}
- {London, 2012}
- {Rio, 2016}

and then parse the olympic games webpage to the program, and the AI will search
for patterns where the elements of the template are found, and retrieve
information (conclussions) about other olympic games in the form `{location,
year}`, whenever it finds similar patterns in the data given.

#### WordNet Dataset
A very famous data set is the WordNet dataset, which is a huge effort on
labeling words such as nouns, verbs, adjectives among others, into conginitve
synonims (synsets). These synsents are linked by semantical and lexical
relations.
More on [WordNet's site](https://wordnet.princeton.edu/)
Definitions of words

#### Word Representation
The most complex kind of semantics analysis is Word Representation, in which
every word in a given data set has a unique numerical representation, normally
in the form of a vector. This is useful, because this representation can be
obtained and applied in a neural network.

### One-Hot Representation
One-hot representation is the easiest way to give words a numerical
representation, the only task to do is to create a vector of size `N`, where
only one element will have a value of `1`, and the rest of the elements will be
`0`.

For example, in the phrase:
- "He wrote a book"
    - "He"      [1, 0, 0, 0]
    - "wrote"   [0, 1, 0, 0]
    - "a"       [0, 0, 1, 0]
    - "book"    [0, 0, 0, 1]

This, as easy as it may be, is not an optimal approach since there are many
problems that will arise, the first one and most obvious is that of the huge
ammount of memory used, also most of that memory allocated by the program will
be filled with pure `0's`. Another important fact is that of the lack of tha
capability of implying some sort of similarity between words, for example:
- "book"    [0, 0, 1, 0, ..., 0]
- "novel"   [0, 0, ..., 1, 0, 0]

"book" and "novel" are words that in most contexts will work as synonims but in
a one-hot representation they will be tow completely different structures, with
no hint of a possible link between them.

### Distribution Representation
This approach excels at giving some sort of relation between certain groups of
words. It works by making a distribution of values along a vector, instead of
only having `ones and zeros`. For example:
- "He wrote a book"
    - "He"      [-0.34, -0.08, 0.02, -0.18, 0.22, ...]
    - "wrote"   [-0.27, 0.40, 0.00, -0.65, - 0.15, ...]
    - "a"       [-0.12, -0.25, 0.29, -0.09, 0.40, ...]
    - "book"    [-0.23, -0.16, -0.05, -0.57, ...]

This allows the AI to make some inference about the position of particular
words in a given sentence, for example:
- "for `_______` he ate"
    - the blank space can be filled with different words such as
        ["dinner", "breakfast", "lunch"]

### word2vec
Word vector is a model to generate vector model for words, such as the previous
example, words will have a particular numerical representation, with different
values distributed along the elements of the vector. The advantage of this
approach is that similar words are given similar vector values (magnitude), so
words like `["wrote", "authored", ...]` will have a very similar vector
representantion.

The most amazing part of `word2vec` is that it gives the ability of making
mathematical operations on words, and also between words, so now, things like
adding two words are possible and in fact have a particular meaning and use
when treating them as numbers, whereas there is no logic way in which one could
add two words, in a string representantion sort of way.

#### Skip-gram architecture
Is a neural network architecture used for predicting a context word given a
target word. this will allow to get some values for different words given a
particular vector representation.

For example, if we define a function for computing the distance between words,
we now have the ability to find synonims of a word by taking the closest ones
to it. We can get any kind of relation, as long as it is well defined, for
example:

- "king" - "man" = `[some_vector]`
if we add this new value of the difference `"king" - "man"` to a word like
`"woman"`, theway of perform that would be:
```python
diff_king_man = "king" - "man"
woman_plus_diff = "woman" + diff_king_man
result = closest_word_to(woman_plus_diff)

# print result
print(f"the result is: {result}")
```

which should print:
- `queen`

There can be any kind of relation to be analyzed, for example one can get the
relation between `{England, London}` and add it to `{France}` and hopefully get
as result `{Paris}`.
