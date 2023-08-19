<?php
require '../models/view_the_feedback_model.php';
$feedbacks=get_feedbacks();
require '../views/view_the_feedback.php';
?>