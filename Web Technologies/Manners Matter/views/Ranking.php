<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles/style.css">
    <link rel="stylesheet" href="./views/styles/ranking.css">
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
        Ranking
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
          <section class="best-ones">
            <div id="Score">
            <h1>Score Board</h1> 
            </div>

          <div class="podium">  
            <div class="podium_image">
              <div id="container-places"> 
                <div class="second-place">
                  <?php 
                  echo '<div class="second_place_image" style="background-image: url(\'data:image/jpeg;base64,' . base64_encode($best_of_3[2]["avatar"]) . '\');">';
                  ?>
                </div>
                <p style="margin-top: -0.2em; margin-right: 1.2em;">
                  <?php
                   echo $best_of_3[2]["username"] ;
                  ?>
                </p>
                </div>
  
                <div class="first-place">
                  <?php 
                  echo '<div class="first_place_image" style="background-image: url(\'data:image/jpeg;base64,' . base64_encode($best_of_3[1]["avatar"]) . '\');">';
                  ?>
                  </div>
                  <p style="margin-right:4em ;">
                  <?php
                    echo $best_of_3[1]["username"] ;
                   ?>
                  </p>
                </div>
  
                <div class="third-place">
                    <?php 
                    echo '<div class="third_place_image" style="background-image: url(\'data:image/jpeg;base64,' . base64_encode($best_of_3[3]["avatar"]) . '\');">';
                    ?>
                  </div>
                <p style="margin-right: 5em;">
                  <?php
                  echo $best_of_3[3]["username"] ;
                  ?>
                </p> 
                </div>
              </div>
            </div>
 
          </div>
          <div class="table">
           <table>
            <thead>
              <tr>
              <th>Nr</th>
              <th>User</th>
              <th>Score</th>
              <th>Rank</th>
              </tr>
            </thead>
            <tbody>
              <?php 
              foreach ($page_info as $key => $info) {
                  $content="";
                  $content .= "<td>" . $key . "</td>";
                  $content .= '<td><img src="data:image/jpeg;base64,' . base64_encode($info["avatar"]) . '"/>' . $info["username"] . '</td>';
                  $content .= "<td>" . $info['score'] . "</td>";
                  $content .= "<td>" . $info['rank'] . "</td>";
                  echo "<tr>".$content."</tr>";   
              }
            ?>
            </tbody>
           </table>
          </div>
          <div class="pagination">
            <div>&lt;</div>
            <div><a href="Ranking?id=1">1</a></div>
            <div><a href="Ranking?id=2">2</a></div>
            <div><a href="Ranking?id=3">3</a></div>
            <div><a href="Ranking?id=4">4</a></div>
            <div><a href="Ranking?id=5">5</a></div>
            <div><a href="Ranking?id=6">6</a></div>
            <div>&gt;</div>
          </div>
          </section>
         
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>