<?php

 
$arr = explode("/", $_SERVER['REQUEST_URI'] );


if (in_array("About", $arr))
    require '../controllers/about_controller.php';
elseif (in_array("Advices", $arr))
    require '../controllers/advices_controller.php';
elseif (in_array("Challenge", $arr))
    require '../controllers/challenge_controller.php';
elseif (in_array("Contact", $arr))
    require '../controllers/contact_controller.php';
elseif (in_array("Home", $arr))
    require '../controllers/index_controller.php';
elseif (in_array("Login", $arr))
    require '../controllers/login_controller.php';
elseif (in_array("Profile", $arr))
    require '../controllers/profile_controller.php';
elseif (in_array("Ranking", $arr))
    {
     $_GET["id"]=1;
     require '../controllers/ranking_controller.php';
    }
elseif (in_array("Register", $arr))
    require '../controllers/register_controller.php';
elseif (in_array("Logout", $arr))
    require '../controllers/logout_controller.php';
elseif (in_array("Export", $arr))
    require '../controllers/export_data_controller.php';
elseif (in_array("EditProfile", $arr))
    require '../controllers/edit_profile_controller.php';
elseif (in_array("UpdateProfile", $arr))
    require '../controllers/edit_profile_controller.php';

#ARTICLES
elseif (in_array("Email", $arr))
    require '../controllers/articles/email_controller.php';
elseif (in_array("Emoji", $arr))
    require '../controllers/articles/emoji_controller.php';
elseif (in_array("General%20Rules", $arr))
    require '../controllers/articles/general_rules_controller.php';
elseif (in_array("Interview", $arr))
    require '../controllers/articles/interview_controller.php';
elseif (in_array("Video%20Conference", $arr))
    require '../controllers/articles/video_conference_controller.php';

#QUIZ

elseif (in_array("Quiz", $arr))
    require '../controllers/quiz/quiz_controller.php';
elseif (in_array("Result",$arr))
    require '../controllers/result_controller.php';
## PAGINATION RANK
elseif (is_numeric(strstr($arr[count($arr)-1],"id")[-1])==True && str_contains($arr[count($arr)-1],"Ranking")==True)
    {
      require '../controllers/ranking_controller.php';
      if(isset($_GET["id"])) 
         $_GET["id"]=(int)strstr($arr[count($arr)-1],"id")[-1];
    }
else 
 echo "Wrong Adress";





?>