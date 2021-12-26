import Adafruit_DHT


class DHT11:
    def __init__(self):
        self.humidity = None
        self.temperature = None

    # Read temperature and humidity
    def tempHumSensor(self):
        dht_sensor = Adafruit_DHT.DHT11
        dht_pin = 4

        new_humidity, new_temperature = Adafruit_DHT.read(dht_sensor, dht_pin)
        if (new_humidity is None and new_temperature is None) or new_temperature not in range(0, 101) or \
                new_humidity not in range(0, 101):
            if (self.humidity is None and self.temperature is None) or self.temperature not in range(0, 101) or \
                    self.humidity not in range(0, 101):
                while (new_humidity is None and new_temperature is None) or new_temperature not in range(0, 101) or \
                        new_humidity not in range(0, 101):
                    new_humidity, new_temperature = Adafruit_DHT.read(dht_sensor, dht_pin)
                    self.humidity, self.temperature = new_humidity, new_temperature
            return self.temperature, self.humidity
        else:
            self.humidity, self.temperature = new_humidity, new_temperature
            return self.temperature, self.humidity
