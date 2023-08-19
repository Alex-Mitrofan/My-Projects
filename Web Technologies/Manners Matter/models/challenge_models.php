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
function new_rank ($score)
{
    $result="";
    if ($score<250)
      $result="Baby";
    if ($score>=250 && $score<500)
      $result="Boy";
    if ($score>=500 && $score<1000)
      $result="Man";
    if ($score>=1000)
      $result="Getman";
    return $result;
}
function get_score_and_set($score, $name_user,$dificulty)
{
    global $conn;
    if ($dificulty!='Practice')

    {// Selectează utilizatorul cu numele de utilizator specificat
    $query = "SELECT * FROM users WHERE username = '" . mysqli_real_escape_string($conn, $name_user) . "'";
    $qer = mysqli_query($conn, $query);
    if (!$qer) {
        die("Error in query: " . mysqli_error($conn));
    }
    $rez = $qer->fetch_assoc();

    // Actualizează scorul utilizatorului
    $new_score = (int) $rez['score'] + (int) $score;
    $new_rank=new_rank($new_score);
    $update_query = "UPDATE users SET score = " . $new_score . ", rank = '" .  $new_rank . "' WHERE username = '" . mysqli_real_escape_string($conn, $name_user) . "'";
    $update_result = mysqli_query($conn, $update_query);
    if (!$update_result) {
        die("Error in query: " . mysqli_error($conn));
    }

    // Construiește un array cu informațiile actualizate
    $info = array();
    $info['old_score'] = $rez['score'];
    $info['new_score'] = $new_score;
    $info['old_rank'] = $rez['rank'];
    $info['new_rank']=$new_rank;
    $info['username'] = $rez['username'];
    $info['mode']=$dificulty;
   }
   else
   {
    $query = "SELECT * FROM users WHERE username = '" . mysqli_real_escape_string($conn, $name_user) . "'";
    $qer = mysqli_query($conn, $query);
    if (!$qer) {
        die("Error in query: " . mysqli_error($conn));
    }
    $rez = $qer->fetch_assoc();
    $info = array();
    $info['old_score'] = $rez['score'];
    $info['new_score'] = $rez['score'];
    $info['old_rank'] = $rez['rank'];
    $info['username'] = $rez['username'];
    $info['mode']=$dificulty;
   }

    return $info;
}
function permutation_question($question)
{
    $keys = array_keys($question);
    shuffle($keys);

    $result = [];
    foreach ($keys as $key) {
        $result[$key] = $question[$key];
    }

    return $result;
}
function get_question_and_answers($difficulty)
{
     global $conn;
     $result=[];
     if ($difficulty!='practice')
     {
       if (!($qer=mysqli_query($conn,'select * from questions where lower(dificulty)=\''.$difficulty.'\' order by rand() limit 5')))
       {
           die("Eror query challenge_model.php");
       }
       $k=1;
       while($rez=$qer->fetch_assoc())
       {
        $result[$k++]=$rez;
       }
     }
     else
     {
       if (!($qer=mysqli_query($conn,'select * from questions order by rand() limit 5')))
       {
           die("Eror query challenge_model.php");
       }
       $k=1;
       while($rez=$qer->fetch_assoc())
       {
        $result[$k++]=$rez;
       }
     }


     return $result;
}

?>