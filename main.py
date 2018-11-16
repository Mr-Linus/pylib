import time
import serial
import pynmea2
from lib.gps import GPS
from lib.sms import SMS
from lib.gprs import GPRS

g=GPS()
g.print_gps()
g.print_bd()