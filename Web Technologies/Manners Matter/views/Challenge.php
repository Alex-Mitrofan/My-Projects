<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/challenge-option.css">
    <?php if ($avatar): ?>
    <style>
      .avatar{
          background-image:  url('data:image/png;base64,<?php echo $avatar; ?>');
        }
    </style>
    <?php endif; ?>
  </head>
  <body>
    <header>
      <div class="logo">
        <a href="Home">Manners Matter</a>
      </div>
      <div class="title">
         Challenge
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
          <section>
            <h1>
             Test yoursef!! 
            </h1>
            <div class="content">
            <img src="./views/images/chalenge.jpg" alt="challenge-image">
            <p>
              It is good practice to test your knowledge from time to time and this section is dedicated to this. Before we start, a few things must be mentioned. <br>
              You will take a test containing 7-10 questions, some with yes/no or full answers, is of different difficulty which can be set by ticking one of the options below (essay/medium/hard) or if you just want to practice the "practice" option.<br>
              After setting the difficulty press start and an automatic test will be loaded for which you have time unlimited answers. You have the opportunity
              give as many tests as you want 
                                                                   
            </p>
            <p class="attention" >
              !!! Attention!!!<br> 
              If the test is on a difficulty other than practice, its score will influence the position on the Ranking
            </p>
            </div>



            <div class="info-challenge">
            <form action="Quiz", method="POST">
            <input type="radio" id="Practice" name="Difficulty" value="Practice" checked>
            <label for="Practice">Practice</label>
            <input type="radio" id="Easy" name="Difficulty" value="Easy">
            <label for="Easy"> Easy </label>   
            <input type="radio" id="Medium" name="Difficulty" value="Medium">
            <label for="Medium"> Medium </label>
            <input type="radio" id="Hard" name="Difficulty" value="Hard">
            <label for="Hard"> Hard </label>  
            <span>
              <input class="start_button" type="submit" value="Start" onclick="location.href='Quiz';" style="width: 10em;">              

            </span>
            </form>
            </div>
          </section>
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>