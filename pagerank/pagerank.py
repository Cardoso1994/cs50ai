import os
import random
import re
import sys
from copy import deepcopy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # create an empty dict for transition model
    transition_mod = dict.fromkeys(corpus, 0)
    corpus_len = len(corpus)

    # if there is no way out of page
    if not corpus[page]:
        prob = 1 / corpus_len
        for _page in corpus:
            transition_mod[_page] += prob

        return transition_mod

    # compute random P of whole corpus
    random_corpus = (1 - damping_factor) / corpus_len
    for _page in corpus:
        transition_mod[_page] += random_corpus

    # compute P of links in page
    linked = len(corpus[page])
    random_linked = damping_factor / linked
    for _page in corpus[page]:
        transition_mod[_page] += random_linked

    return transition_mod


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pagerank_sample = dict.fromkeys(corpus, 0)
    page = random.choice(list(corpus))

    # iterate over the total ammount of samples
    for sample in range(n):
        pagerank_sample[page] += 1 / n
        trans_mod = transition_model(corpus, page, damping_factor)
        page = str((random.choices(population= list(trans_mod),
                weights=list(trans_mod.values()), k=1))[0])

    return pagerank_sample


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # function variables
    pagerank_it = dict.fromkeys(corpus, 0)
    corpus_len = len(corpus)
    convergence = 0.001

    linked_from = {_page: {'pages':set(), 'len':0} for _page in corpus}

    # initial setup
    # also computing the inverse of corpus a dict that holds for each page,
    # what other pages link to it
    prob = 1 / corpus_len
    for _page in corpus:
        pagerank_it[_page] = prob
        for _page_1 in corpus:
            if _page in corpus[_page_1]:
                linked_from[_page]['pages'].add(_page_1)
                linked_from[_page]['len'] += 1


    # iterative process
    first_term = (1 - damping_factor) / corpus_len
    while True:
        error = -0.02
        for _page in corpus:
            prev_rank = pagerank_it[_page]
            pagerank_it[_page] = first_term
            for _page_1 in linked_from[_page]['pages']:
                pagerank_it[_page] += pagerank_it[_page_1] \
                        / len(corpus[_page_1]) * damping_factor

            post_rank = pagerank_it[_page]
            diff = abs(post_rank - prev_rank)
            if diff > error:
                error = diff

        if error < convergence:
            break

    return pagerank_it

if __name__ == "__main__":
    main()
