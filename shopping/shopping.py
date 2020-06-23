import csv
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # replacing months string for numbers
    shopping_data = pd.read_csv(filename)
    months = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'June':5, 'Jul':6,
              'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
    shopping_data = shopping_data.replace(months)

    # replacing VisitorType for ints [returning = 1, otherwise = 0]
    shopping_data["VisitorType"] = np.where(shopping_data["VisitorType"] ==
                                            'Returning_Visitor', 1, 0)

    # replacing Weekend and Revenue bools for ints
    bool_replacement = {True:1, False:0}
    shopping_data["Weekend"] = \
            shopping_data["Weekend"].replace(bool_replacement)
    shopping_data["Revenue"] = \
            shopping_data["Revenue"].replace(bool_replacement)
    evidence = []
    labels = []
    for _, row in shopping_data.iterrows():
        tmp = row.tolist()
        evidence.append(tmp[:-1])
        labels.append(tmp[-1])

    scaler = StandardScaler()
    scaler.fit(evidence)
    evidence = scaler.transform(evidence)

    return (evidence, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(evidence, labels)

    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    data_frame = pd.DataFrame({"labels": labels, "predictions": predictions})
    actual_positive_mask = data_frame["labels"] == 1.0
    actual_positive = data_frame[actual_positive_mask]
    sensitivity = (
        (actual_positive["labels"] == actual_positive["predictions"]).sum()
                   ) / actual_positive.shape[0]
    actual_negative_mask = data_frame["labels"] == 0.0
    actual_negative = data_frame[actual_negative_mask]

    specificity = (
        (actual_negative["labels"] == actual_negative["predictions"]).sum()
                  ) / actual_negative.shape[0]

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
