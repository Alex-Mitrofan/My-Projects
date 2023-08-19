<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/about.css">
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
         About
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
        <div class="About-us">   
        <h1>About us!!</h1>
        
        <h2>Where the idea comes from and when it start?</h2>
        <p>
          We all know that having something is an asset for your career and in life in general, and on the street people behave
          as they normally do, you rarely see someone yelling or monkeying around, but in the online environment 
          there are no limits and this was very visible during the quarantine period.And the idea here came to educate people in a fun way how to behave in 
          the online environment.
        </p>
        <h2>What is the role of this site and what you can do in it?</h2>
        <p>The role of this web application is to provide users with information about manners in the online environment, to offer them 
          personalized advice based on their needs and to test their knowledge gained from reading the informative materials 
          provided. The application has a section with the ranking of the best users, its purpose being to motivate them to put into practice 
          the information learned 
          through the tests in the related section.</p>
        <h2>State of the site</h2> 
        <p>The site is fully functional, and more articles and new functionalities will be added along the way.</p>
        <h2>The team behind</h2>
        <p>Mitrofan Alexandru</p>
        <p>Ciocan Alexandru</p>
        </div>
        </section>
       </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>