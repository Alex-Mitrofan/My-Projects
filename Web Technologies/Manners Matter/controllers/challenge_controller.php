<?php
require '../models/challenge_models.php';

if(isset($_COOKIE["username"]) == False){

    header('Location: Home', true, 303);
}

require '../models/profile_model.php';

$arr = get_user($_COOKIE["username"]);
$avatar = $arr[8];
require '../views/challenge.php';
?>