<?php
require("get_profile.php");
$arr = explode("/", $_SERVER['REQUEST_URI'] );
 

for($i = 0; $i < count($arr) - 1; $i++)
    if($arr[$i] == "get_profile"){
        $username = $arr[$i+1];
        get_profile($username);
    }

 
?>