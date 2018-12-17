import time
import serial
import pynmea2
from lib.gps import GPS
from lib.sms import SMS
from lib.gprs import GPRS



# demo for gprs
g = GPRS()
g.print_signal_quality()
g.print_network_register()
g.activate_mobile_scene()
g.print_attach_network()
g.print_apn()
g.print_ip()
