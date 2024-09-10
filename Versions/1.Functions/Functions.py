"""
OXO 2: Functions
This version limits the duplicating of code by
putting the loops responsible for receiving correct input
in a function. 

It also has the functions in seperate files, 
which is not a great idea for a project this small.
It's done just for educational purposes.
"""

from display import display_board
from game_logic import check_result, handle_input

# Define the initial state of the board
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# Each list embeded in the main list represent a row, a value a single cell

# Display the starting message and ask the user to start the game
input('=== Welcome to OXO 2 ===\nPress Enter to START ')

# Main game loop
while True:

    display_board(board)

    if check_result(board): # check_result(board) should be None, which means False, if there is no winner or the board hasn't been fully filled yet
        break # break out of the game loop if the game has ended

    board = handle_input(board, 'X')
    
    display_board(board)

    if check_result(board):
        break
    
    board = handle_input(board, 'O')

# Display the result message
print()
if check_result(board) == '=':
    print("It's a tie!")

else:
    print(f"Player {check_result(board)} won!")

print('Thank you for playing :)')

