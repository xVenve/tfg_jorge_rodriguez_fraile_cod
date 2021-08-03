from datetime import datetime
import Adafruit_DHT
import time


def tempHumSensor():
    dht_sensor = Adafruit_DHT.DHT11
    dht_pin = 4

    while True:
        humidity, temperature = Adafruit_DHT.read(dht_sensor, dht_pin)

        if temperature is not None and humidity is not None:
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                  ": Temperatura: {0:0.1f} °C | Humedad: {1:0.1f} %".format(temperature, humidity))
        else:
            print("Error de lectura")
        time.sleep(2)


try:
    print(tempHumSensor())
except KeyboardInterrupt:
    exit(0)