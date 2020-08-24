<?php
require('dbconnect.php');
if (isset($_POST['user']) and isset($_POST['pass'])) {

    // Assigning POST values to variables.
    $username = $_POST['user'];
    $password = $_POST['pass'];

    // CHECK FOR THE RECORD FROM TABLE
    $query = "SELECT * FROM admin WHERE username='$username' and password='$password' ";
    $result = mysqli_query($connection, $query);
    $count = mysqli_num_rows($result);

    if ($count == 1) {
        echo "<script type='text/javascript'>alert('Login Successful')</script>";
        header("Location: ty.php");
    } else {
        //header("location: index.html");
        echo "Invalid Login Credentials";
        echo "<script type='text/javascript'>alert('Invalid Login Credential')</script>";
    }
}
?>