import random

# Constants

BOARD_SIZE = 5
SHIPS_COUNTER = 3
SHOTS = 10

# Create the board

board = [['-'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
print(" ")
print("Welcome to Battleship Game!")
print("Pleas type in your name and press Enter to start!")
print(" ")
player_name = input("What is your name Capitan ?: ")


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
        row = int(input(f"Capitan {player_name} Fire Row (0-4): "))
        col = int(input(f"Capitan {player_name} Fire Column (0-4): "))
        return row, col
    except ValueError:
        print(f"{player_name} Please enter valid integers.")
        return get_player_guess()


def check_guess(guess, ships):

    """ Game checks if was hit or miss"""

    if guess in ships:
        ships.remove(guess)
        return f"Hit! Capitan {player_name} We sank enemi shop hury!"
    else:
        return f"Miss! Capitn {player_name}: preper canons!"


def update_board(board, guess, result):

    """ Updeting game board with miss or hit"""

    row, col = guess
    if result == "Hit!":
        board[row][col] = "x"
    else:
        board[row][col] = "O"


def main():

    """ This is main game engine """

    ships = place_ships(board, SHIPS_COUNTER)

    print("x" * 25)
    print(" ")
    print("1.You have 10 Turns (shots)\nto destroy all\nenemies battleships!")
    print("2.Below the game board you see guess row option")
    print("pick the row number from 0 to 4")
    print("automaticly shows you another option to choose column")
    print("Please pick columnt number\nfrom 0 - 4 ")
    print(f"3.Game board shows 'O' for miss and 'X' for hit")
    print("4.Under game board you can see Game counter")
    print(f"How meny turens you made\nBest of Luck! {player_name}")
    print(" ")
    print("x" * 25)
    print(f"Capitan {player_name}, there is an Enemy ships nearby!")
    print("Preper Cannons ")
    print("aye aye Capitan")
    print("Canons ready to fire!")
    print_board(board)
    # print(ships)
    turns = 0
    while turns < SHOTS and ships:
        guess = get_player_guess()
        if 0 <= guess[0] < BOARD_SIZE and 0 <= guess[1] < BOARD_SIZE:
            result = check_guess(guess, ships)
            update_board(board, guess, result)
            print(result)
        else:
            print(f"{player_name} Too far. Try again.")
        print_board(board)
        turns += 1
        print(f"{player_name} Your heve: {SHOTS} shots")
        print(f"Your ammunition counter: {turns}")
    if not ships:
        print(f"Capitan {player_name} Congratulations! You sunk all enemy ships!")
    else:
        print(f"{player_name} Game Over . You ran out of ammunition.")
        print("Ships were at:", ships)


if __name__ == "__main__":
    main()
