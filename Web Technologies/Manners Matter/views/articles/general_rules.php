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
        
        <div class="div_articles" style="flex-direction: column;">
         <section>
          <h1>General rules of ethics on the Internet that we all need to know</h1>
            <p>Article taken from <cite><a href="https://libguides.hull.ac.uk/digitalstudent/tenrules">libguides.hull.ac.uk </a></cite></p>
            <time datetime="2023-04-07 20:30">2023-04-08 1:35</time>
            <p>You need to consider carefully the way you behave and act online as it defines what kind of a 'digital citizen' you are. This is not a series of simple dichotomous decisions that you have to make. The way you choose to behave online requires you to think carefully about many decisions you may usually take for granted. One useful way to look at this is to cons
               ider the idea of "netiquette" (Shea, 2011) or net etiquette. The principles of netiquette serve as a way for users to consider their behavior. Shea (2011) defined 10 principles of netiquette to guide people new to the internet and to provide critical thinking points for experienced users. Each website or community you use will have its own culture and etiquette.
               Shea's principles are designed to help you navigate both new and existing online services you use:</p>
           </section>
           <section >
            <h2>Rule 1: Remember the Human</h2>  
            <img src="../views/images/image_rule1.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
            <div style="padding-top:0.2em">   
            <p>When you are online, it is sometimes easy to forget the human. That is, the people you are interacting with online are real humans and not disembodied usernames or profile pictures. 
                While it brings so many benefits, the internet can often dehumanise other people, especially when you are interacting with someone you do not know personally. For this, remember, it is important to remember the human. You should never say something to someone online that you would not say to him or her in person. It is also useful to remember that online interactions are nearly always recorded and backed up. 
                If you act inappropriately, these recordings will serve as evidence against you.</p>
             </div>
           </section> 
            <section>
                <h2>Rule 2: Be ethical</h2>
                <img src="../views/images/image_rule2.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>In life, people generally follow the law. It can however be easy to let your ethics slip when online. Illegal streaming of movies, illegal downloading of music and copyright infringement is still breaking the law. It is the online equivalent of shoplifting. These activities are a huge loss of revenue for artists and companies. Artists, companies, internet providers and law enforcement agencies are continuing to prosecute people who illegally access and/or their material. Breaking the law is bad netiquette.

                    Just like any other decisions we make, what we do online has ethical implications. These ethical choices are not necessarily associated with law, but the decisions you make online demonstrate your ethical stances. For example, if you use a program like AdBlocker, you are cutting off the revenue streams of the websites you visit. This includes small and independent websites just as much as it affects larger corporations. 
                    Think carefully about what kind of digital citizen you want to be!</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 3: Know where you are</h2>
                <img src="../views/images/image_rule3.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>Netiquette varies from website to website. What is acceptable in one environment is not acceptable in another. For example, the way you behave on university websites and discussion forums will be very different to how you behave on a social network like Facebook. One good piece of advice comes from Shea (2011) "lurk before you leap". When you approach a new website, watch and monitor how people communicate and interact. Once you have observed their behaviour and have an idea of what is acceptable feel free to join in!</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 4: Respect other people's time and data limits</h2>
                <img src="../views/images/image_rule4.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>When you post anything online, write an email or share a post it will take other people's time to read. Shea (2011) argues "it's your responsibility to ensure that the time they spend reading your posting isn't wasted". It is important that you direct messages to the right people. With modern technology, it is too easy to send a message to everybody in your contact list. Instead, you need to spend time focusing your message and sending it to the relevant people. Social networks can help you achieve that by focusing your contributions towards appropriate networks. Facebook is great for personal stuff whereas ResearchGate is better for academic discussions.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 5: Make yourself look good online</h2>
                <img src="../views/images/image_rule5.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>Make sure you are careful with what you share. It is always advisable not to share anything embarrassing, illegal or inappropriate. People you have not even met may look you up online. Make sure you set a good impression. Always ensure that what you write and share is understandable and grammatically correct. It makes it hard for others to read your work if it is not communicated properly. It generally helps to avoid swearing, but if you feel the need it may be an idea to use euphemisms or asterisks to filter it out; e.g. f***.

                    Online interactions can be a great leveller. Unless you share such personal information, attributes like your gender, weight, general appearance, name, religion and race will be unknown to those you interact with. You can take advantage of this anonymity.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 6: Share expert knowledge</h2>
                <img src="../views/images/image_rule6.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>Sharing is one of the principles behind the majority of internet services. If you are knowledgeable in an area then you have something to offer! Share what you know and it will help other users. You can share your experiences as part of this - both positive and negative. If you have made any mistakes, sharing these can help prevent others from doing the same. If you ever ask questions to other users, it is good practice to post a summary of the responses. This enabled everyone to benefit from answers and does not require each individual to do the same synthesis.

                    You should never post anything disingenuous online. In the online environment, it is very easy for untruths, errors and mistakes to become accepted as fact and propagated. You have responsibility to ensuring the accuracy of your contributions. If you are sharing opinion or ideas, make sure it is clear to your audience.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 7: Keep disagreement healthy</h2>
                <img src="../views/images/image_rule7.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>People are always going to disagree and that is healthy. Such disagreements can be about heated issues like politics, religion and philosophy or they can be relatively trivial. When involved in any such a debate, it is important to be respectful of the other people involved. Never reduce the discussion to personal issues and avoid inappropriate language. If you are going to provide negative comments, ensure they are constructive and useful.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 8: Respect other people's privacy</h2>
                <img src="../views/images/image_rule8.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>When you are networked to someone on a website like Facebook or LinkedIn, you may be given privileged access to information about him or her and what he or she shares. You need to ensure you do not breach anyone's wishes by sharing any of the content they have made available to you. It is also worth mentioning that you should not use anyone else's computers, mobile devices or accounts without their permission.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 9: Don't abuse your power</h2>
                <img src="../views/images/image_rule9.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>If you are an administrator or facilitator for any online environment, make sure you do not abuse the privilege of access that your position may give you.</p>
                </div>
                
            </section>
            <section>
                <h2>Rule 10: Be forgiving of other people's mistakes</h2>
                <img src="../views/images/image_rule10.png" alt="image1" style="width: 10em; height: 10em;float:left;margin:0;">
                <div style="padding-top:0.2em">   
                <p>People will make mistakes when they are new to online environments. Everyone has to start somewhere, so try and be forgiving of other's mistakes.</p>
                </div>
                
            </section>
            <p>Tags: <i>ethical</i>, <i>life</i>, <i>job</i>, <i>online-enviroment</i>, <i>ruels</i></p>
           
          
        </div>


    </main>
    <footer>
        Copyright © 2023 
    </footer>
	 
  </body>
</html>