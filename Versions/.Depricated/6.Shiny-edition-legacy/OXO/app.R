library(shiny)

# Source UI and server logic from external files
source("ui.R")
source("server.R")

# Create the Shiny app
shinyApp(ui = ui, server = server)