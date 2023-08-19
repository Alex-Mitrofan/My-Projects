<?php
require "../models/update_profile_model.php"; 
 

if(isset($_POST["name"])) 
    $name = $_POST['name'];
if(isset($_POST["location"])) 
    $location = $_POST['location'];
if(isset($_POST["age"])) 
    $age = $_POST['age'];
if(isset($_POST["sex"])) 
    $sex = $_POST['sex'];
if(isset($_POST["ocupation"])) 
    $ocupation = $_POST['occupation'];
 
update_user($username, $name, $location, $age, $sex, $ocupation); 
    
 
?>