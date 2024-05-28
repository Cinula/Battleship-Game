import random

print("Welcome in Battleship Game!\nGood Luck!\n")

class BattleshipField:

    """ Creating class game board for battleship game """

    def __init__(self, boar):
        self.board = board

    def get_numbers_paired_to_letters():
        numbers_paired_to_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return numbers_paired_to_letters
    
    def print_board(self):
        print("  A B C D E F G H")
        row_n = 1
        for row in self.board:
            print("%d|%s|" % (row_n, "|".join(row)))
            row_n += 1 


class Battleship:

    def __init__(self, board):
        self.board = board
    
    def creating_ships(self):
        for i in range(5):
            self.r_row, self.c_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.r_row][self.c_column] == "X":
                self.r_row, self.c_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.r_row][self.c_column] = "X"
        return self.board




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