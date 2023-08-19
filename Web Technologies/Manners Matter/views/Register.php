<?php
  $username = false;  
   
  if (isset($_COOKIE['wrong_username'])) {
    if($_COOKIE["wrong_username"] == 'True')
      $username = true;  
      
  }

  $password = false;  
 
  if (isset($_COOKIE['wrong_password'])) {
    if($_COOKIE["wrong_password"] == 'True')
      $password = true;  
  }


?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/login.css">
  </head>
  <body>
    <header>
      <div class="logo">
        <a href="Home">Manners Matter</a>
      </div>
      <div class="title">
        Register
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
            <div class="signin_box">
                <h1>Register</h1>
                <form method="post" action="Register">
                    <?php if ($username) : ?>
                      <div>
                          <p style="color: red;">Username already used. Try another one!</p>
                      </div>
                    <?php endif; ?>
                    <div class="field">
                        <label>Username</label>
                        <input id="username" name="username" type="text" required >
    
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <input id="password" name="password" type="password" required >
    
                    </div>
                    <div class="field">
                        <label>Repeat your password</label>
                        <input id="repeat_password" name="repeat_password" type="password" required >
    
                    </div>
                    <div class="field">
                        <label>First name</label>
                        <input id="first_name" name="first_name" type="text">
    
                    </div>
                    <div class="field">
                        <label>Last name</label>
                        <input id="last_name" name="last_name" type="text">
    
                    </div>
                     
                    <input id="submit" name="submit" type="submit" value="Register" >
                    <?php if ($password) : ?>
                      <div>
                          <p style="color: red;">Wrong password!</p>
                      </div>
                    <?php endif; ?>
    
                </form>
            </div>
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>