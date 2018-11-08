import time
import serial


class GPRS:


    # define Serial
    ser = serial.Serial("/dev/ttyS0", 115200)
    # define AT command
    q_signal_quality = "AT+CSQ\r\n".encode()
    q_network_register = "AT+CREG?\r\n".encode()
    q_attach_network = "AT+CGATT?\r\n".encode()
    q_apn = "AT+CSTT?\r\n".encode()
    s_apn = "AT+CSTT=\"CMNET\"\r\n".encode()
    q_ip = "AT+CIFSR\r\n".encode()
    mobile_scene = "AT+CIICR\r\n".encode()

    def run_at(self, command):
        self.ser.write(command)
        time.sleep(1)

    def signal_quality(self):
        self.run_at(self.q_signal_quality)
        while True:
            line = self.ser.readline().decode()
            if "+CSQ:" in line:
                result = int(str(line).split(':')[1].split(',')[0])
                break
        return result

    def get_signal_quality(self):
        print("GPRS signal Quality: "+str(self.signal_quality()))

    def network_register(self):
        self.run_at(self.q_network_register)
        while True:
            line = self.ser.readline().decode()
            if "+CREG:" in line:
                result = int(str(line).split(':')[1].split(',')[1])
                break
        return result

    def get_network_register(self):
        print("Network Registration: "+str(self.network_register()))

    def attach_network(self):
        self.run_at(self.q_attach_network)
        while True:
            line = self.ser.readline().decode()
            if "+CGATT:" in line:
                result = int(str(line).split(':')[1])
                break
        return result

    def get_attach_network(self):
        print("Attach GPRS Network: "+str(self.attach_network()))

    def apn_info(self):
        self.run_at(self.q_apn)
        while True:
            line = self.ser.readline().decode()
            if "+CSTT:" in line:
                result = str(line).split("\"")[1]
                break
        return result

    def get_apn(self):
        print("APN: "+self.apn_info())

    def set_apn(self):
        self.run_at(self.s_apn)
        while True:
            line = self.ser.readline().decode()
            if "ERROR" in line:
                result = 1
                break
            if "OK" in line:
                result = 0
                break
        return result

    def activate_mobile_scene(self):
        self.run_at(self.mobile_scene)
        while True:
            line = self.ser.readline().decode()
            if "ERROR" in line:
                result = 1
                break
            if "OK" in line:
                result = 0
                break
        return result

    def ip(self):
        self.run_at(self.q_ip)
        while True:
            line = self.ser.readline().decode()
            if '.' in line:
                result = str(line)
                break
        return result

    def get_ip(self):
        print("IP:"+self.ip())