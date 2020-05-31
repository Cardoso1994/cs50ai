import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.crossword.variables:
            for word in self.crossword.words:
                if var.length != len(word):
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # check for every item in x's domain, if there is at least one value
        # in y's domain that does not violate the arc restrictions
        #
        # An arc restriction in a crossword problem is the fact that in the
        # intersection of the words, they must have the same letter
        #
        # if something does not hold the restrictions, it must be removed from
        # x's domain. And the function should return True. Otherwise it must
        # return False
        cells = self.crossword.overlaps[x, y]
        not_viable = set()
        flag = False

        # debugging prints
        # print(f"cells: {cells}")
        # print(f"x domain before: {self.domains[x]}")
        # print(f"y domain before: {self.domains[y]}")
        # if not cells:
        #     return False

        for x_option in self.domains[x]:
            for y_option in self.domains[y]:
                if x_option == y_option:
                    continue
                if x_option[cells[0]] == y_option[cells[1]]:
                    break
            else:
                not_viable.add(x_option)
                flag = True

        self.domains[x] = self.domains[x] - not_viable
        # debugging prints
        # print(f"x domain after: {self.domains[x]}\n")
        return flag

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # check if arcs is None. creates a queue of tuples
        if arcs is None:
            arcs = []
            for x in self.crossword.variables:
                for pair in self.crossword.neighbors(x):
                    arcs.append((x, pair))

        for x, y in arcs:
            if self.revise(x, y):
                if not self.domains[x]:
                    return False
                for pair in (self.crossword.neighbors(x) - {y}):
                    arcs.append((x, pair))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        if len(self.crossword.variables) != len(set(assignment.keys())):
            return False

        for _, word in assignment.items():
            if not word:
                return False

        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # assignment = {variable: word, ...}
        # check if all values in dict are different
        vals = set(assignment.values())
        if len(vals) != len(assignment):
            return False

        # for every key value pair, both have the same lenght
        for var, word in assignment.items():
            if var.length != len(word):
                return False

        # no conflicts between neighbors
        for var in assignment.keys():
            neighs = self.crossword.neighbors(var).intersection(
                set(assignment.keys()))
            for neigh in neighs:
                i, j = self.crossword.overlaps[var, neigh]
                if assignment[var][i] != assignment[neigh][j]:
                    return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        neighbors = self.crossword.neighbors(var) - set(assignment.keys())
        var_words = self.domains[var]
        var_orders = [0] * len(var_words)

        # TODO
        # should check which word rules out less
        # Assign a numerical value in var_orders which will tell how many
        #   values it rules out from its neighbors.
        # There's a one-to-one correspondance between var_words and var_orders
        for i, word in enumerate(var_words):
            for neigh in neighbors:
                if word in self.domains[neigh]:
                    var_orders[i] += 1
                cells = self.crossword.overlaps[var, neigh]
                for neigh_word in self.domains[neigh] - {word}:
                    if word[cells[0]] != neigh_word[cells[1]]:
                        var_orders[i] += 1

        zipped_list = zip(var_orders, var_words)
        sorted_pairs = sorted(zipped_list)
        tups = zip(*sorted_pairs)
        var_orders, var_words = [list(tuple) for tuple in tups]

        return var_words

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        def len_values(var):
            return len(self.domains[var])

        unassigned = list(self.crossword.variables - set(assignment.keys()))
        unassigned.sort(key=len_values)
        return unassigned[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        # for value in self.domains[var]:
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
            new_assignment.pop(var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
