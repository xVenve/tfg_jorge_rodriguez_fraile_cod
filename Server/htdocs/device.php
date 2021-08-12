<?php
session_start();
if (!isset($_SESSION["username"])) {
    header("location:index.php?action=login");
}

$con = mysqli_connect("localhost", "xvenve", "[n.A@Muz/mJpX.xf", "tfg_db");
if (!$con) {
    die("Connection failed: " . mysqli_connect_error());
}

$chartQuery = 'SELECT * FROM (SELECT * FROM sensor_data WHERE device="' . $_GET["id"] . '" ORDER BY id DESC LIMIT 720) sub ORDER BY id ASC';
$chartQueryRecords = mysqli_query($con, $chartQuery);
?>

<!DOCTYPE html>
<html>

<head>
    <title><?php echo $_GET["id"] ?></title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <link href="styles.css" rel="stylesheet" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
        google.charts.load('current', {
            'packages': ['corechart'],
            'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
        });
        google.charts.setOnLoadCallback(drawCharts);

        function drawCharts() {
            var data = google.visualization.arrayToDataTable([
                ['Fecha', 'Temperatura', 'Humedad', 'PM2.5', 'PM10', 'CO', 'CO2'],
                <?php
                while ($row = mysqli_fetch_assoc($chartQueryRecords)) {
                    echo "['" . $row['date'] . "'," . $row['temperature'] . "," . $row['humidity'] . "," . $row['pm2_5'] . "," . $row['pm10'] . "," . $row['co'] . "," . $row['co2'] . "],";
                }
                ?>
            ]);
            var options = {};

            var view = new google.visualization.DataView(data);
            view.setColumns([0, 1, 2]);
            var view2 = new google.visualization.DataView(data);
            view2.setColumns([0, 3, 4, 5]);
            var view3 = new google.visualization.DataView(data);
            view3.setColumns([0, 6]);

            var chart = new google.visualization.LineChart(document.getElementById('regions_temp_hum'));
            chart.draw(view, options);
            var chart = new google.visualization.LineChart(document.getElementById('regions_pm_co'));
            chart.draw(view2, options);
            var chart = new google.visualization.LineChart(document.getElementById('regions_co2'));
            chart.draw(view3, options);
        }
    </script>
</head>

<body style="background-color:#6495ED;">
    <div class="all">
        <div class="center">
            <?php
            echo '<h1>' . $_GET["id"] . '</h1>';

            echo '<img src="http://' . $_GET["ip"] . ':8000/stream.mjpg" width="100%">'
            ?>

            <button class="boton" id="boton_volver" onclick="location.href=' main.php'">Volver</button>
            <br></br>

            <div id="regions_temp_hum" style="width: 100%; height: 500px;"></div>
            <div id="regions_pm_co" style="width: 100%; height: 500px;"></div>
            <div id="regions_co2" style="width: 100%; height: 500px;"></div>
            <button class="boton" id="boton_volver" onclick="location.href=' main.php'">Volver</button>
            <br></br>

            <?php
            $query = 'SELECT * FROM sensor_data WHERE device="' . $_GET["id"] . '" ORDER BY id DESC LIMIT 500';
            $result = mysqli_query($con, $query);

            echo "<table class='tables'>
            <tr>
                <th>Fecha</th>
                <th>Temperatura</th>
                <th>Humedad</th>
                <th>PM<sub>2.5</sub></th>
                <th>PM<sub>10</sub></th>
                <th>CO</th>
                <th>CO<sub>2</sub></th>
            </tr>";
            while ($row = mysqli_fetch_array($result)) {
                echo "<tr>";
                echo "<td>" . $row['date'] . "</td>";
                echo "<td>" . $row['temperature'] . "</td>";
                echo "<td>" . $row['humidity'] . "</td>";
                echo "<td>" . $row['pm2_5'] . "</td>";
                echo "<td>" . $row['pm10'] . "</td>";
                echo "<td>" . $row['co'] . "</td>";
                echo "<td>" . $row['co2'] . "</td>";
                echo "</tr>";
            }
            echo "</table>";
            ?>
            <button class="boton" id="boton_volver" onclick="location.href=' main.php'">Volver</button>
        </div>
    </div>
</body>

</html>