import Adafruit_DHT


class DHT22(object):
    sensor = Adafruit_DHT.DHT22
    pin = 17  # GPIO 17

    def get_temperature(self):
        _, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temperature is not None:
            return temperature
        else:
            return 999

    def get_humidity(self):
        humidity, _ = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None:
            return humidity
        else:
            return 999


if __name__ == '__main__':
    print(DHT22().get_temperature())
    print(DHT22().get_humidity())
