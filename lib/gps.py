import time
import serial
import pynmea2


class GPS:
    GPSStart = "AT+CGNSPWR=1\r\n".encode()
    StatStart = "AT+CGNSTST=1\r\n".encode()
    StatStop = "AT+CGNSTST=0\r\n".encode()
    GPS_BD = "AT+CGNSMOD=1,0,1,0\r\n".encode()
    GPS_Only = "AT+CGNSMOD=1,0,0,0\r\n".encode()
    GPS_Info = "AT+CGNSINF\r\n".encode()

    ser = serial.Serial("/dev/ttyS0", 115200)

    def get_gps(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.GPS_Only)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPRMC" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNRMC" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return float(rmc.lat)/100, float(rmc.lon)/100

    def print_gps(self):
        lat, lon = self.get_gps()
        print("GPS Location: ")
        print("Latitude:  ", str(lat))
        print("Longitude: ", str(lon))

    def get_bd(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.GPS_BD)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPRMC" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNRMC" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return float(rmc.lat)/100, float(rmc.lon)/100

    def print_bd(self):
        lat, lon = self.get_bd()
        print("BeiDou Location:")
        print("Latitude:  ", str(lat))
        print("Longitude: ", str(lon))

    def get_gps_time(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPRMC" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNRMC" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return rmc.timestamp.replace(hour=rmc.timestamp.hour+8)

    def print_gps_time(self):
        print("GPS Time: "+str(self.get_gps_time()))

    def get_gps_altitude(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPGGA" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNGGA" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return rmc.altitude

    def print_gps_altitude(self):
        print("Current Altitude："+str(self.get_gps_altitude())+" m")

    def get_gps_speed(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPRMC" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNRMC" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return rmc.spd_over_grnd

    def print_gps_speed(self):
        print("Current Speed: "+str(self.get_gps_speed())+" Knots.")

    def get_gps_date(self):
        self.ser.write(self.GPSStart)
        time.sleep(0.5)
        self.ser.write(self.StatStart)
        while True:
            line = self.ser.readline().decode()
            if "$GPRMC" in line:
                rmc = pynmea2.parse(line)
                break
            elif "GNRMC" in line:
                rmc = pynmea2.parse(line)
                break
        self.ser.write(self.StatStop)
        return rmc.datestamp

    def print_gps_date(self):
        print("Current Time: "+str(self.get_gps_date()))