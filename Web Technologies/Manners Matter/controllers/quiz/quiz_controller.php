<?php
session_start();
require '../models/challenge_models.php';

if (isset($_POST["Difficulty"]))
{
    $questions=get_question_and_answers(strtolower($_POST["Difficulty"]));
    $_SESSION['mode']=$_POST["Difficulty"];
    $_POST["Difficulty"] = null;
   
} 

require '../models/profile_model.php';
if(isset($_COOKIE["username"]) == True){
    $arr = get_user($_COOKIE["username"]);
    $avatar = $arr[8];
  }
require '../views/quiz/quiz.php';
?>