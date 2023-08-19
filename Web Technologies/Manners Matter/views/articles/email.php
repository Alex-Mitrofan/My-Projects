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
 
            <h1>FOR EMAIL ETIQUETTE</h1>
            <p>Article taken from <cite><a href="https://www.lawsociety.com.au/resources/resources/career-hub/10-rules-email-etiquette">www.lawsociety.com.au </a></cite></p>
            <time datetime="2023-04-01 14:00">2023-04-01 14:00</time>
            <img class="article_image" src="../views/images/email-logo.jpg" alt="email">
            <h2>10 rules for email etiquette</h2>
            <p>In a 2015 study, Adobe Systems found that the average worker spends 6.3 hours each day sifting through and responding to emails. That’s more than 30 hours per week which adds up to 63 full days each year.
              You’d think all this practise would make us all experts in the art of email communication, yet many professionals are still getting it wrong. The accidental “reply all” on a private email surely happens 
              more often than HR departments would like to deal with. And how many times have you received an 
              email that is irrelevant, inappropriate or aggressive? </p>
            <p>To avoid battles and better manage your professional relationships, she advises following the following tips.</p>
            <h3>1. Use a clear, professional subject line</h3>
            <p>Show your recipient clearly what the email will cover. Many people will decide whether they will open an email depending on the 
              subject line. For someone who gets hundreds of emails a day, a subject line that is to the point makes it easier for them to sort 
              through their inbox and decide what 
              communications to prioritise.</p>
            <hr>
            <h3>2. Proofread every email you send</h3>
            <p>Make sure there are no grammatical or professional errors. Have you spelt the recipient’s name correctly? 
              Are there spelling errors? Are you using simple sentence structures and correct capitalisation and punctuation? 
              Ignoring these compromises your professionalism and the credibility of your email.</p>
            <hr>
            <h3>3. Write your email before entering the recipient email address</h3>
            <p>It is always best practice to write the contents of your email first in case you accidentally send the message too early.</p>
            <hr>
            <h3>4. Double check you have the correct recipient</h3>
            <p>There is nothing worse than sending an email to the wrong Jess or a confidential document to the wrong client or company.</p>
            <hr>
            <h3>5. Ensure you CC all relevant recipients</h3>
            <p>It is unprofessional to leave out a colleague or client from a relevant email chain. Be mindful of who should be informed about a given matter and respect 
              that.</p>
            <hr>
             <h3>6. You don't always have to "reply all"</h3>
             <p>Think about who needs to read your response; no one wants to read an email chain from 20 people that has nothing to do with them.</p>
             <hr>
             <h3>7. Reply to your emails</h3>
             <p>Most people at some point have felt swamped by the large number of emails they have to sift through. But replying to an email is good etiquette, especially if the sender is expecting a response. Acknowledging you received the email but will get back to the 
              sender at a later time is a professional alternative to ignoring or avoiding certain emails.</p>
             <hr>
              <h3>8. Include a signature block</h3>
              <p>If your recipient doesn’t know anything about you, they may be skeptical of the authenticity of your email. It is professional to include your full name, title, your company and your contact 
                number.</p>
              <hr>
              <h3>9. Use the appropriate level of formality</h3>
              <p>For instance, begin with “Dear _____”, use “please” and “thank you” where necessary, and always end your email with the appropriate phrase, “Kind regards”, “Thank you”, “Sincerely” 
                and so on.</p>
              <hr>
              <h3>10. Keep emails brief and to the point</h3>
              <p>No one wants to read an enormous chunk of text. You can always follow up on the matter later or suggest they give you a call if they have any queries or concerns.</p>
            <p class="tags">Tags: <i>writing</i>,<i>Email</i>,<i>Job</i></p>
          </section>
          
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>