create database prueba;

CREATE USER 'xvenve'@'%' IDENTIFIED VIA mysql_native_password USING '[n.A@Muz/mJpX.xf';

GRANT USAGE ON *.* TO 'xvenve'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON prueba.* TO 'xvenve'@'%' WITH GRANT OPTION;

use prueba;

CREATE TABLE tabla_prueba (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

SELECT * FROM tabla_prueba ORDER BY id DESC;
