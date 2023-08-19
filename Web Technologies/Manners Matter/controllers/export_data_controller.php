<?php
require "../models/profile_model.php";
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
 
$array = array(
    'key1' => 'value1',
    'key2' => 'value2',
    'key3' => 'value3'
);
$fileContent = array("username" => $username, 
                "rank: " => $rank,
                "score: " => $score ,
                "name: " => $name,
                "location: " => $location ,
                "age: " => $age,
                "sex: " => $sex ,
                "ocupation: " => $ocupation ,
                "avatar: " => $avatar
);
$json = json_encode($fileContent);

$fileName = "data.txt";

 
header("Content-type: text/plain");
header("Content-Disposition: attachment; filename=".$fileName);

 
echo $json;
exit;
?>