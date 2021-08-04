import Adafruit_DHT


def tempHumSensor():
    dht_sensor = Adafruit_DHT.DHT11
    dht_pin = 4

    humidity, temperature = Adafruit_DHT.read(dht_sensor, dht_pin)
    while (humidity is None and temperature is None) or temperature not in range(0, 101) \
            or humidity not in range(0, 101):
        humidity, temperature = Adafruit_DHT.read(dht_sensor, dht_pin)
        print(temperature, humidity)

    return temperature, humidity
