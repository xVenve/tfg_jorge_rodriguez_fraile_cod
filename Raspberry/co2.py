import serial


class CO2Sensor:
    request = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]

    def __init__(self, port='/dev/ttyS0'):
        self.serial = serial.Serial(
            port=port,
            timeout=1
        )

    def get(self):
        self.serial.write(bytearray(self.request))
        response = self.serial.read(9)
        if len(response) == 9:
            return (response[2] << 8) | response[3]
        return -1
