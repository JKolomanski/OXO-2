"""
OXO 2: Loner edition
This version is simillar to Deluxe but it features
a singleplayer gamemode, where one player plays against
a randomised computer-player.
"""

from random import randint

# Template to compare the input against
board_template = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))


# Ask what gamemode would the player like to play
def gamemode_selection():
    while True:
        choice = input('Please choose a gamemode, type:\n[1] for multiplayer\n[2] for singleplayer\n')

        if choice == '1':
            return 'multiplayer'
        elif choice == '2':
            return 'singleplayer'
        else:
            print("incorrect input, please type: '1' or '2' and press Enter")


# Ask which player the human should be
def get_human_player():
    while True:
        player = input('Which would you like to play as? (X/O): ').upper()

        if player == 'X' or player == 'O':
            return player
        else:
            print("Invalid player (please type 'X' or 'O' and press Enter)")
        

# Ask who should start tha game
def get_starting_player():
    while True:
        starting = input('Which player should start the game? (X/O): ').upper() # the upper method converts all letters in a string to uppercase

        if starting != 'X' and starting != 'O':
            print("Invalid player (please type 'X' or 'O' and press Enter)")
        else:
            return starting


# Display the current state of the board in terminal
def display_board(board):
    print()
    for rowIndex in range(len(board)):
        print(f'{board[rowIndex][0]} | {board[rowIndex][1]} | {board[rowIndex][2]}')

        if rowIndex < 2: # Don't print the dividing lines after the last row
            print('--+---+--')
    print()


# Modify the state of the board based on player's input
def write_to_board(move, board, template, player):
    for row in range(3):
        for col in range(3):
            if template[row][col] == str(move) and board[row][col] == ' ':
                board[row][col] = player
                return board
    raise Exception


# Check who the winner is / if it is a tie
def check_result(board):

    # Check for same rows
    for row in range(3):
        if board[row][0] != ' ' and (board[row][0] == board[row][1] == board[row][2]):
            return board[row][0]

    # Check for same columns
    for col in range(3):
        if board[0][col] != ' ' and (board[0][col] == board[1][col] == board[2][col]):
            return board[0][col]

    # Check for same diagonals
    if board[1][1] != ' ' and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1] # I forgot about this return statement, that's why it didn't work xd

    # Check for empty cells
    for row in board:
        for cell in row:
            if cell != 'X' and cell != 'O':
                return None # Return None if the game should still continue
    
    # It's a tie!
    return '='


# The repeating part of the game loop has been put in a function
def handle_input(board, player):

    # Loop to keep asking the user for input until correct one is given
    while True:
        try:
            move = input(f'Player {player}, make your move (1-9): ')
            if int(move) > 9 or int(move) < 1:
                raise ValueError
            board = write_to_board(move, board, board_template, player)
            break # Break out of the loop if a correct input is given

        # If the input given is invalid the loop will be repeated

        # Custom messages for different incorrect inputs (Improvement 4)
        except ValueError:
            print(f"Invalid input: spot '{move}' doesn't exist, you fool!")

        except Exception:
            print(f"Invalid input: spot '{move}' is already taken!")

    return board


# Modify the state of the board randomly
def computer_move(board, player):
    # Choose a random index for a row, then for a column, check if the chosen cell is empty,
    # if not, try again (This is a crude way of doing things that may cause the loop to run repeatedly
    # for no good reason, can you think of a better way?)
    while True:
        choiceRow = randint(0, 2)
        choiceCol = randint(0, 2)
        
        # Modify the chosen cell
        if board[choiceRow][choiceCol] == ' ':
            board[choiceRow][choiceCol] = player
            return board
        

# Ask if the user wants to continue playing (improvement 5)
def continue_playing():
    while True:

        continuePlaying = input('Do you want to play again? (Y/N): ').upper()
        if continuePlaying == 'Y':
            return True
        elif continuePlaying == 'N':
            return False

        else:
            print('Invalid input! Please try again')


# Display the starting message and ask the user to start the game
input('=== Welcome to OXO 2 ===\nPress Enter to START ')

# Loop containing the game loop and other functionalities
while True:

    # Define the initial state of the board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # Each list embeded in the main list represent a row, a value, a single cell

    gamemode = gamemode_selection()

    if gamemode == 'singleplayer':
        humanPlayer = get_human_player()
    
    player = get_starting_player()

    # Main game loop for multiplayer
    while gamemode == 'multiplayer':

        display_board(board)

        if check_result(board): # check_result(board) should be None, which means False, if there is no winner or the board hasn't been fully filled yet
            break # break out of the game loop if the game has ended

        board = handle_input(board, player)

        # Switch to the next player
        if player == 'X': player = 'O'
        else: player = 'X'

    # Game loop for singleplayer
    while gamemode == 'singleplayer':

        display_board(board)

        if check_result(board):
            break

        if player == humanPlayer:
            board = handle_input(board, player)

        else:
            board = computer_move(board, player)
            print("The computer has made it's move!")

        # Switch to the next player
        if player == 'X': player = 'O'
        else: player = 'X'


    # Display the result message
    print()
    if check_result(board) == '=':
        print("It's a tie!")

    else:
        print(f"Player {check_result(board)} won!")

    if not continue_playing(): break

print('Thank you for playing :)')
