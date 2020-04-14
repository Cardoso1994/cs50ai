"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    if terminal(board):
        return (42)

    for row in board:
        for value in row:
            if value is X:
                count_x += 1
            elif value is O:
                count_o += 1

    if count_x == count_o:
        return (X)

    return (O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    if terminal(board):
        return (42)

    for indx_row, row in enumerate(board):
        for indx_val, val in enumerate(row):
            if val is None:
                moves.add((indx_row, indx_val))

    return (moves)

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(action)
    board_ = deepcopy(board)
    if board_[action[0]][action[1]] == EMPTY:
        board_[action[0]][action[1]] = player(board)
    else:
        raise ValueError

    return(board_)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    diagonal_0 = [board[0][0], board[1][1], board[2][2]]
    diagonal_1 = [board[0][2], board[1][1], board[2][0]]

    # check winner in rows
    for row in board:
        if all(val == X for val in row):
            return X
        if all(val == O for val in row):
            return O

    # check winner in columns
    for i in range(3):
        if all(val[i] == X for val in board):
                return X
        if all(val[i] == O for val in board):
                return O

    # check winner in diagonals
    if all(val == X for val in diagonal_0) \
            or all(val == X for val in diagonal_1):
        return X

    if all(val == O for val in diagonal_0) \
            or all(val == O for val in diagonal_1):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True

    if all(val != EMPTY for row in board for val in row):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    util = {X: 1, O: -1, EMPTY: 0}

    return util[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # base case
    if terminal(board):
        return None

    # get the player to move
    player_ = player(board)

    # get possible actions
    actions_ = actions(board)

    if player is X:
        _maximize(board, actions_)

    else:
        _minimize(board, actions)



def _maximize(board, actions):
    """
    tries to maximize the score of the game
    Returns the best possible outcome, 1, 0 or -1, in that order
    """
    best = (-math.inf, ())

    for action_ in actions:
        current_board = result(board, action_)
        if terminal(current_board):
            return (utility(current_board), action_)

        actions_min = actions(current_board)
        result_min = _minimize(current_board, actions_min)

        if result_min[0] == 1:
            return (1, action_)
        elif result_min[0] > best[0]:
            best = (result_min[0], action_)



def _minimize:
    """
    tries to minimize the score of the game
    """
    pass
