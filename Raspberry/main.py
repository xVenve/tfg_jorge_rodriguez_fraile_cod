import uuid
from datetime import datetime
import time
import socket

from co2 import *
from database import *
from sds011 import *
from co import *
from temp_hum import *

# Device IP
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Device identification
device_id = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])

# Insert new device/Update device to Online
device_params = {
    "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "ip": get_ip(),
    "status": "Online",
    "device": device_id,
}
insert_update_device_DB(device_params)

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
    init_co_sensor()
    time.sleep(16)

    while True:
        time.sleep(4)

        temperature, humidity = temp_hum_sensor.tempHumSensor()
        co = co_sensor_readadc(mq7_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
        co2 = co2_sensor.get()
        pm2_5, pm10 = dust_sensor.query()
        intruder = 0

        # Insert measurements
        data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "device": device_id,
            "temperature": temperature,
            "humidity": humidity,
            "pm2_5": pm2_5,
            "pm10": pm10,
            "co": str("%.2f" % ((co / 1024.) * 100)),
            "co2": co2,
            "intruder": intruder,
        }
        insert_sensor_data_DB(data)

except KeyboardInterrupt:
    GPIO.cleanup()

    # Stop dust sensor
    dust_sensor.sleep(sleep=True)

    # Update device to Offline
    device_params = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": get_ip(),
        "status": "Offline",
        "device": device_id,
    }
    insert_update_device_DB(device_params)
