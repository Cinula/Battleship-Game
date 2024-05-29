import random


# Constants

BOARD_SIZE = 5
SHIPS_COUNTER = 3
SHOTS = 10

# Create the board

board = [['-'] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def print_board(board):

    """creating game board"""

    for row in board:
        print(' '.join(row))

def place_ships(board, num_ships):

    """ Placeing ships on the board """
    
    ships = []
    while len(ships) < num_ships:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if (row, col) not in ships:
            ships.append((row, col))
    return ships

def get_player_guess():
    
    """ Function for player to choose where to shoot"""
    
    try:
        row = int(input("Guess Row (0-4): "))
        col = int(input("Guess Column (0-4): "))
        return row, col
    except ValueError:
        print("Please enter valid integers.")
        return get_player_guess()

def check_guess(guess, ships):

    """ Game checks if was hit or miss"""

    if guess in ships:
        ships.remove(guess)
        return "Hit!"
    else:
        return "Miss!"

def update_board(board, guess, result):

    """ Updeting game board with miss or hit"""

    row, col = guess
    if result == "Hit!":
        board[row][col] = "X"
    else:
        board[row][col] = "O"

def main():

    """ This is main game engine """

    ships = place_ships(board, SHIPS_COUNTER)
    print("Welcome to Battleship!")
    print("x" * 25)
    print("1.You have 10 Turns (shots)\nto destroy all\nenemies battleships!")
    print("2.Below the game board you\nsee guess row option\npick the row number from 0 to 4\nautomaticly shows you another option\nto choose column\nPlease pick columnt number\nfrom 0 - 4 ")
    print("3.Game board shows 'O' for miss and 'X' for hit.\n4.Under game board you can see\nGame counter\nHow meny turens you made\nBest of Luck!" )
    print("x" * 25)
    print_board(board)
    turns = 0
    while turns < SHOTS and ships:
        guess = get_player_guess()
        if 0 <= guess[0] < BOARD_SIZE and 0 <= guess[1] < BOARD_SIZE:
            result = check_guess(guess, ships)
            update_board(board, guess, result)
            print(result)
        else:
            print("Out of bounds. Try again.")
        print_board(board)
        turns += 1
        print(f"Your heve: {SHOTS} turns\nYour turns counter: {turns}" )
    if not ships:
        print("Congratulations! You sunk all the ships!")
    else:
        print("Game Over. You ran out of turns.")
        print("Ships were at:", ships)
if __name__ == "__main__":
    main()
