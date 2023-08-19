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
function get_feedbacks()
{
    global $conn;
    $result=[];
    if (!($qer=mysqli_query($conn,"select * from feedback")))
    {
        die("Eror to query admin feedback module");
    }
    while($rez=$qer->fetch_assoc())
    {
     $result[]=$rez;
    }
    return $result;
}

?>