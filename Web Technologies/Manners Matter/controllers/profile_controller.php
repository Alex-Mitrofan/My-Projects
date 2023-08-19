<?php

if(isset($_COOKIE["username"]) == False){

    header('Location: Home', true, 303);
}
require '../models/profile_model.php';

$arr = get_user($_COOKIE["username"]);

$username = $arr[0];
$rank = $arr[1];
$score = $arr[2];
$name = $arr[3];
$location = $arr[4];
$age = $arr[5];
$sex = $arr[6];
$ocupation = $arr[7];
$avatar = $arr[8];
 
 
require '../views/profile.php';

?>