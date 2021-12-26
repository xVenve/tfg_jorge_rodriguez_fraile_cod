import mysql.connector


class DB:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )

    # Insert measurements into DB
    def insert_sensor_data_DB(self, values):
        with self.mydb.cursor() as mycursor:
            sql = "INSERT INTO sensor_data (date, device, temperature, humidity, pm2_5, pm10, co, co2)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s); "
            val = (
                values["date"],
                values["device"],
                values["temperature"],
                values["humidity"],
                values["pm2_5"],
                values["pm10"],
                values["co"],
                values["co2"],
            )
            mycursor.execute(sql, val)
            self.mydb.commit()
            print(val, "inserted.")

    # Insert/Update device status into DB
    def insert_update_device_DB(self, params):
        with self.mydb.cursor() as mycursor:
            sql = "INSERT INTO devices (id, ip, date, status) VALUES (%s, %s, %s, %s)"
            val = (
                params["device"],
                params["ip"],
                params["date"],
                params["status"],
            )
            try:
                mycursor.execute(sql, val)
                self.mydb.commit()
                print(params["device"], "inserted")
            except mysql.connector.errors.IntegrityError:
                sql = "UPDATE devices SET date=%s, ip=%s, status=%s WHERE id=%s"
                val = (params["date"], params["ip"], params["status"], params["device"])
                mycursor.execute(sql, val)
                self.mydb.commit()
                print(params["device"], "updated to", params["status"])
