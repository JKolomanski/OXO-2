library(shiny)
library(shinyjs) 

navbarPage(
  "OXO",
  
  tabPanel("Play",
           fluidPage(
             useShinyjs(),
             div(style = "display: flex; flex-direction: column; align-items: center; margin-top: 80px;",
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
                   
               div(style = "display: flex; margin-top: 60px;",
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
             titlePanel("About OXO"),
             p("OXO 2: Shiny edition is a simple tic-tac-toe game
               in the form of a web app built with Shiny."),
             
             p("It's a part of a bigger project 
               focused on making different versions of this simple game 
               with different technologies. "),
             
             tags$a(href = "https://github.com/JKolomanski/OXO-2", "GitHub repository", target = "_blank")
             
           )
          ),
  
  tabPanel("Plots",
           fluidPage(
             titlePanel("Plots"),
             div(style = "display: flex; margin: 5%; margin-top: 8%",
               plotOutput("wins_plot"),
               div(style = "width: 10%;"),
               plotOutput("starts_plot")
             )
           )
          ),
  
  div(style = "position: absolute; bottom: 0; left: 50%; width: 250px; transform: translateX(-58%); text-align: center; margin: 20px;", 
      hr(),
      tags$a(href = 'https://jkolomanski.github.io', 
             'Jakub Kołomański | MMXXV', target = '_blank'),
      
    )
)
