<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/profile.css">

    <?php if ($avatar): ?>
    <style>
      .profile_picture{
          background-image:  url('data:image/png;base64,<?php echo $avatar; ?>');
        }
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
         Profile
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
        
            
          <div class="profile_elements">
            <div class="upper_part">
              <div class="profile_picture">      
              </div>

              <a href="EditProfile">
                <button type="button" class="edit"> 
                  <span class="edit_icon">
                  </span>
                  Edit
              </button>
              </a>
             
            
            </div>
            <ul>
              <li><div class="username">Username: <?php echo $username; ?></div></li>
              <li><div class="rank">Rank: <?php echo $rank; ?></div></li>
              <li><div class="score">Score: <?php echo $score; ?>xp</div></li>
              <li><div class="name">Name: <?php echo $name; ?></div></li>
              <li><div class="location">Location: <?php echo $location; ?></div></li>
              <li><div class="age">Age: <?php echo $age; ?></div></li>
              <li><div class="sex">Sex: <?php echo $sex; ?></div></li>
              <li><div class="ocupation">Occupation: <?php echo $ocupation; ?></div></li>
            </ul>

            <form action="Export" method="post">
              <button type="submit" class="export">
                Export Data
            </button>  
           </form>
          </div>
         
        </div>
       


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>