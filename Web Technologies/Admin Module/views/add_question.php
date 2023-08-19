<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./../Manners Matter/views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles_admin/style.css">
    <link rel="stylesheet" href="./views/styles_admin/add_question.css">
  </head>
  <body>
    <header>
      <div class="logo">
        <a href="Admin_Advice">Manners Matter</a>
      </div>
      <div class="title">
        Add Questions
      </div>
      <div class="profile">
        <div class="username">
          <a href="Admin_Login">Login</a>
        </div>
        <div class="dropdown_profile">
          <div class="avatar">
          </div>

          <div class="dropdown_content">
            <a href="Admin_Login">Logout</a>
          </div>
        </div>
      </div>
  </header>
    <main>
      <nav>
        <ul>
          <li>
            <a href="Admin_Advice">Add Advices</a>
          </li>
          <li>
            <a href="Admin_Question">Add Questions</a>
          </li>
          <li>
            <a href="Admin_Feedback">View the feedback</a>
          </li>
          <li>
            <a href="Admin_Articles">Add Articles</a>
          </li>
        </ul>
      </nav>
        
        <div class="div_articles">
          
          <div class="question">
            <div class="style">
            <form action="Admin_Question" method="POST">
            <label for="new_question">Question</label><br>
            <input type="text" id="new_question" name="new_question" required><br>
  
            <label for="correct">Correct Answer</label><br>
            <input type="text" id="correct" name="correct" required><br>

            <label for="w1">Wrong Answer</label><br>
            <input type="text" id="w1" name="w1" required><br>

             <label for="w2">Wrong Answer</label><br>
             <input type="text" id="w2" name="w2" required><br>
              
             <label for="w3">Wrong Answer</label><br>
             <input type="text" id="w3" name="w3" required><br>
              
             <input class="submit_button" type="submit" value="Add">
            </form>
            </div>
          </div>
          <?php
          if (isset($exist)==True)
          { 
            if ($exist==False)
            {
              $value='<br><p style="text-align: center; color: green; padding-left:50em">
              Question has been set </p>';
              echo $value;
            } 
            else
            {
              $value='<br><p style="text-align: center; color: green; padding-left:43em">
              Question has not been set.Already exist!!</p>';
              echo $value;
            }
          } 
            ?>
       
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>