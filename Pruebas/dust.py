# coding=utf-8
import time
import aqi
from Raspberry.sds011 import *

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)


def get_data():
    return sensor.query()


def conv_aqi(pmt_2_5, pmt_10):
    aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pmt_2_5))
    aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pmt_10))
    return aqi_2_5, aqi_10


sensor.sleep(sleep=False)
try:
    while True:
        time.sleep(5)
        pmt_2_5, pmt_10 = get_data()
        aqi_2_5, aqi_10 = conv_aqi(pmt_2_5, pmt_10)
        tPayload = "PMT2.5: " + str(pmt_2_5) + "μg/m3 (AQI:" + str(aqi_2_5) + ")" + \
                   "PMT10: " + str(pmt_10) + "μg/m3 (AQI:" + str(aqi_10) + ")"
        print(tPayload)
except KeyboardInterrupt:
    sensor.sleep(sleep=True)
