<?php
require '../models/ranking_model.php';
if (isset($_GET["id"]))
{
  $page_info=get_first_users_for_page($_GET["id"]);
  $best_of_3=get_first_three_users();
  $_GET["id"]=null;
}

require '../models/profile_model.php';

if(isset($_COOKIE["username"]) == True){
  $arr = get_user($_COOKIE["username"]);
  $avatar = $arr[8];
}

require '../views/ranking.php';
?>