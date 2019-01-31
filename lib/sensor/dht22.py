import Adafruit_DHT


class DHT22(object):
    # Init the class
    sensor = Adafruit_DHT.DHT22
    pin = 17  # GPIO Number

    def get_temperature(self):
        """
        Description: Get the temperature with the dht22 sensor.
        :return: Temperature number or error number: 999.
        """
        _, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temperature is not None:
            return temperature
        else:
            return 999

    def get_humidity(self):
        """
        Description: Get the humidity with the dht22 sensor.
        :return: Humidity number or error number: 999.
        """
        humidity, _ = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None:
            return humidity
        else:
            return 999


# Used to test the function work status.
# Get the temperature & humidity data from dht22 if you run this file.
if __name__ == '__main__':
    print(DHT22().get_temperature())
    print(DHT22().get_humidity())
