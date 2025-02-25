server <- function(input, output, session) {
  button_states <- reactiveValues(
    btn_1 = "", btn_2 = "", btn_3 = "",
    btn_4 = "", btn_5 = "", btn_6 = "",
    btn_7 = "", btn_8 = "", btn_9 = ""
  )
  
  observe({
    for (i in 1:9) {
      observeEvent(input[[paste0("btn_", i)]], {
        btn_id <- paste0("btn_", i)
        current_value <- button_states[[btn_id]]
        
        # Toggle between "", "X", and "O"
        new_value <- ifelse(current_value == "", "X",
                            ifelse(current_value == "X", "O", ""))
        
        button_states[[btn_id]] <- new_value
        
        # Debugging: Print new value
        print(paste("New value:", new_value))
        
        # Use JavaScript to directly update button text
        session$sendCustomMessage(type = "updateButtonText", list(id = btn_id, value = new_value))
      }, ignoreInit = TRUE)
    }
  })
}