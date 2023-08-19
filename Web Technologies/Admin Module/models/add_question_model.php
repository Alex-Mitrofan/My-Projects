<?php
$conn=new mysqli(
    'localhost', // locatia serverului (aici, masina locala)
    'root',       // numele de cont
    '',    // parola (atentie, in clar!)
    'manners_matter',   // baza de date
);
if (mysqli_connect_errno()) {
    die ('Eror connection database challenge_model...');
}

function is_exist($question)
{
  global $conn;
  $result=False;
  if (!($qez=mysqli_query($conn,'select question from questions')))
  {
      die('Eror query add_question_model');
  }
  while ($rez=$qez->fetch_assoc())
  {
     if ($rez["question"]==$question)
     { 
       $result=True;
       break;
     }
  }
  return $result;
}
function set_question($question,$good,$bad1,$bad2,$bad3)
{
   global $conn;
   $result=is_exist($question);
   $options=array('easy','hard','medium');
   if ($result==True)
   {
     $result='Question already exist!';
   }
   else
   {
    shuffle($options);
    $mode=$options[0];
    $query="INSERT INTO questions (question, good_answer, bad_answer1, bad_answer2, bad_answer3,dificulty) VALUES ('$question', '$good', '$bad1', '$bad2', '$bad3', '$mode')";
    if (!($qez=mysqli_query($conn,$query)))
    {
        die('Eror query add_question_model');
    }
   }
}
?>