<?php
$conn=new mysqli(
    'localhost', // locatia serverului (aici, masina locala)
    'root',       // numele de cont
    '',    // parola (atentie, in clar!)
    'manners_matter',   // baza de date
);
if (mysqli_connect_errno()) {
    die ('Eror connection database challenge_model...');
}
function send_the_feedback($email,$feedback)
{
    global $conn;
    $email = mysqli_real_escape_string($conn, $email);
    $feedback = mysqli_real_escape_string($conn, $feedback);
    $currentDate = date("Y-m-d"); // Obține data curentă în formatul "YYYY-MM-DD"

    // Construim interogarea SQL de tipul INSERT
    $query = "INSERT INTO feedback (email, message, date) VALUES ('$email', '$feedback', '$currentDate')";

    // Executăm interogarea și verificăm rezultatul
    if (mysqli_query($conn, $query)) {
        return 1; // Inserarea a fost realizată cu succes
    } else {
        return 0; // Eroare la inserare
    }
}

?>