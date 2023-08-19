<?php
session_start();

if(isset($_COOKIE["username"]))
header('Location: Home', true, 303);
 
if(isset($_POST["username"]) && isset($_POST["password"])){

    require '../models/login_model.php';
    $escapedUsername = mysqli_real_escape_string($con, $_POST["username"]);
    $escapedPassword = mysqli_real_escape_string($con, $_POST["password"]);

    $result = search_username_password($escapedUsername, $escapedPassword);

    if($result == 1){
        setcookie("username", $_POST["username"]);
        $_SESSION["user"] = $_POST["username"];
        header('Location: Home', true, 303);
    }
}

require '../views/login.html';
 

?>