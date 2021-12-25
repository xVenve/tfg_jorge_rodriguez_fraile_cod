CREATE DATABASE tfg_db;

CREATE USER 'xvenve'@'%' IDENTIFIED VIA mysql_native_password USING '[n.A@Muz/mJpX.xf';

GRANT USAGE ON *.* TO 'xvenve'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tfg_db.* TO 'xvenve'@'%' WITH GRANT OPTION;

CREATE USER 'tfg_user'@'%' IDENTIFIED VIA mysql_native_password USING '***';
GRANT ALL PRIVILEGES ON tfg_db.* TO 'tfg_user'@'%';

CREATE USER 'device_user'@'%' IDENTIFIED VIA mysql_native_password USING '***';
GRANT INSERT, UPDATE ON *.* TO 'device_user'@'%';

use tfg_db;

CREATE TABLE sensor_data (
  date datetime NOT NULL,
  device varchar(50) NOT NULL,
  temperature float NOT NULL,
  humidity float NOT NULL,
  pm2_5 float NOT NULL,
  pm10 float NOT NULL,
  co float NOT NULL,
  co2 mediumint(9) NOT NULL,
  PRIMARY KEY (date,device),
  CONSTRAINT deviceData FOREIGN KEY (device) 
  REFERENCES devices(id) ON DELETE CASCADE ON UPDATE CASCADE
);

SELECT * FROM sensor_data ORDER BY id DESC;

CREATE TABLE devices (
  id varchar(50) NOT NULL,
  ip varchar(16) NOT NULL,
  date varchar(19) NOT NULL,
  status varchar(7) NOT NULL,
  PRIMARY KEY (id)
);

SELECT * FROM devices ORDER BY id DESC;

CREATE TABLE users (
  username varchar(32) NOT NULL,
  password varchar(32) NOT NULL,
  PRIMARY KEY (username)
);