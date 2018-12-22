import serial
import time


class SMS:
    sms_center = "86 13 80 02 50 50 0F"
    pdu_sms_center = "0891683108200505F0"
    pdu_sms_receiver = "685100253703F1"
    receive_phone = "AT+CMGS=\"+8615005273301\"\n"
    set_text_mode = "AT+CMGF=1\r\n"
    text = "helloworld\n"
    ser = serial.Serial("/dev/ttyS0", 115200)
    data = ""
    W_buff = [set_text_mode, receive_phone, text]
    num = 1

    def send_text_phone(self):
        self.ser.write(self.W_buff[0].encode())
        while True:
            while self.ser.inWaiting() > 0:
                self.data += self.ser.read(self.ser.inWaiting()).decode()
            if self.data != "":
                print(self.data)
                # if data.count("O") > 0 and data.count("K") > 0 and num < 3:	# the string have ok
                if self.num < 2:
                    time.sleep(1)
                    self.ser.write(self.W_buff[1].encode())
                    time.sleep(1)
                    self.ser.write("\n".encode())
                else:
                    return

    def send_text_message(self):
        while True:
            while self.ser.inWaiting() > 0:
                self.data += self.ser.read(self.ser.inWaiting()).decode()
            if ">" in self.data:
                self.ser.write(self.W_buff[2].encode())
                time.sleep(1)
                self.ser.write("\x1a\r\n".encode())
                return

