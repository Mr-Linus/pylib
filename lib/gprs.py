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
        print("GPRS signal Quality:"+str(self.signal_quality()))
