create database tfg_db;

CREATE USER 'xvenve'@'%' IDENTIFIED VIA mysql_native_password USING '[n.A@Muz/mJpX.xf';

GRANT USAGE ON *.* TO 'xvenve'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tfg_db.* TO 'xvenve'@'%' WITH GRANT OPTION;

use tfg_db;

CREATE TABLE sensor_data (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    date DATETIME NOT NULL,
    device VARCHAR(50) NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    pm2_5 FLOAT NOT NULL,
    pm10 FLOAT NOT NULL,
    co FLOAT NOT NULL,
    co2 MEDIUMINT NOT NULL,
    intruder tinyint(1) NOT NULL,
    PRIMARY KEY (id)
);

SELECT * FROM sensor_data ORDER BY id DESC;

CREATE TABLE devices (
    id varchar(50) NOT NULL,
    date varchar(50) NOT NULL,
    status varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

SELECT * FROM devices ORDER BY id DESC;

CREATE TABLE IF NOT EXISTS `users` (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(250) NOT NULL,
  password varchar(250) NOT NULL,
  PRIMARY KEY (id)
 );