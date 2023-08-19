<?php

require 'database_connection.php';

function get_profile($username){
    global $con;
    
    $sql = "SELECT * FROM users where username='".$username."';";
    $result = mysqli_query($con, $sql);

    $arr = [];
        while ($inreg = $result->fetch_assoc()) {
            $arr[] = $inreg['username'];
            $arr[] = $inreg['rank'];
            $arr[] = $inreg['score'];
            $arr[] = $inreg['name'];
            $arr[] = $inreg['location'];
            $arr[] = $inreg['age'];
            $arr[] = $inreg['sex'];
            $arr[] = $inreg['ocupation'];
            $arr[] = base64_encode($inreg['avatar']);
        }

    $user = [];   
    $user = array('username'=>$arr[0],
                'rank'     => htmlspecialchars(intval($arr[1])),
                'score'    => htmlspecialchars(intval($arr[2])),
                'name'     => htmlspecialchars(($arr[3])),
                'location' => htmlspecialchars(($arr[4])),
                'age'      => htmlspecialchars(intval($arr[5])),
                'sex'      => htmlspecialchars(($arr[6])),
                'ocupation'=> htmlspecialchars(($arr[7])),
                'avatar'   => htmlspecialchars(($arr[8])));
  



    $json = json_encode($user);
    echo $json;
     
    #echo '<img src="data:image/png;base64,' . $arr[8] . '" alt="Image">';
    #return $json;
            
    }

 


?>