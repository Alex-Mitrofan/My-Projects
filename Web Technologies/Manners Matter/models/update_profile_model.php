<?php

require 'database_connection.php';

function update_user($username, $name, $location, $age, $sex, $ocupation ){
    global $con;
    $sql = "UPDATE users SET name = '$name', location = '$location', age = '$age', sex = '$sex', ocupation = '$ocupation'  WHERE username = '$username'";
    $result = mysqli_query($con, $sql);         
            
    }

?>
