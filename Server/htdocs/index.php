<?php
$connect = mysqli_connect("localhost", "xvenve", "[n.A@Muz/mJpX.xf", "tfg_db");
session_start();
if (isset($_SESSION["username"])) {
    header("location:main.php");
}
if (isset($_POST["login"])) {
    if (empty($_POST["username"]) && empty($_POST["password"])) {
        echo '<script>alert("Ambos campos son obligatorios")</script>';
    } else {
        $username = mysqli_real_escape_string($connect, $_POST["username"]);
        $password = mysqli_real_escape_string($connect, $_POST["password"]);
        $password = md5($password);
        $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
        $result = mysqli_query($connect, $query);
        if (mysqli_num_rows($result) > 0) {
            $_SESSION['username'] = $username;
            header("location:main.php");
        } else {
            echo '<script>alert("Compruebe los credenciales")</script>';
        }
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>CPD Control</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <link href="styles.css" rel="stylesheet" />
</head>

<body>
    <br><br />
    <div class="container all" style="width:500px;">
        <h3 align="center">Inicio de sesión</h3>
        <br /><br />
        <form method="post">
            <label>Nombre de usuario</label>
            <input type="text" name="username" class="form-control" /><br />
            <label>Contraseña</label>
            <input type="password" name="password" class="form-control" /><br />
            <input type="submit" name="login" value="Iniciar sesión" class="btn btn-info" /><br />
        </form>
    </div>
</body>

</html>