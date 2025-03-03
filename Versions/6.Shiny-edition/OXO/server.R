###################################################################
#                                                                 #
# OXO 2: Shiny edition                                            #
# A web app written with shiny with some additional functionality #
# currently W.I.P                                                 #
#                                                                 #
###################################################################

library(shiny)
library(shinyjs)
library(ggplot2)

function(input, output, session) {
  
  # Set the beggining value of game text
  output$game_txt = renderText({
    "Please select the starting player and begin the game"
  })
  
  board = reactiveVal(matrix(c('1', '2', '3', '4', '5', '6', '7', '8', '9'), nrow = 3, ncol = 3, byrow = TRUE))
  player = reactiveVal('X')
  result = reactiveVal(NULL)
  player_data = reactiveVal(read.csv("player_data.csv", header = TRUE, row.names = 1))
  starting_player = reactiveVal(NULL)
  
  
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
  
  
  # Apply a function to all buttons
  apply_all_buttons = function(func) {
    lapply(paste0("btn", 1:9), function(btn_id) {
      func(btn_id)
    })
  }
  
  
  # Change the color of button text according to player
  change_btn_color = function(btn_id) {
    current_player = player()
    
    if (current_player == 'X') {
      color = '#f7913b'
    } else {
      color = '#3e8bf7'
    }
    
    js_code = paste0("document.getElementById('", btn_id, "').style.color = '", color, "';")
    runjs(js_code)
    
  }
  
  
  # Save the data about the game to files
  save_result = function() {
    current_player = player()
    current_starting_player = starting_player()
    data = player_data()
    
    data[current_player, "wins"] = data[current_player, "wins"] + 1
    data[current_starting_player, "starts"] = data[current_starting_player, "starts"] + 1
    
    player_data(data)
    write.csv(data, "player_data.csv", row.names = TRUE)
  }
    
  
  # Render plots
  render_plots = function(type) {
    renderPlot({
      current_player_data = player_data()

      data_long = data.frame(Player = rownames(current_player_data), Value = current_player_data[[type]])
      
      ggplot(data_long, aes(x = Player, y = Value, fill = Player)) +
        geom_bar(stat = "identity") + 
        labs(title = paste('Number of', type), x = "Player", y = type) +
        theme_minimal() +
        scale_fill_manual(values = c("X" = "#b26c33", "O" = "#648fcb")) +
        scale_y_continuous(breaks = seq(0, max(data_long$Value, na.rm = TRUE), by = 1))
    })
  }
  
  
  # Reset the whole game
  reset = function() {
    apply_all_buttons(enable)
    
    clear_label = function(btn_id) {
      updateActionButton(session, btn_id, label = '')
    }
    
    apply_all_buttons(clear_label)
    board(matrix(c('1', '2', '3', '4', '5', '6', '7', '8', '9'), nrow = 3, ncol = 3, byrow = TRUE))
    selected_player = input$starting_option
    player(substring(selected_player, nchar(selected_player), nchar(selected_player)))
    result(NULL)
    change_game_txt()
  }
  
  
  # Handle press of the game buttons
  button_click = function(btn_id, player) {
    updateActionButton(session, btn_id, label = player)  # Change the button label
    change_btn_color(btn_id)
    
    write_to_board(substring(btn_id, nchar(btn_id), nchar(btn_id)), player)
    
    result(check_result())
    
    if (!is.null(result())) {
      apply_all_buttons(disable)
      save_result()
    }
    
    swap_player()
    
    disable(btn_id)
    change_game_txt()
    
  }
  
  
  # Behaviour of the game buttons
  lapply(paste0("btn", 1:9), function(btn_id) {
    observeEvent(input[[btn_id]], {

      button_click(btn_id, player())
    })
  })
  
  
  # Behaviour of the start / reset button
  observeEvent(input$btn_start, {
    updateActionButton(session, 'btn_start', label = 'RESET')  # Change the button label
    reset()
    starting_player(player())
  })
  
  
  # Disable all game buttons at the beggining
  apply_all_buttons(disable)
  
  
  # Render the plots
  output$wins_plot = render_plots("wins")
  output$starts_plot = render_plots("starts")
  
}