<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/advices.css">
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
         Advices
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
          <form method="post" action="Advices">
            <fieldset>
              <legend>Please select what fits you the best:</legend>
              <div>
                <p>Age:</p>
                <input type="checkbox" id="age1" name="age1" value="teenager" >
                <label for="age1">Teenager</label>
          
                <input type="checkbox" id="age2" name="age2" value="adult" >
                <label for="age2">Adult</label>
          
                <input type="checkbox" id="age3" name="age3" value="elder" >
                <label for="age3">Elder</label>

                <br>
                <p>Ocupation:</p>
                <input type="checkbox" id="ocupation1" name="ocupation1" value="student" >
                <label for="ocupation1">Student</label>
          
                <input type="checkbox" id="ocupation2" name="ocupation2" value="employed" >
                <label for="ocupation2">Employed</label>
          
                <input type="checkbox" id="ocupation3" name="ocupation3" value="unemployed" >
                <label for="ocupation3">Unemployed</label>

                <br>
                <p>Context:</p>
                <input type="checkbox" id="context1" name="context1" value="academic" >
                <label for="context1">Academic</label>
          
                <input type="checkbox" id="context2" name="context2" value="job" >
                <label for="context2">Job</label>
          
                <input type="checkbox" id="context3" name="context3" value="free_time" >
                <label for="context3">Free time</label>

                <br>
                <p>In search for a new job:</p>
                <input type="checkbox" id="job1" name="job1" value="yes" >
                <label for="job1">Yes</label>
          
                <input type="checkbox" id="job2" name="job2" value="No" >
                <label for="job2">No</label>

                <br>
              </div>
              <div class="submit_button">
                <button type="submit">Submit</button>
              </div>
            </fieldset>
          </form>

          <div class="list_of_advices">
            <h2>List of advices:</h2>
            <ol>
              <?php
                for($i=0; $i<count($advices); $i++){
                  echo "<li>" . $advices[$i] . "</li>";
                }
              ?>
            </ol>
        </div>

      </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>