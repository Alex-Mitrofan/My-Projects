<?php
require("get_advices.php");
$arr = explode("/", $_SERVER['REQUEST_URI'] );
 
$lastFourElements = array_slice($arr, -4);

$age = $lastFourElements[0];
$ocupation = $lastFourElements[1];
$context = $lastFourElements[2];
$job = $lastFourElements[3];


get_advices($age, $ocupation, $context, $job);

 
?>