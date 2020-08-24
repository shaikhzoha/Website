<?php
require('dbconnect.php');
if (isset($_POST['user']) and isset($_POST['pass'])) {

    // Assigning POST values to variables.
    $username = $_POST['user'];
    $password = $_POST['pass'];

    // CHECK FOR THE RECORD FROM TABLE
    $query = "INSERT INTO `admin` (`username`, `password`) VALUES  ('$username','$password') ";
    $result = mysqli_query($connection, $query);
    
		echo "<script type='text/javascript'>alert('Login Successful')</script>";
        header("Location: ty_signup.php");
}
?>