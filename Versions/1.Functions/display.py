# Display the current state of the board in terminal
def display_board(board):
    print()
    for row in board:
        print(f'{row[0]} | {row[1]} | {row[2]}')

        if row != board[2]: # Don't print the dividing lines after the last row
            print('--+---+--')
    print()