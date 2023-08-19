<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="./../Manners Matter/views/images/favicon.png">
    <link rel="stylesheet" href="./views/styles_admin/style.css">
    <link rel="stylesheet" href="./views/styles_admin/feedback.css">
  </head>
  <body>
    <header>
      <div class="logo">
        <a href="Admin_Advice">Manners Matter</a>
      </div>
      <div class="title">
        Vew The Feedback
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
          <h3>Here you can see the feedback: </h3>
          <div class="feedback">
            <p>Date: 10-04-2023</p>
            <p>email: email@email.com</p>
            <p>This is an example of feedback</p>
          </div>
          <div class="feedback">
            <p>Date: 10-03-2023</p>
            <p>email: email2@email.com</p>
            <p>This is another example</p>
          </div>
          <?php
          $feedback_section='<div class="feedback">';
          for ($i=0;$i<count($feedbacks);$i++)
          {
            $feedback_section='<div class="feedback">';
            $feedback_section.='<p>Date: '.$feedbacks[$i]["date"].'</p>';
            $feedback_section.='<p>email: '.$feedbacks[$i]["email"].'</p>';
            $feedback_section.='<p>'.$feedbacks[$i]["message"].'</p>';
            $feedback_section.="</div>";
            echo $feedback_section;
          }
          ?>
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>