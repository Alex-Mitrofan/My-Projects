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
           Quiz
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
              <a href="Login">Logout</a>
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
            $intrebare='<form method="POST" action="Result">';
            for ($i=1;$i<=count($questions);$i++)
            {
              $intrebare.='<h1>'.'Question '.$i.'</h1>';
              $intrebare.='<p class="question">'.$questions[$i]["question"].'</p>';
              $permutation=permutation_question($questions[$i]);
              $k=1;
              foreach ($permutation as $key=>$values)
              {

                if ($key=='good_answer'|| $key=='bad_answer1'|| $key=='bad_answer2'||$key=='bad_answer3')
                  {
                  $intrebare.='<label for="q'.$i.'_'.$k.'">';
                  $intrebare.='<input type="radio" id="q'.$i.'_'.$k.'"name="q'.$i.'"value="'.$key.'">';
                  $intrebare.=$values;
                  $intrebare.='</label>';
                  }
                  $k++;
              }
              
            }
            $intrebare .= '<button type="submit" style="background-color: #4CAF50; color: white; padding: 16px 24px; border: none; border-radius: 4px; cursor: pointer; display: inline-block; width: 100px;">Submit</button>';
            $intrebare.='</form>';
            
            echo $intrebare;
            ?>
          </section>
          </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>