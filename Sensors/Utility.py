from ev3dev.ev3 import *

############################################################
# Sensors
gyro_sensor = Sensor('in3')
irSeeker = Sensor("in1")
irSeeker.mode = "AC"
ultrasonic_Sensor = Sensor("in2")
button = Sensor("in4")

############################################################
# Fix Values
directions = {0: 8888,  # 112.5
              1: 8888,
              2: -105,  # 90
              3: -75,
              4: -45,
              5: 0,
              6: 45,
              7: 75,
              8: 105,
              9: 8888,
              }
