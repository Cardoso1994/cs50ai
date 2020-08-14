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
- terminal symbol
- non-terminal symbol
N
D
ADJ
P
NP
VP
-nltk

## ngram
### character n-gram
### word n-gram
### unigram
### bigram
### trigram
### tokenization
- challenges of tokenization
- ngrams can be modeled with markov models
- markovify

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
