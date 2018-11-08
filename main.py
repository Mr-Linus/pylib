import time
import serial
import pynmea2
from lib.gps import GPS
from lib.sms import SMS
from lib.gprs import GPRS

g = GPRS()
g.get_network_register()
g.get_signal_quality()
g.get_attach_network()
g.get_apn()
g.get_ip()