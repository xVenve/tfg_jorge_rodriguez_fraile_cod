import json

import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="192.168.1.40",
        user="xvenve",
        password="[n.A@Muz/mJpX.xf",
        database="prueba"
    )
    return mydb


def getDB():
    mydb = connect()
    r = []
    with mydb.cursor() as mycursor:
        mycursor.execute(
            "SELECT id, nombre FROM tabla_prueba ORDER BY id;")
        myresult = mycursor.fetchall()
        for key, nombre in myresult:
            r.append({"id": key, "nombre": nombre})
        mydb.commit()
        print(mycursor.rowcount, "record selected.")
    result = json.dumps(r, sort_keys=True)
    return result


def insertDB(params):
    mydb = connect()
    with mydb.cursor() as mycursor:
        sql = "INSERT INTO tabla_prueba (nombre) VALUES (%s);"
        val = (params["nombre"],)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


try:
    connect()
    print("Conectado con exito")
except mysql.connector.errors.ProgrammingError as error:
    print("Error al conectar ", error)
    exit(-1)

try:
    data = {"nombre": "MariaDB"}
    insertDB(data)
    print("Insertado con exito")
except mysql.connector.errors.ProgrammingError as error:
    print("Error al insertar ", error)
    exit(-1)

try:
    print(getDB())
    print("Recibido con exito")
    exit(0)
except mysql.connector.errors.ProgrammingError as error:
    print("Error al solicitar ", error)
    exit(-1)
