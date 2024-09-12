"""
OXO 2
Remake of a simple, terminal-based
tic-tac-toe game made in Python a while back.
For educational purposes.
"""

# Define the initial state of the board
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# Each list embeded in the main list represent a row, a value a single cell


# Display the current state of the board in terminal
def display_board(board):
    print()
    for row in board:
        print(f'{row[0]} | {row[1]} | {row[2]}')

        if row != board[2]: # Don't print the dividing lines after the last row
            print('--+---+--')
        # There exists an edgecase which can break this part of the code and the lines won't display properly,
        # can think of what it is?
    print()


# Modify the state of the board based on player's input
def write_to_board(move, board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == str(move):
                board[row][col] = player
                return board
    raise ValueError


# Check who the winner is / if it is a tie
def check_result(board):

    # Check for same rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Check for same columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check for same diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1] # I forgot about this return statement, that's why it didn't work xd

    # Check for empty cells
    for row in board:
        for cell in row:
            if cell != 'X' and cell != 'O':
                return None # Return None if the game should still continue
    
    # It's a tie!
    return '='


# Display the starting message and ask the user to start the game
input('=== Welcome to OXO 2 ===\nPress Enter to START ')

# Main game loop
while True:

    display_board(board)
    if check_result(board): # check_result(board) should be None, which means False, at the begginig
        break # break out of the game loop if the game has ended

    # Loop to keep asking the user for input until correct one is given
    while True:
        try:
            move = int(input('player X, make your move (1-9): '))
            board = write_to_board(move, board, 'X')
            break # Break out of the loop if a correct input is given

        # If the input given is invalid the loop will be repeated
        except ValueError: # Is executed only if an error has been thrown (could be done with an if statement aswell)
            print('Invalid input!')
    
    display_board(board)
    if check_result(board):
        break

    # Repeat for a second player (could be put in a function instead of repeating code)
    while True:
        try:
            move = int(input('player O, make your move (1-9): '))
            board = write_to_board(move, board, 'O')
            break

        except ValueError:
            print('Invalid input!')

# Display the result message
print()
if check_result(board) == '=':
    print("It's a tie!")

else:
    print(f"Player {check_result(board)} won!")

print('Thank you for playing :)')

