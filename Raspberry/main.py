import socket
import threading
import time
import uuid
from datetime import datetime

from cam_on_web import *
from co import *
from co2 import *
from database import *
from sds011 import *
from temp_hum import *


class cpdDevice:
    def __init__(self):
        self.start()

    # Device IP
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip

    # Device identification
    def get_device_id(self):
        return ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])

    # Run device functions
    def start(self):
        db = DB("192.168.1.40", "device_user", "device_pass", "tfg_db")
        # Insert new device/Update device to Online
        device_params = {
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "ip": self.get_ip(),
            "status": "Online",
            "device": self.get_device_id(),
        }
        db.insert_update_device_DB(device_params)

        # Stream device cam
        camera = threading.Thread(target=cam_web)
        camera.start()

        # Temperature and Humidity sensor
        temp_hum_sensor = DHT11()

        # Dust sensor
        dust_sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

        # CO2 sensor
        co2_sensor = CO2Sensor('/dev/ttyAMA0')

        try:
            print("Sensors warming up...")
            # Start dust sensor
            dust_sensor.sleep(sleep=False)

            # Start CO sensor
            co_sensor = COSensor()
            time.sleep(16)

            while True:
                time.sleep(4)

                temperature, humidity = temp_hum_sensor.tempHumSensor()
                co = co_sensor.co_sensor_readadc()
                co2 = co2_sensor.get()
                pm2_5, pm10 = dust_sensor.query()

                # Insert measurements
                data = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "device": self.get_device_id(),
                    "temperature": temperature,
                    "humidity": humidity,
                    "pm2_5": pm2_5,
                    "pm10": pm10,
                    "co": str("%.2f" % ((co / 1024.) * 100)),
                    "co2": co2,
                }
                db.insert_sensor_data_DB(data)

        except KeyboardInterrupt:
            GPIO.cleanup()

            # Stop dust sensor
            dust_sensor.sleep(sleep=True)

            # Update device to Offline
            device_params = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ip": self.get_ip(),
                "status": "Offline",
                "device": self.get_device_id(),
            }
            db.insert_update_device_DB(device_params)


if __name__ == '__main__':
    cpd = cpdDevice()
