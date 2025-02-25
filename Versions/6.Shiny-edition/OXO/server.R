####################################################################
#                                                                  #
# OXO 2: Shiny edition                                             #
# A web app written with shiny  with some additional functionality #
# currently W.I.P                                                  #
#                                                                  #
####################################################################

library(shiny)
library(shinyjs)

function(input, output, session) {
  
  # Set the beggining value of game text
  output$game_txt <- renderText({
    "Player X begins!"
  })
  
  board = reactiveVal(matrix(c('1', '2', '3', '4', '5', '6', '7', '8', '9'), nrow = 3, ncol = 3, byrow = TRUE))
  player = reactiveVal('X')
  result = reactiveVal(NULL)
  
  
  # Write the move to the board
  write_to_board = function(move, player) {
    current_board = board()
    for (row in 1:nrow(current_board)) {
      for (col in 1:ncol(current_board)) {
        if (current_board[row, col] == move) {
          current_board[row, col] = player
        }
      }
    }
    board(current_board)
  }
  
  
  # Change the current player
  swap_player = function() {
    current_player = player()
    if (current_player == 'X') {
      player('O')
    } else {
      player('X')
    }
  }
  
  
  # Check who the winner is / if it is a tie
  check_result = function() {
    current_board = board()
    
    for (i in 1:nrow(current_board)) {
      
      # Check for same rows
      if (length(unique(current_board[i, ])) == 1 && current_board[i, 1] != ' ') {
        return(current_board[i, 1])
      }
      
      # Check for same columns
      if (length(unique(current_board[, i])) == 1 && current_board[1, i] != ' ') {
        return(current_board[1, i])
      }
    }
    
    # Check for same diagonals
    if ((length(unique(diag(current_board))) == 1 || length(unique(current_board[cbind(1:3, 3:1)])) == 1) && current_board[2, 2] != ' ') {
      return(current_board[2, 2])
    }
    
    # Check for empty cells
    for (row in 1:nrow(current_board)) {
      for (col in 1:ncol(current_board)) {
        if (current_board[row, col] != 'X' && current_board[row, col] != 'O') {
          return(NULL)
        }
      }
    }
    
    # It's a tie!
    return('=')
  }
  
  # Change the text above the playfield
  change_game_txt = function() {
    current_result = result()
    
    if (is.null(current_result)) {
      output$game_txt = renderText({
        paste('Player', player(), ', make your move', sep=' ')
      })
    } else if (current_result == '=') {
      output$game_txt = renderText({
        "It's a tie!"
      })
    } else {
      output$game_txt = renderText({
        paste('Player', result(), ' Won!', sep=' ')
      })
    }
  }
  
  
  # Disable all buttons
  disable_all = function() {
    lapply(paste0("btn", 1:9), function(btn_id) {
      disable(btn_id)
    })
  }
  
  
  # Handle press of the game buttons
  button_click = function(btn_id, player) {
    updateActionButton(session, btn_id, label = player)  # Change the button label
    
    write_to_board(substring(btn_id, nchar(btn_id), nchar(btn_id)), player)
    print(board) # REMOVE ME LATER
    
    swap_player()
    
    disable(btn_id)
    
    result(check_result())
    print(result)
    change_game_txt()
    
    if (!is.null(result())) {
      disable_all()
    }
  }
  
  
  # apply the button_click to all game buttons
  lapply(paste0("btn", 1:9), function(btn_id) {
    observeEvent(input[[btn_id]], {

      button_click(btn_id, player())
    })
  })
}