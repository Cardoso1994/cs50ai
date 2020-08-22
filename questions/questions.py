import nltk
import sys
import os
import string
import re
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }

    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    # query = set(tokenize(input("Query: ")))
    query = set(tokenize("whEn WAs pytHon 3.0 releaSED?"))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    corpus = {}
    for file in os.listdir(directory):
        with open(os.path.join(directory, file)) as file_:
            corpus[file] = file_.read()

    return corpus


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    document    = [word for word in nltk.word_tokenize(document.lower())]
    words       = []

    for word in document:
        for char in string.punctuation:
            if char in word:
                word = word.replace(char, '')

        if word != '' and word not in nltk.corpus.stopwords.words("english"):
            words.append(word)

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    whole_words = get_all_words(documents)
    total_docs  = len(documents)
    idfs        = {}

    for word in whole_words:
        count = 0
        for document in documents:
            if word in documents[document]:
                count += 1
        if count > 0:
            idfs[word] = math.log(total_docs / count)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    tf_idf      = []
    top_files   = []

    for file in files:
        count = 0
        word_gen = (word for word in query if word in files[file])
        for word in word_gen:
            count += files[file].count(word) * idfs[word]
        top_files.append(file)
        tf_idf.append(count)

    tf_idf, top_files = zip(*sorted(zip(tf_idf, top_files),
                                        key=lambda x: x[0], reverse=True))
    return top_files[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    top_sent   = []
    mwm         = []
    qtd         = []

    # compute matching word measure and query term density
    for sentence in sentences:
        mwm_ = 0
        qtd_ = 0
        word_gen = (word for word in query if word in sentences[sentence])
        for word in word_gen:
            mwm_ += idfs[word]
            qtd_ += sentences[sentence].count(word) / len(sentences[sentence])
        top_sent.append(sentence)
        mwm.append(mwm_)
        qtd.append(qtd_)

    # sorting with matching word measure
    top_sent, mwm, qtd = zip(*sorted(zip(top_sent, mwm, qtd),
                                     key=lambda x: x[1], reverse=True))
    top_sent = list(top_sent)
    mwm = list(mwm)
    qtd = list(qtd)

    # sorts all repeated mwm elements, if any
    # and puts them back in original lists
    i = 0
    len_mwm = len(mwm)
    while i < len_mwm:
        mwm_ = mwm[i]
        j = i + 1
        while j < len_mwm and mwm_ == mwm[j]:
            j += 1
        if j - i > 1:
            short_top_sent = top_sent[i : j]
            short_mwm = mwm[i : j]
            short_qtd = qtd[i : j]
            short_top_sent, short_mwm, short_qtd = \
                zip(*sorted(zip(short_top_sent, short_mwm, short_qtd),
                            key=lambda x: x[2], reverse=True))
            top_sent[i : j] = short_top_sent
            mwm[i : j] = short_mwm
            qtd[i : j] = short_qtd
        i = j

    return top_sent[:n]

def get_all_words(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list of
    words, returns a set of all the words present in all documents combined
    """

    words = set()
    for document in documents:
        for word_ in documents[document]:
            words.add(word_)

    return words

if __name__ == "__main__":
    main()
