<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/quiz.css">
    <link rel="stylesheet" href="./views/styles/style.css">
  </head>
  <body>
    <header>
        <div class="logo">
          <a href="Home">Manners Matter</a>
        </div>
        <div class="title">
           Result
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
            <?php
            echo '<div style="text-align: center;">';
            echo '<h2>Performance</h2>';
            echo '<p> Difficulty mode: '.$info['mode'];
            echo "<p>Good answers: $nr_corect_answerd";
            echo "<p>Wrong answers:".(5-$nr_corect_answerd);
            echo '<p>Old Score: ' . $info['old_score'] . '</p>';
            echo '<p>New Score: ' . $info['new_score'] . '</p>';
            echo '<p>Old Rank: ' . $info['old_rank'] . '</p>';
            echo '<p>New Rank:'.$info ['new_rank'] . '</p>';
            echo '<p>Username: ' . $info['username'] . '</p>';
            echo '</div>';
            
            // Back to home button
            echo '<div style="text-align: center; margin-top: 20px;">';
            echo '<a href="Home" style="background-color: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 4px; text-decoration: none;">Back to Home Page</a>';
            echo '</div>';
            ?>
          </section>
          </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>