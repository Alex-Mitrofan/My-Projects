<?php

if(isset($_COOKIE["username"]) == False){

    header('Location: Home', true, 303);
}

#Avatar picture for menu
require '../models/profile_model.php';

$arr = get_user($_COOKIE["username"]);
$avatar = $arr[8];

#declare options for advices
$age='';
$ocupation='';
$context='';
$job='';

#check if options were set
#AGE
if(isset($_POST["age1"]))
    if($age)
        $age .= "," . $_POST["age1"];
    else
        $age .= $_POST["age1"];

if(isset($_POST["age2"]))
    if($age)
        $age .= "," . $_POST["age2"];
    else
        $age .= $_POST["age2"];

if(isset($_POST["age3"]))
    if($age)
        $age .= "," . $_POST["age3"];
    else
        $age .= $_POST["age3"];
#OCUPATION

if(isset($_POST["ocupation1"]))
    if($ocupation)
        $ocupation .= "," . $_POST["ocupation1"];
    else
        $ocupation .= $_POST["ocupation1"];

if(isset($_POST["ocupation2"]))
    if($ocupation)
        $ocupation .= "," . $_POST["ocupation2"];
    else
        $ocupation .= $_POST["ocupation2"];

if(isset($_POST["ocupation3"]))
    if($ocupation)
        $ocupation .= "," . $_POST["ocupation3"];
    else
        $ocupation .= $_POST["ocupation3"];

#CONTEXT
if(isset($_POST["context1"]))
    if($context)
        $context .= "," . $_POST["context1"];
    else
        $context .= $_POST["context1"];

if(isset($_POST["context2"]))
    if($context)
        $context .= "," . $_POST["context2"];
    else
        $context .= $_POST["context2"];

if(isset($_POST["context3"]))
    if($context)
        $context .= "," . $_POST["context3"];
    else
        $context .= $_POST["context3"];

#JOB
if(isset($_POST["job1"]))
    if($job)
        $job .= "," . $_POST["job1"];
    else
        $job .= $_POST["job1"];

if(isset($_POST["job2"]))
    if($job)
        $job .= "," . $_POST["job2"];
    else
        $job .= $_POST["job2"];

if($age == '')
    $age = 0;
if($context == '')
    $context = 0;
if($ocupation == '')
    $ocupation = 0;
if($job == '')
    $job = 0;

require '../models/advices_model.php';
 
$advices = get_advices($age, $ocupation, $context, $job);
    
require '../views/advices.php';

?>