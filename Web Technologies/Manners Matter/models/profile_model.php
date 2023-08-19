<?php

function get_user($username){
    define ('URL', 'http://localhost/Tehnologii-Web/GetProfileService/get_profile/' . $username);

    $c = curl_init();
    curl_setopt ($c, CURLOPT_URL, URL);
    curl_setopt ($c, CURLOPT_RETURNTRANSFER, true);
    curl_setopt ($c, CURLOPT_SSL_VERIFYPEER, false);
    $res = curl_exec  ($c);
    curl_close($c);
    #echo $res;
    $decode =  json_decode($res);
    $res = [];
    if($decode!=null)
    {
     foreach($decode as $element){
        array_push($res, $element);
    }
    }
    return $res;
    
}   

?>