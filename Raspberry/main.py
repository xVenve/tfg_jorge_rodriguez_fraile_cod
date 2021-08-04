import uuid
from datetime import datetime
import time
from database import *
from temp_hum import *

device_id = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])

device_params = {
    "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "status": "Online",
    "device": device_id,
}
insert_update_device_DB(device_params)

try:
    while True:
        temperature, humidity = tempHumSensor()
        pm2_5, pm10 = 2.5, 10
        co = 1
        co2 = 2
        intruder = 0

        data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "device": device_id,
            "temperature": temperature,
            "humidity": humidity,
            "pm2_5": pm2_5,
            "pm10": pm10,
            "co": co,
            "co2": co2,
            "intruder": intruder,
        }
        insert_sensor_data_DB(data)

        time.sleep(5)
except KeyboardInterrupt:
    device_params = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Offline",
        "device": device_id,
    }
    insert_update_device_DB(device_params)
