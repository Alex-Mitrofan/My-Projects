<?php

#require '../models/students_model.php';
require '../models/profile_model.php';

if(isset($_COOKIE["username"]) == True){
    $arr = get_user($_COOKIE["username"]);
    $avatar = $arr[8];
  }
require '../views/index.php';

?>