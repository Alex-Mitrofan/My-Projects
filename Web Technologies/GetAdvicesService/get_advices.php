<?php

require 'database_connection.php';
 
function get_advices($age, $ocupation, $context, $job){ 
    global $con;
    $advices1 = [];
    $advices2 = [];
    $advices3 = [];
    $advices4 = [];

    $ages = explode(",", $age);
     
    for ($i = 0; $i < count($ages); $i++)
        if ($ages[$i] != 0){
            
            $sql = "SELECT advice FROM advices where age LIKE '%" . $ages[$i] . "%';";
            $result = mysqli_query($con, $sql);
            #echo $sql;
            while ($inreg = $result->fetch_assoc())  
                $advices1[] = $inreg['advice'];
      
        }

    
    $ocupations = explode(",", $ocupation);
    
    for ($i = 0; $i < count($ocupations); $i++)
        if ($ocupations[$i] != 0){
            
            $sql = "SELECT advice FROM advices where ocupation LIKE '%" . $ocupations[$i] . "%';";
            $result = mysqli_query($con, $sql);
            #echo $sql;
            while ($inreg = $result->fetch_assoc())  
                $advices2[] = $inreg['advice'];
        
        }

    $contexts = explode(",", $context);
    
    for ($i = 0; $i < count($contexts); $i++)
        if ($contexts[$i] != 0){
            
            $sql = "SELECT advice FROM advices where context LIKE '%" . $contexts[$i] . "%';";
            $result = mysqli_query($con, $sql);
            #echo $sql;
            while ($inreg = $result->fetch_assoc())  
                $advices3[] = $inreg['advice'];
        
        }

    $jobs = explode(",", $job);
    
    for ($i = 0; $i < count($jobs); $i++)
        if ($jobs[$i] != 0){
            
            $sql = "SELECT advice FROM advices where job LIKE '%" . $jobs[$i] . "%';";
            $result = mysqli_query($con, $sql);
            #echo $sql;
            while ($inreg = $result->fetch_assoc())  
                $advices4[] = $inreg['advice'];
        
        }
    $list_advices = [];
    if($advices1!=null)
        $list_advices[] = $advices1;
    if($advices2!=null)
        $list_advices[] = $advices2;
    if($advices3!=null)
        $list_advices[] = $advices3;
    if($advices4!=null)
        $list_advices[] = $advices4;
 
    $uniqueAdvices = call_user_func_array('array_intersect', $list_advices);
    $uniqueAdvices = array_unique($uniqueAdvices);

    $json = json_encode($uniqueAdvices);
    echo $json;

    
}
 
?>