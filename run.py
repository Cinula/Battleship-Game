import random

# Main Variable 

GAME_BOARD_SIZE = 5
SHIPS_COUNTER = 3
SHOTS = 10

# Creating Game board 

board = [["-"] * GAME_BOARD_SIZE for _ in range(GAME_BOARD_SIZE)]

def print_board(board):

    """ Creating game board """

    for row in board:
        print(' '.join(row))

def place_ships(board, num_ships):

    """ Placeing ships randomly on game board """

    ships = []
    while len(ships) < num_ships:
        row = random.randint(0, GAME_BOARD_SIZE - 1)
        col = random.randint(0, GAME_BOARD_SIZE - 1)
        if (row, col) not in ships:
            ships.append((row,col))
    return(ships)

def get_player_guess():
    
    """ Function for player to shoot """

