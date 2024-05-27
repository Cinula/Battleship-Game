import random

print("Welcome in Battleship Game!")

board = []
for i in range(0, 5):
    board.append(["-"] * 5)

def p_board_game(board):
    """ 
    Creating game boar
    """
    for row in board:
        print((" ").join(row))

print("Let's Play!")

p_board_game(board)