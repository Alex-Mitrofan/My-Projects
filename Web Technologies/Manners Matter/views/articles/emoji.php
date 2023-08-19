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
 
            <h1>Proper Emoji Etiquette: When to Use (or Not Use) Them</h1>
            <p>Article taken from <cite><a href="https://www.makeuseof.com/"> makeuseof.com </a></cite></p>
            <time datetime="2023-04-01 14:00">2023-04-01 14:00</time>

            <img class="article_image" src="../views/images/emoji.jpg" alt="emoji image">
            <p>Emojis have become a habitual way of sharing thoughts, feelings, and concepts. However, these smiley-face icons aren't appropriate in every form of communication. So, when is it fitting to use them?
            </p>
            <h2>When to Use (or Not Use) Emojis</h2>
            <p>When it comes to communication and socializing, there's a time and place for everything, even in the digital world. Let's go over the scenarios when it is (and isn't) OK to use emojis, and which ones to use...   
            </p>
            <h3>Personal Text</h3>
            <p>In personal texts, anything goes when it comes to emojis. The type and amount of emojis you use will come down to your personal communication style, and the relationship you have with the recipient. In fact, this is the ideal time to use them, as even one emoji can make a difference in how the other person perceives your text.
            </p>
            <p>For example, "I'm just too much" followed by a laughing or clown emoji will let them know it's just a joke. But the same text followed by a sad-face or heart-broken emoji will invoke a sympathetic response since it reads as a sad phrase.
            </p>
            <h3>Social Media</h3> 
            <p>How you use emojis on social media will vary greatly depending on the platform, recipient, content, and agenda. With light-hearted posts, anything goes. While serious content warrants fewer emojis due to their cartoonish nature.
            </p>
            <p>
                For example, you might want to leave a comment with a bunch of laughing emojis on a funny Instagram video. But if you're commenting about your experience at a restaurant on its Facebook page, anything other than a smiley-face or thumbs-up emoji might be out of place.
            </p>
            <h3>Semi-Formal Communication</h3>
            <p>Semi-formal communication includes things like inquiries, arrangements for an event, complaints, as well as texts with individuals you don't know personally.
            </p>
            <p>Emojis should be used sparingly in these texts since they can make the recipient uncomfortable if they don't know you, or it might give them the impression that you're not taking the subject discussed seriously. But they're not entirely taboo either.
            </p>
            <h3>Communication With Coworkers</h3>
            <p>While your first thought might be to entirely avoid emojis with anyone work-related, that's not always the case—it depends on the nature of the relationship and the subject of discussion.
            </p>
            <p>If you're having a friendly back-and-forth with a coworker, emojis are OK, as long as you don't use too many and match the emojis with the topic. Jokes can be followed by laughing emojis, regards to a sick family member can be sent with heart emojis, and relaying of an embarrassing story can be paired with the monkey covering their eyes.
            </p>
            <h3>Clients and Customers</h3>
            <p>If your communication with a client or customer has always centered around business and nothing else, steer clear from emoji use, especially if you don't know them personally. Otherwise, light emoji use could be OK.
            </p>
            <p>A good rule is to wait for the client or customer to use them first, and you can follow their lead. Even then, consider the nature of the discussion and ensure that including an emoji in your response is appropriate. Simply because you've established friendly communication, doesn't mean emojis won't come off as unprofessional.
            </p>
            <p>And if you do use them, stick to the basic ones. There won't be any part of business-related communication that warrants the tongue-out emoji.
            </p>
            <h3>Communicating With Your Boss</h3>
            <p>When communicating with your boss or any higher-up, emoji use is ill-advised. Similar to clients and customers, follow their lead, with extra consideration to the nature of the discussion.
            </p>
            <p>If you have a good relationship with your boss, and they send an emoji, you've got the green light to include one in your response—only given the discussion leans to light-hearted. Under any other circumstances, it's safer to avoid emojis.
            </p>

            <p class="tags">Tags: <i>emoji</i>, <i>social media</i>, <i>coworkers</i></p>
          </section>
          
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>