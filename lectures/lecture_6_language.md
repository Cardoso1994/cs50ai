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
### Sentiment Analysis
- bag-of-words model
- naive bayes
    Baye's Rule
    P[ :) ]
    P[ :( ]
    independent events for any word in a review
    P(positive review)
    P(word | positive)
    P(word | negative)
    normalize
    if zero probability for a word?
        - additive smoothing
        - laplace smoothing

## Information retrieval
### topic modeling
### term frequency
- function words
- content words
- ignore function words

### Inverse document frequency
idf = log ((docs with word) / (total docs))

## Semantics
### Information extraction
- Templates when {sth} was founded in {sth}"

#### WordNet Dataset
Definitions of words

#### Word Representation
- one-hot representation (vectors of 1 and 0's)
- distribution representation
- word2vec
    - vector representation
    - skip-gram architecture (NN)
    - distance between words
