<?php
//connecting to the database
session_start();
$host = "localhost";    /* Host name */
$user = "root";         /* User */
$password = "";         /* Password */
$dbname = "test-website";     /* Database name */
$con = mysqli_connect($host, $user, $password,$dbname);

?>