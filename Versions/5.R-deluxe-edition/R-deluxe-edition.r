# OXO 2: R deluxe
# OXO 2: deluxe rewritten in R with all it's features except custom error messages


# Clear the console accordingly to the enviroment
clear_console = function() {
  sys_info = Sys.info()
  
  if (!is.null(sys_info)) {
    system_type = sys_info['sysname']
    
    if (system_type == "Darwin" || system_type == "Linux") {
      system('clear')  # For macOS and Linux
      
    } else  {
      cat("\014")  # For Windows
    }
    
  } else {
    cat("\014") # For non-interactive environments
  }
}


# Get user input in the correct way depending on whether the program is running
# in interactive or non-interactive mode
user_input = function(prompt) {
  if (interactive()) {
    return(toupper(readline(prompt)))
  } else {
    cat(prompt)
    return(toupper(readLines("stdin", n=1)))
  }
}


# Ask who should start the game
get_starting_player = function() {
  while (TRUE) {
    starting = user_input('\nWhich player should start the game? (X/O): ')
    
    if (starting == 'X' || starting == 'O') {
      return(starting)
    }
    
    cat("Invalid input! Please try again\n")
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
  cat('\n')
}


# Modify the state of the board based on players input
write_to_board = function(move, board, possible_moves, player) {
  for (row in 1:nrow(board)) {
    for (col in 1:ncol(board)) {
      
      if (possible_moves[row, col] == move) {
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
    if (length(unique(board[i, ])) == 1 && board[i, 1] != ' ') {
      return(board[i, 1])
    }
    
    # Check for same columns
    if (length(unique(board[, i])) == 1 && board[1, i] != ' ') {
      return(board[1, i])
    }
  }
  
  # Check for same diagonals
  if ((length(unique(diag(board))) == 1 || length(unique(board[cbind(1:3, 3:1)])) == 1) && board[2, 2] != ' ') {
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


handle_input = function(board, possible_moves, player) {
  while (TRUE) {
    move = user_input(paste('\nPlayer', player, ', make your move (1-9): ', sep=' '))
    
    if (move %in% possible_moves && move != ' ') {
      board = write_to_board(move, board, possible_moves, player)
      possible_moves[which(possible_moves == move, arr.ind = TRUE)] = ' '
      return(list(board, possible_moves))
      
    } else {
      cat('Invalid input!\n')
    }
  }
}


# Ask if the user wants to continue playing
continue_playing = function() {
  while (TRUE) {
    continuePlaying = user_input('\nDo you want to play again? (Y/N): ')
    
    if (continuePlaying == 'Y') {
      return(TRUE)
    } else if (continuePlaying == 'N') {
        return(FALSE)
    } else {
        cat("Invalid input! Please try again\n")
    }
  } 
}


# Display the starting message and ask the user to start the game
clear_console()
invisible(user_input('=== Welcome to OXO 2: R deluxe edition ===\nPress Enter to START '))


# Loop containing the game loop and other functionalities
while (TRUE) {
  
  # Define the initial state of the board
  board = matrix(data = c(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '), nrow=3, ncol=3, FALSE)
  # Define the possible moves template
  possible_moves = matrix(data = c('1', '4', '7', '2', '5', '8', '3', '6', '9'), nrow=3, ncol=3, FALSE)
  
  player = get_starting_player()
  
  # Main game loop
  while(TRUE) {
    
    display_board(board)
    
    if (!is.null(check_result(board))) { # if check_result(board) is not null, end the game
      break
    }
    
    result_vec = handle_input(board, possible_moves, player)
    board = result_vec[[1]]
    possible_moves = result_vec[[2]]
    
    # Switching to the next player
    if (player == 'X') {player = 'O'}
    else {player = 'X'}
  }
  
  # Display the result message
  display_board(board)
  if (check_result(board) == '=') {
    cat("It's a tie!")
  } else {
    cat(paste('\nPlayer', check_result(board), 'won!', sep=' '))
  }
  
  if (!continue_playing()) {
    break
  }
}

cat('\nThank you for playing :)\n')