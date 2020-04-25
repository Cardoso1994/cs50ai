import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """

        # if all the cells are mines or none of them are mines
        if self.count == len(self.cells):
            return self.cells
        elif self.count == 0:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # if all the cells are mines or none of them are mines
        if self.count == 0:
            return self.cells
        if self.count == len(self.cells):
            return set()


    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """

        if len(self.cells) == 1:
            return
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

        return

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        if len(self.cells) == 1:
            return
        # check if cell in self.cells
        if cell in self.cells:
            self.cells.remove(cell)

        return


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

        return


    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

        return


    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

        return


    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        current_mines = set()
        current_safes = set()

        self.moves_made.add(cell)
        self.mark_safe(cell)

        # gettin current sentence
        current_sentence = Sentence(self.get_neighbors(cell), count)
        _current_sentence_cells = current_sentence.cells.copy()

        # clean sentence,  remove cells that are already safes or mines
        current_mines_ = (cell for cell in _current_sentence_cells
                            if cell in self.mines)
        for mine in current_mines_:
            current_sentence.cells.discard(mine)
            current_sentence.count -= 1

        current_safes_ = (cell for cell in _current_sentence_cells
                            if cell in self.safes)
        for safe in current_safes_:
            current_sentence.cells.discard(safe)

        # check if all cells are either safes or mines
        if current_sentence.count == 0:
            current_safes.update(current_sentence.cells)
        elif current_sentence.count == len(current_sentence.cells):
            current_mines.update(current_sentence.cells)

        # add sentence to knowledge
        self.knowledge.append(current_sentence)

        # removing subsets from other sentences. Divide and conquer
        for sentence in self.knowledge:
            for other in self.knowledge:
                if sentence == other:
                    pass
                elif sentence.cells.issubset(other.cells) \
                    and len(sentence.cells) < len(other.cells):
                    other.cells = other.cells - sentence.cells
                    other.count -= sentence.count

        # getting new conclussions
        for sentence in self.knowledge:
            known_ = sentence.known_mines()
            if known_:
                current_mines.update(known_)

            known_ = sentence.known_safes()
            if known_:
                current_safes.update(known_)

        # updating mines and safes
        for cell in current_mines:
            self.mark_mine(cell)
        for cell in current_safes:
            self.mark_safe(cell)

        return


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in (cell_ for cell_ in self.safes
                     if cell_ not in self.moves_made):
            return cell

        return None


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        mines_ = 0
        convergence = (self.height * self.width - len(self.mines))
        while mines_ <= convergence:
            i = random.randrange(self.height)
            j = random.randrange(self.width)
            if (i, j) not in self.moves_made and (i, j) not in self.mines:
                return (i, j)

            mines_ += 1

        return


    def get_neighbors(self, cell):
        """
        Returns a set containing all the neighboring cells of cell
        """

        neighbors = set()
        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    neighbors.add((i, j))

        return neighbors
