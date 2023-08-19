<?php
require '../models/contact_model.php';
if (isset($_POST["email"]) && isset($_POST["message"]))
{
   send_the_feedback($_POST["email"],$_POST["message"]);
   $_POST["email"]=null;
   $_POST["message"]=null;
}

require '../models/profile_model.php';

if(isset($_COOKIE["username"]) == True){
    $arr = get_user($_COOKIE["username"]);
    $avatar = $arr[8];
  }

require '../views/contact.php';

?>