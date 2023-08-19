<?php
session_start();

 
if(isset($_COOKIE["username"]))
    header('Location: Home', true, 303);

require '../models/register_model.php';

setcookie("wrong_username", 'False', time() + 86400); 
$_COOKIE["wrong_username"] = 'False';
setcookie("wrong_password", 'False', time() + 86400); 
$_COOKIE["wrong_password"] = 'False';

require '../views/register.php';

#check if username is unique
if (isset($_POST["username"])){
    $escapedUsername = mysqli_real_escape_string($con, $_POST["username"]);
   
    $result = username_already_used($escapedUsername);
    if ($result == 1){
        setcookie("wrong_username", 'True', time() + 86400);
        $_COOKIE["wrong_username"] = 'True';
    }
}

#check if password was repeated correctly
if (isset($_POST["password"]) && isset($_POST["repeat_password"]))
    if ($_POST["password"] != $_POST["repeat_password"] && $_POST["password"] != ''){

        setcookie("wrong_password", 'True', time() + 86400); 
        $_COOKIE["wrong_password"] = 'True';
    }

if (!isset($_POST["password"]) || !isset($_POST["repeat_password"]))
    $_COOKIE["wrong_username"] = 'True';




if($_COOKIE["wrong_username"] == 'False' &&  $_COOKIE["wrong_password"] == 'False'){
    if (isset($_POST["username"]) && isset($_POST["password"]) && isset($_POST["last_name"])) {
        $escapedUsername = mysqli_real_escape_string($con, $_POST["username"]);
        $escapedPassword = mysqli_real_escape_string($con, $_POST["password"]);
        $escapedName = mysqli_real_escape_string($con, $_POST["last_name"]);

        register($escapedUsername, $escapedPassword, $escapedName);

        #setcookie("username", $_POST["username"]);
        #$_SESSION["user"] = $_POST["username"];
        #header('Location: Home', true, 303);
        unset($_POST['username']);
        unset($_POST['password']);
        unset($_POST['repeat_password']);
        unset($_POST['last_name']);

        header('Location: Register');
    }
}

unset($_POST['username']);
unset($_POST['password']);
unset($_POST['repeat_password']);
unset($_POST['last_name']);





 


?>