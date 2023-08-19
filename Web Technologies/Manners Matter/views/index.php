<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="views/images/favicon.png">
    <link rel="stylesheet" href="views/styles/style.css">
    <link rel="stylesheet" href="views/styles/home.css">
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
           Home
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
          <div class="section">
           
            <article>
              <div class="text">
                <a href="Articles/Emoji"><h2>Proper Emoji Etiquette: When to Use (or Not Use) Them</h2></a>
                <p>Emojis have become a habitual way of sharing thoughts, feelings, and concepts. However, these smiley-face icons aren't appropriate in every form of communication. So, when is it fitting to use them?
                </p>
                <div class="tags">
                  Tags: <i>emoji</i>, <i>social media</i>, <i>coworkers</i>
                </div>
              </div>
              <img class="article_image" src="./views/images/emoji.jpg" alt="emoji image">

            </article>
            
            <article>
              <div class="text">
                <a href="Articles/Video%20Conference"><h2>Video conferencing etiquette: 10 tips for a successful video conference</h2></a>
                <p>Video conferencing has become an essential component of the modern business world and helps improve the connectedness of remote team members.
                  <br>In fact, 80% of executives say video conferencing is taking over audio conferencing.</p>
              
                <div class="tags">
                  Tags: <i>conference</i>, <i>video conference</i>, <i>job</i>, <i>clothing</i>, <i>hardware</i>
                </div>
              </div>
              <img class="article_image" src="./views/images/video_conference.png" alt="emoji image">

            </article>

            <article>
              <div class="text">
                <a href="Articles/General%20Rules"><h2>General rules of ethics on the Internet that we all need to know</h2></a>
                <p>Whether we want it or not, the Internet is part of our lives, including our professional life,   where <br> successful communication with colleagues is essential to be successful</p>
                <div class="tags">
                  <p>Tags: <i>ethical</i>, <i>life</i>, <i>job</i>, <i>online-enviroment</i>, <i>ruels</i></p>
                </div>
              </div>
              <img class="article_image"  src="./views/images/general_ethic_rule.png" alt="rules">
            </article>

            <article>
              <div class="text">
                <a href="Articles/Email"><h2>Email etiquette</h2></a>
                <p>If you want to communicate better and avoid an office e-war take in a count next tips</p>
                <div class="tags">
                  <p>Tags: <i>writing</i>,<i>Email</i>,<i>Job</i></p>
                </div>
              </div>
              <img class="article_image"  src="./views/images/email-logo.jpg" alt="rules">
            </article>
             
            <article>
              <div class="text">
                <a href="Articles/Interview"><h2> Zoom Interview Attire: What (and What Not) to Wear</h2></a>
                <p>You've accepted your Zoom interview invite, but then the fear creeps in — what Zoom interview attire do you wear?
                  <br> In this guide, we'll help you figure out what to wear for a virtual interview so you can look (and feel!) your best on camera.  
                </p>
              
                <div class="tags">
                  Tags: <i>interview</i>, <i>conference</i>, <i>video conference</i>, <i>job</i>, <i>clothing</i>
                </div>
              </div>
              <img class="article_image" src="./views/images/interview.png" alt="interview image">

            </article>

             <div class="pagination">
              <div><a href="Home">&lt;</a></div>
              <div><a href="Home">1</a></div>
              <div><a href="Home">2</a></div>
              <div><a href="Home">3</a></div>
              <div><a href="Home">4</a></div>
              <div><a href="Home">5</a></div>
              <div><a href="Home">6</a></div>
              <div><a href="Home">&gt;</a></div>
             </div>
             
            </div>
           
         
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>