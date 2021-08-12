<?php
session_start();
if (!isset($_SESSION["username"])) {
    header("location:index.php?action=login");
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>CPD Control</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <link href="styles.css" rel="stylesheet" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>

<body style="background-color:#6495ED;">
    <div class="all">
        <div class="center">

            <?php
            echo '<h1>Bienvenido, ' . $_SESSION["username"] . '</h1>';

            $connect = mysqli_connect("localhost", "xvenve", "[n.A@Muz/mJpX.xf", "tfg_db");

            $query = "SELECT * FROM devices";
            $result = mysqli_query($connect, $query);
            echo "<table class='tables'>
            <tr>
                <th>Nombre del dispositivo</th>
                <th>Estado</th>
                <th>Último cambio de estado</th>
                <th>Control</th>
            </tr>";

            while ($row = mysqli_fetch_array($result)) {
                echo "<tr>";
                echo "<td>" . $row['id'] . "</td>";
                echo "<td>" . $row['status'] . "</td>";
                echo "<td>" . $row['date'] . "</td>";
                echo '<td><button class="boton" onclick="location.href=\'device.php?id=' . $row['id'] . '&ip=' . $row['ip'] . '\'">Acceder</button></td>';

                echo "</tr>";
            }
            echo "</table>";
            ?>
            <button class="boton" id="boton_volver" onclick="location.href='logout.php'">Cerrar sesión</button>

        </div>
    </div>
</body>

</html>