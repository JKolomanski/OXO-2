ui <- htmlTemplate(
  text_ = "
  <!DOCTYPE html>
  <html>
  <head>
      <link rel='stylesheet' type='text/css' media='screen' href='main.css' />
      <title>OXO: Shiny edition</title>
      <script src='https://code.jquery.com/jquery-3.6.0.min.js'></script>
      <script>
        $(document).ready(function() {
          if (typeof Shiny !== 'undefined') {
            console.log('Shiny is loaded');
          } else {
            console.error('Shiny is NOT loaded');
          }

          Shiny.addCustomMessageHandler('updateButtonText', function(data) {
            console.log('Received message for:', data.id, 'with value:', data.value);
            let button = document.getElementById(data.id);
            if (button) {
              button.innerText = data.value;
            } else {
              console.error('Button not found:', data.id);
            }
          });
        });
      </script>
  </head>
  <body>
  
    <div class='topDiv'>
      <h1>☰☰☰ OXO ☰☰☰</h1>
      
      <div class='buttonsDiv'>
        <button id='aboutButton' class='pageButton'>About</button>
        <button id='playButton' class='pageButton'>Play</button>
        <button id='plotsButton' class='pageButton'>Plots</button>
      </div>
      
      <div class='gridDiv'>
        {{gridButtons}}
      </div>
      
    </div>
    
    <div class='bottomDiv'>
      <a href='https://jkolomanski.github.io' class='bottomText'>Jakub Kołomański | MMXXV</a>
    </div>
    
  </body>
  </html>
  ",
  gridButtons = do.call(
    tagList,
    lapply(1:9, function(i) {
      actionButton(inputId = paste0("btn_", i), label = "", class = "grid-button", `id` = paste0("btn_", i))
    })
  )
)
