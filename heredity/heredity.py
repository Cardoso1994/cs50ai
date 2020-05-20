import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        # P(trait | gene=2)
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        # P(trait | gene=1)
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        # P(trait | gene=0)
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, AND
        * everyone in set `two_genes` has two copies of the gene, AND
        * everyone not in `one_gene` or `two_gene` does not have the gene, AND
        * everyone in set `have_trait` has the trait, AND
        * everyone not in set` have_trait` does not have the trait.
    """
    # initial value of joint probability
    joint_p = 1

    # get people for zero genes
    people_names = set(people.keys())
    zero_genes  = people_names - (one_gene | two_genes)

    # dict that tells us the inverse of the sets above.
    # i.e. each people -> how many genes it has
    # and if they have the trait or not
    people_genes = {person:{'gene':None, 'trait':False}
                    for person in people_names
                   }

    # this dict has the probability of passing a bad gene depending on how many
    # genes a person has. This is the prob of a parent passing a gene
    probs_hereditary = {
            2: {1:0.99, 0:0.01},
            1: {1:0.5, 0:0.5},
            0: {1:0.01, 0:0.99},
            }

    # filling people_genes
    for person in zero_genes:
        people_genes[person]['gene'] = 0
        if person in have_trait:
            people_genes[person]['trait'] = True
    for person in one_gene:
        people_genes[person]['gene'] = 1
        if person in have_trait:
            people_genes[person]['trait'] = True
    for person in two_genes:
        people_genes[person]['gene'] = 2
        if person in have_trait:
            people_genes[person]['trait'] = True

    # computing joint prob for zero genes people
    # the product of the probability of each parent not passing the gene
    for person in zero_genes:
        particular_joint = 1
        mother = people[person]['mother']
        father = people[person]['father']
        if mother is None:
            particular_joint *= PROBS['gene'][0]
        else:
            particular_joint *= \
                (probs_hereditary[people_genes[mother]['gene']][0]
                        * probs_hereditary[people_genes[father]['gene']][0])

        particular_joint *= PROBS['trait'][0][people_genes[person]['trait']]
        joint_p *= particular_joint

    # computing joint prob for one gene
    # the sum of two cases, either mother and not father, or father and not
    #   mother
    for person in one_gene:
        particular_joint = 1
        mother = people[person]['mother']
        father = people[person]['father']
        if mother is None:
            particular_joint *= PROBS['gene'][1]
        else:
            from_mother = (probs_hereditary[people_genes[mother]['gene']][1]
                    * probs_hereditary[people_genes[father]['gene']][0])
            from_father = (probs_hereditary[people_genes[mother]['gene']][0]
                    * probs_hereditary[people_genes[father]['gene']][1])
            particular_joint *= (from_mother + from_father)

        particular_joint *= PROBS['trait'][1][people_genes[person]['trait']]
        joint_p *= particular_joint

    # computing joint prob for two genes
    # each parent passes one gene
    for person in two_genes:
        particular_joint = 1
        mother = people[person]['mother']
        father = people[person]['father']
        if mother is None:
            particular_joint *= PROBS['gene'][2]
        else:
            particular_joint *= \
                (probs_hereditary[people_genes[mother]['gene']][1]
                        * probs_hereditary[people_genes[father]['gene']][1])
        particular_joint *= PROBS['trait'][2][people_genes[person]['trait']]
        joint_p *= particular_joint

    return joint_p


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    people_names = set(probabilities.keys())
    zero_genes = people_names - (one_gene | two_genes)

    for person in people_names:
        if person in zero_genes:
            probabilities[person]['gene'][0] += p
        elif person in one_gene:
            probabilities[person]['gene'][1] += p
        elif person in two_genes:
            probabilities[person]['gene'][2] += p

        if person in have_trait:
            probabilities[person]['trait'][True] += p
        else:
            probabilities[person]['trait'][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    for _ in probabilities:
        alpha = (probabilities[_]['gene'][1] + probabilities[_]['gene'][2]
            + probabilities[_]['gene'][0]) ** -1
        probabilities[_]['gene'][0] *= alpha
        probabilities[_]['gene'][1] *= alpha
        probabilities[_]['gene'][2] *= alpha

        alpha = (probabilities[_]['trait'][True] +
                    probabilities[_]['trait'][False]) ** -1
        probabilities[_]['trait'][True] *= alpha
        probabilities[_]['trait'][False] *= alpha

if __name__ == "__main__":
    main()
