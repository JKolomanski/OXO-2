ui <- htmlTemplate(
  text_ = "
  <!DOCTYPE html>
  <html>
  <head>
      <link rel='stylesheet' type='text/css' media='screen' href='main.css' />
      <title>OXO: Shiny edition</title>
  </head>
  <body>
  
    <div class='topDiv'>
      <h1>☰☰☰ OXO ☰☰☰</h1>
      
      <div class='buttonsDiv'>
      <button id='myButton'>Play</button>
      <button id='myButton'>Stats</button>
      <button id='myButton'>About</button>
      </div>
    </div>
    
    <div class='bottomDiv'>
      <a href='https://jkolomanski.github.io' class='bottomText'>Jakub Kołomański | MMXXV</a>
    </div>
    
  </body>
  </html>
  "
)