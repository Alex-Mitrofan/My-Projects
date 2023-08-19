<?php

$arr = explode("/", $_SERVER['REQUEST_URI'] );

if (in_array("Admin_Advice",$arr))
  require  '../controllers/add_advices_controller.php';
elseif (in_array("Admin_Articles",$arr))
    require  '../controllers/add_articles_controller.php';
elseif (in_array("Admin_Question",$arr))
  require  '../controllers/add_question_controller.php';
elseif (in_array("Admin_Login",$arr))
  require  '../controllers/login_controller.php';
elseif (in_array("Admin_Feedback",$arr))
  require '../controllers/view_the_feedback_controller.php';
else
  echo "Wrong Adrees"

?>