import time
import serial


class AT:
    restore_command = "ATZ\r\n".encode()
    ser = serial.Serial("/dev/ttyS0", 115200)

    def run_at(self, command):
        self.ser.write(command)
        time.sleep(2)
        print(self.ser.readline().decode())

    def restore(self):
        self.run_at(self.restore_command)

