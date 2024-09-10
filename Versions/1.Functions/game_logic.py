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


# The repeating part of the game loop has been put in a function
def handle_input(board, player):

    # Loop to keep asking the user for input until correct one is given
    while True:
        try:
            move = int(input(f'player {player}, make your move (1-9): '))
            board = write_to_board(move, board, player)
            break # Break out of the loop if a correct input is given

        # If the input given is invalid the loop will be repeated
        except ValueError: # Is executed only if an error has been thrown (could be done with an if statement aswell)
            print('Invalid input!')
            continue

    return board