<?php
require "../models/challenge_models.php" ;
session_start();

## Calcul of score

$score=0;
$nr_corect_answerd=0;
$name_user=$_SESSION["user"];
$dificulty = $_SESSION['mode'];
if (isset($_POST["q1"])==true && $_POST["q1"]=='good_answer' )
{
    $score+=5;
    $nr_corect_answerd++;
}
if (isset($_POST["q2"])==true && $_POST["q2"]=='good_answer' )
{
    $score+=5;
    $nr_corect_answerd++;

}
if (isset($_POST["q3"])==true && $_POST["q3"]=='good_answer' )
{
    $score+=5;
    $nr_corect_answerd++;
}
if (isset($_POST["q4"])==true && $_POST["q4"]=='good_answer' )
{
    $score+=5;
    $nr_corect_answerd++;
}
if (isset($_POST["q5"])==true && $_POST["q5"]=='good_answer' )
{
    $score+=5;
    $nr_corect_answerd++;
}
if ($nr_corect_answerd<2)
{
    $score=-2;
}
$info=get_score_and_set($score,$name_user,$dificulty);
require "../views/Result.php"
?>