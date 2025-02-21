# OXO 2: R edition
# Regular verison of OXO 2 rewritten in R

# Define the initial state of the board
board = matrix(data = c('1', '4', '7', '2', '5', '8', '3', '6', '9'), nrow=3, ncol=3, FALSE)
possible_moves = c('1', '4', '7', '2', '5', '8', '3', '6', '9')


# Clear the console accordingly to the enviroment
clear_console = function() {
  sys_info = Sys.info()

  if (!is.null(sys_info)) {
    system_type = sys_info['sysname']
    
    if (system_type == "Darwin" || system_type == "Linux") {
      system('clear')  # For macOS and Linux
      
    } else  {
      cat("\014")  # For Windows and non-interactive enviroments
    }
    
  } else {
    cat("\014") # For non-interactive environments
  }
}


# Display the current state of the board in terminal
display_board = function(board) {
  clear_console()
  
  # cat('\n')
  for (row in 1:nrow(board)) {
    
  cat(paste(board[row, 1], board[row, 2], board[row, 3], sep=' ┃ '))
  if (row != 3) {cat('\n━━╋━━━╋━━\n')} # Don't print the dividing lines after the last row
  }
  cat('\n\n')
}


# Modify the state of the board based on players input
write_to_board = function(move, board, player) {
  for (row in 1:nrow(board)) {
    for (col in 1:ncol(board)) {

      if (board[row, col] == move) {
        board[row, col] = player
      }
    }
  }
  board
}


# Check who the winner is / if it is a tie
check_result = function(board) {
  for (i in 1:nrow(board)) {
    
    # Check for same rows
    if (length(unique(board[i, ])) == 1) {
      return(board[i, 1])
    }
    
    # Check for same columns
    if (length(unique(board[, i])) == 1) {
      return(board[1, i])
    }
  }
  
  # Check for same diagonals
  if (length(unique(diag(board))) == 1 || length(unique(board[cbind(1:3, 3:1)])) == 1) {
    return(board[2, 2])
  }
  
  # Check for empty cells
  for (row in 1:nrow(board)) {
    for (col in 1:ncol(board)) {
      if (board[row, col] != 'X' && board[row, col] != 'O') {
        return(NULL)
      }
    }
  }
  
  # It's a tie!
  return('=')
}


# Get user input in the correct way depending on whether the program is running
# in interactive or non-interactive mode
user_input = function(prompt) {
  if (interactive()) {
    return(readline(prompt))
  } else {
    cat(prompt)
    return(readLines("stdin", n=1))
  }
}


# Display the starting message and ask the user to start the game
clear_console()
invisible(user_input('=== Welcome to OXO 2: R edition ===\nPress Enter to START '))



# Main game loop
while (TRUE) {
  
  display_board(board)
  if (!is.null(check_result(board))) { # if check_result(board) is not null, end the game
    break
  }
  
  # Loop to keep asking the user for input until correct one is given
  while (TRUE) {
    move = user_input('Player X, make your move (1-9): ')
    
    if (move %in% board && move %in% possible_moves) {
      board = write_to_board(move, board, 'X')
      break
      
    } else {
      cat('Invalid input!\n')
    }
  }
  
  display_board(board)
  if (!is.null(check_result(board))) { # if check_result(board) is not null, end the game
    break
  }
  
  # Repeat for a second player (could be put in a function instead of repeating code)
  while (TRUE) {
    move = user_input('Player O, make your move (1-9): ')
    
    if (move %in% board && move %in% possible_moves) {
      board = write_to_board(move, board, 'O')
      break
      
    } else {
      cat('Invalid input!\n')
    }
  }
}


# Display the result message
display_board(board)
if (check_result(board) == '=') {
  cat("It's a tie!")
} else {
  cat(paste('Player', check_result(board), 'won!', sep=' '))
}

cat('\nThank you for playing :)\n')