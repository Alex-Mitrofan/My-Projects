<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/contact.css">
    <?php if(isset($_COOKIE["username"]) == True ): if ($avatar): ?>
    <style>
      .avatar{
          background-image:  url('data:image/png;base64,<?php echo $avatar; ?>');
        }
    </style>
    <?php endif; endif;?>
  </head>
  <body>
    <header>
      <div class="logo">
        <a href="Home">Manners Matter</a>
      </div>
      <div class="title">
         Contact
      </div>
      <div class="profile">
        <div class="username">
          <a href="Login">Login</a>
        </div>
        <div class="dropdown_profile">
          <div class="avatar">
          </div>

          <div class="dropdown_content">
            <a href="Profile">My Profile</a>
            <a href="Logout">Logout</a>
          </div>
        </div>
      </div>
  </header>
    <main>
      <nav>
        <ul>
          <li>
            <a href="Home">Home</a>
          </li>
          <li>
            <a href="Profile">Profile</a>
          </li>
          <li>
            <a href="Advices">Advices</a>
          </li>
          <li>
            <a href="Challenge">Challenge</a>
          </li>
          <li>
            <a href="Ranking">Ranking</a> 
          </li>
          <li>
            <a href="About">About</a>
          </li>
          <li>
            <a href="Contact">Contact</a>
          </li>
        </ul>
      </nav>
      
        
        <div class="div_articles">
          <h4>Have any questions or want to give us a feedback? We'd love to hear from you!</h4>
          <form action="Contact" method="POST">
            <label for="email">Type your email address:</label><br>
            <input class="email_box" type="email" id="email" name="email" value="email" required><br>

            <label for="message">Type your message:</label><br>
            <input class="input_box" type="text" id="message" name="message" value="feedback_message" required><br>
            
            <div class="submit_button">
              <button  type="submit">Submit</button>
            </div>
          </form> 
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>