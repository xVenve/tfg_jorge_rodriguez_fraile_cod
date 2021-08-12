import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="192.168.1.40",
        user="xvenve",
        password="[n.A@Muz/mJpX.xf",
        database="tfg_db",
    )
    return mydb


def insert_sensor_data_DB(values):
    mydb = connect()
    with mydb.cursor() as mycursor:
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
        mydb.commit()
        print(val, "inserted.")


def insert_update_device_DB(params):
    mydb = connect()
    with mydb.cursor() as mycursor:
        sql = "INSERT INTO devices (id, ip, date, status) VALUES (%s, %s, %s, %s)"
        val = (
            params["device"],
            params["ip"],
            params["date"], 
            params["status"],
        )
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(params["device"], "inserted")
        except mysql.connector.errors.IntegrityError:
            sql = "UPDATE devices SET date=%s, ip=%s, status=%s WHERE id=%s"
            val = (params["date"], params["ip"], params["status"], params["device"])
            mycursor.execute(sql, val)
            mydb.commit()
            print(params["device"], "updated to", params["status"])
