from tictactoe import player, actions, result, winner, utility, minimax

X = 'X'
O = 'O'
EMPTY = None

board = [
    [EMPTY,     EMPTY,      X],
    [EMPTY,     X,      EMPTY],
    [O,     EMPTY,      EMPTY],
]

print(f"it is {player(board)}'s turn")
print(actions(board))
# print(result(board, (1, 0)))
print(f"winner is: {winner(board)}")
print(f"value of board is {utility(board)}")
minimax(board)

