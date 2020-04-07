import csv
import sys
from collections import deque

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    # FTRINGS
    #   f"this is a f string"
    #   fstrings are used to give format for a string.
    #   is an easy way to embed variables into a string
    #   In the string below it will put whatever value is in the variable
    #   "directory"
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    # get the id's for the name passed via input
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # call to breadth first search implementation
    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # create a Queue and an explored set
    tree = QueueFrontier()
    explored = set()

    neighbors = neighbors_curated(source)
    for neighbor in neighbors:
        #                   source_id, neighbor_id, movie_id
        tree.add(Node(state=(source, neighbor[1], neighbor[0]),
                      parent=None, action=neighbor))

    # BFS search to Kevin Bacon. Does nothing if Kevin Bacon is Source
    current = tree.remove()
    while True and source != '102':
        # current = tree.remove()
        explored.add(current.state)
        if is_kevin_bacon(current.action[1]):
            break

        neighbors = neighbors_curated(current.action[1])
        for neighbor in neighbors:
            # add nodes to tree if they aren't already explored
            if not is_in_set((current.action[1], neighbor[1], neighbor[0]),
                         explored):
                tree.add(Node(state=(current.action[1], neighbor[1],
                                     neighbor[0]),
                      parent=current, action=neighbor))
        current = tree.remove()

    # sanity check in case Kevin Bacon is source
    if source != '102':
        tree = QueueFrontier()
    else:
        current = tree.remove()

    # BFS to search for target
    while True:
        if current.action[1] == target:
            break

        neighbors = neighbors_curated(current.action[1])
        for neighbor in neighbors:
            # add nodes to tree frontier if they aren't already explored
            if not is_in_set((current.action[1], neighbor[1], neighbor[0]),
                         explored):
                tree.add(Node(state=(current.action[1], neighbor[1],
                                     neighbor[0]),
                      parent=current, action=neighbor))

        current = tree.remove()

    path = deque()
    while current is not None:
        path.appendleft(current.action)
        current = current.parent

    return (list(path))


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """

    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


def neighbors_curated(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person, without repeating the given person
    """

    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id_ in movies[movie_id]["stars"]:
            if not person_id_ == person_id:
                neighbors.add((movie_id, person_id_))
    return (neighbors)


def is_in_set(connection, explored):
    """
    Checks if a connection between two people has already been explored
    """

    for node in explored:
        if connection[0] in node and\
            connection[1] in node and\
            connection[2] in node:
                return True

    return False


def is_kevin_bacon(person_id):
    """
    Checks if a person is Kevin Bacon
    """

    kevin_id = '102'
    if person_id == kevin_id:
        return True

    return False


if __name__ == "__main__":
    main()
