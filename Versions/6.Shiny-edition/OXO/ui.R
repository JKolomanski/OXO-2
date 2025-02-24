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
      <button id='myButton' class='pageButton'>About</button>
      <button id='myButton' class='pageButton'>Play</button>
      <button id='myButton' class='pageButton'>Plots</button>
      </div>
      
      <dic class='fieldDiv'>
          <button class='grid-button'>X</button>
          <button class='grid-button'>O</button>
          <button class='grid-button'>X</button>
          <button class='grid-button'>O</button>
          <button class='grid-button'>X</button>
          <button class='grid-button'>O</button>
          <button class='grid-button'>X</button>
          <button class='grid-button'>O</button>
          <button class='grid-button'>X</button>
      </div>
      
    </div>
    
    <div class='bottomDiv'>
      <a href='https://jkolomanski.github.io' class='bottomText'>Jakub Kołomański | MMXXV</a>
    </div>
    
  </body>
  </html>
  "
)