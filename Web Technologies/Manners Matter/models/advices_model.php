<?php
 
function get_advices($age, $ocupation, $context, $job){
    define ('URL2', 'http://localhost/Tehnologii-Web/GetAdvicesService/get_advices/' . $age . "/" . $ocupation . "/" . $context . "/" . $job);
    
    $c = curl_init();
    curl_setopt ($c, CURLOPT_URL, URL2);
    curl_setopt ($c, CURLOPT_RETURNTRANSFER, true);
    curl_setopt ($c, CURLOPT_SSL_VERIFYPEER, false);
    $res = curl_exec  ($c);
    curl_close($c);
    #echo $res;
    $decode =  json_decode($res);
    $res = [];

    if($decode != null)
        foreach($decode as $element){
            array_push($res, $element);
        }

    return $res;
}

?>