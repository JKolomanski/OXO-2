library(shiny)
library(shinyjs) 

navbarPage(
  "OXO",
  
  tabPanel("Play",
           fluidPage(
             useShinyjs(),
             div(style = "display: flex; flex-direction: column; align-items: center;",
               titlePanel("Welcome to OXO"),
               
           # game text
           textOutput('game_txt'),
               
                   
           # Row 1
           div(style = "display: flex; margin-top: 30px;",
               actionButton("btn1", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn2", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn3", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;")
           ),
                   
           # Row 2
           div(style = "display: flex;",
               actionButton("btn4", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn5", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn6", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;")
           ),
           
           # Row 3
           div(style = "display: flex;",
               actionButton("btn7", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn8", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;"),
               actionButton("btn9", "", style = "width:80px; height:80px; font-size: 24px; margin: 5px;")
           ),
               
           div(style = "display: flex; margin-top: 30px;",
           selectInput("starting_option", "Starting Player:", 
                       choices = c("Player X", "Player O"), 
                       selectize = FALSE, width = "125px"),
           actionButton("btn_start", "START", style = "width:125px; height:34px; font-size: 12px; margin: 5px; margin-top: 25px;margin-right: 1px;")
           ),

           
             )
           )
  ),
  
  tabPanel("About",
           fluidPage(
             titlePanel("About"),
             textInput("name", "Podaj swoje imię:", ""),
             actionButton("start", "Rozpocznij grę")
           )
  ),
  
  tabPanel("Plots",
           fluidPage(
             titlePanel("Plots"),
             p("WORK IN PROGRESS")
           )
  )
)
