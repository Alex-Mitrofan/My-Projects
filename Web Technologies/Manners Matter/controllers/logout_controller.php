<?php
 
session_start();
unset($_SESSION["user"]);

if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie("username", "", time() - 42000);
}

session_destroy();
header("Location: Home", true, 303);

?>