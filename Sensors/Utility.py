from enum import Enum

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

############################################################
# Definiere Ports
class Ports(Enum):
    in1 = "in1"
    in2 = "in2"
    in3 = "in3"
    in4 = "in4"


############################################################

class Sensors(Enum):
    gyro_sensor = "gyro_sensor"
    ir_sensor = "ir_sensor"
    us_sensor = "us_sensor"
    button_sensor = "button_sensor"
    colour_sensor = "colour_sensor"
