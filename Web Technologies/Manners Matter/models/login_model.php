<?php

require 'database_connection.php';

function search_username_password($username, $password){
    global $con;
    
        $sql = "SELECT * FROM users where username='".$username."' and password='".$password."';";
        $result = mysqli_query($con, $sql);

        if (mysqli_num_rows($result) > 0) 
            return 1;

    return 0;            
            
    }


?>