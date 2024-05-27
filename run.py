import random

print("Welcome in Battleship Game!")

board = []
for i in range(0, 5):
    board.append(["-"] * 5)


def p_board__game(board):

    """ Creating game boar """


for row in board:
    print((" ").join(row))

print("Let's Play!")

p_board_game(board)


def run__row(board):

    """ random row for ship"""
    return random.randint(0, len(board) - 1)


def run__col(board):

    """ rundom column for a ship"""
    return random.randint(0, len(board[0]) - 1)


ship__row = run_row(board)


ship__col = run_col(board)


print(ship_row)
print(ship_col)

for turn in range(10):
    guess_row = int(input("Pick number from 0-4 for row: "))
    gues_col = int(input("Pick number from 0-4 for column: "))

    if guess_row == ship_row and gues_col == ship_col:
        print("you hit!")
        break
    else:
        if turn == 10:
            board[guess_row][gues_col] = "X"
            p_board_game(board)
            print('Game Over')
        else:
            if (guess_row > 4) or (gues_col > 4):
                print("Shot too far!")
            elif board[guess_row][gues_col] in 'OX':
                print("You guess that already!")
            else:
                print("You missed!")
                board[guess_row][gues_col] = "O"
            print("turns count:")
            print(turn + 1)
            p_board_game(board)
print("Game Over!")