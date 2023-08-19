<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Manners Matter</title>
    <link rel="icon" type="image/x-icon" href="../views/images/favicon.png">
    <link rel="stylesheet" href="../views/styles/style.css">
    <link rel="stylesheet" href="../views/styles/articles.css">
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
      </div>
      <div class="profile">
        <div class="username">
          <a href="../Login">Login</a>
        </div>
        <div class="dropdown_profile">
          <div class="avatar">
          </div>

          <div class="dropdown_content">
            <a href="../Profile">My Profile</a>
            <a href="../Logout">Logout</a>
          </div>
        </div>
      </div>

  </header>
    <main>
      <nav>
        <ul>
          <li>
            <a href="../Home">Home</a>
          </li>
          <li>
            <a href="../Profile">Profile</a>
          </li>
          <li>
            <a href="../Advices">Advices</a>
          </li>
          <li>
            <a href="../Challenge">Challenge</a>
          </li>
          <li>
            <a href="../Ranking">Ranking</a> 
          </li>
          <li>
            <a href="../About">About</a>
          </li>
          <li>
            <a href="../Contact">Contact</a>
          </li>
        </ul>
      </nav>
        
        <div class="div_articles">
          <section>
            <h1>Zoom Interview Attire: What (and What Not) to Wear</h1>
            <p>Article taken from <cite><a href="https://www.theforage.com/"> theforage.com </a></cite></p>
            <time datetime="2023-04-08 23:00">2023-04-08 23:00</time>

            <img class="article_image" src="../views/images/interview.png" alt="interview.png">

            <p>You've accepted your Zoom interview invite, but then the fear creeps in — what Zoom interview attire do you wear? In this guide, we'll help you figure out what to wear for a virtual interview so you can look (and feel!) your best on camera. We'll cover:
            </p>
            <h2>How Professional Should You Dress for a Zoom Interview?</h2>
            <p>One of the best ways to decide what to wear for a job interview is to research the company dress code. Look on the company's website to see if there are pictures of people in the office or any news or statements about its dress code online.
            </p>
            <p>A company's culture is your best insight into how professional you should dress. For example, if it's more relaxed and casual in its communication — using “hey” and “hi” instead of “greetings” and “dear” — chances are the company follows a more relaxed dress code.
            </p>
            <p>There are four main types of dress codes that companies follow:</p>
            <ul>
                <li>Business formal</li>
                <li>Business professional</li>
                <li>Business casual</li>
                <li>Casual</li>
            </ul>

            <h3>Business Formal</h3>
            <p>If the term “professional” conjures up images of Mad Men, you're likely thinking of business formal dress codes. Business formal is the most conservative, traditional, and strict dress code. People wear suits and pantsuits, often accessorized with more luxury items like cufflinks and high heels. For a Zoom interview, it's unlikely that you'll need to dress this formally.
            </p>

            <h3>Business Professional</h3>
            <p>A slight step down from a business formal dress code, business professional captures the everyday dress code of many traditional fields like finance and accounting. Suits and pantsuits might be more common, but often without suit jackets, ties, or luxury accessories. If you're interviewing for a more traditional company, this might be the dress code to follow.
            </p>

            <h3>Business Casual</h3>
            <p>No need for a suit in a business casual dress code, but don't run to grab your new jeans, either. Dress pants with blouses, polo shirts, and collared shirts fit into this category. As the name suggests, business casual is a middle ground between more informal clothing and traditional business attire.
            </p>

            <h3>Casual</h3>
            <p>Employees who follow casual dress codes often dress down and wear clothes infused with their style. This dress code includes jeans, simple shirts, casual dresses, and sneakers. Although this dress code is much more relaxed and comfortable, clothes you'd casually wear running errands or working out still aren't acceptable.
            </p>
            <p>When it comes to professional settings, it's usually better to be overdressed than underdressed. So even if you think the company has a casual dress code, try to play it safe and err on the side of business casual.
            </p>

            <h2>Should You Dress the Same for a Zoom Interview as In Person?</h2>
            <p>Yes! You should choose the same attire as you would for any other interview. Even the shoes you wear for a Zoom interview are important. Although the interviewer likely won't see most of your outfit, what you wear during the interview can impact how you present yourself and how confident you feel.
            </p>
            <p>When deciding what to wear, choose an outfit you'd wear if the interviewer were going to show up at your door and meet you in person. You never know when you might get up during the Zoom interview to grab a document or reach for your glass of water. You don't want the hiring manager to see pajama bottoms.
            </p>

            <h2>What Not to Wear in a Zoom Interview</h2>
            <p>Anything widely accepted as “unprofessional,” including profane graphics and words and overly revealing tops, is typically off-limits regarding Zoom attire. Yet once you know what dress code to go with, there aren't necessarily specific items that are off-limits.
            </p>
            <p>Some experts recommend sticking to neutral colors in an interview, often for fear that bright colors or patterns will distract from your face in the video. However, if your outfit doesn't affect your camera view, there's no need to dull your outfit or accessories. Don't be afraid to show off your favorite color or wear an accessory you love — as long as you've checked how it looks on Zoom first.
            </p>
            Tags: <i>interview</i>, <i>conference</i>, <i>video conference</i>, <i>job</i>, <i>clothing</i>



             
          </section>
          
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>