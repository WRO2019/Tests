from ev3dev.ev3 import *
from time import sleep
import logging

Sensor("in1").mode = 'AC'

while True:
    print(Sensor("in1").value())

