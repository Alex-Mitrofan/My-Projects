<?php
require '../models/add_question_model.php';
if (isset($_POST['new_question']))
{
  $exist=is_exist($_POST['new_question']);
  set_question($_POST['new_question'],
               $_POST['correct'],
               $_POST['w1'],
               $_POST['w2'],
               $_POST['w3']);
}
require '../views/add_question.php'
?>