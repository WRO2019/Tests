from enum import Enum
from Sensors import Sensor

############################################################

ir_seeker_angle_area = 180


############################################################

class Colors(Enum):
    no_color = "no_color"
    black = "black"
    blue = "blue"
    green = "green"
    yellow = "yellow"
    red = "red"
    white = "white"
    brown = "brown"


############################################################

colors = {
    0: Colors.no_color,
    1: Colors.black,
    2: Colors.blue,
    3: Colors.green,
    4: Colors.yellow,
    5: Colors.red,
    6: Colors.white,
    7: Colors.brown
}


############################################################

class Ports(Enum):
    in1 = "in1"
    in2 = "in2"
    in3 = "in3"
    in4 = "in4"


############################################################

class SensorTypes(Enum):
    gyro_sensor = "gyro_sensor"
    ir_sensor = "ir_sensor"
    button_sensor = "button_sensor"
    colour_sensor = "colour_sensor"


############################################################

class SensorModes(Enum):
    ir_gefilter = 'AC-ALL'
    ir_ungefiltert = 'DC-ALL'
    color = 'COL-COLOR'
    reflect = 'COL-REFLECT'
    ambiente = 'COL-AMBIENT'


############################################################

class ValueTypes(Enum):
    raw = "raw"
    ################################
    # gyro sensor
    gyro_angle = "gyro_angle"
    gyro_angle_smooth = "gyro_angle_smooth"
    ################################
    # ir seeker
    ir_distance = "ir_distance"
    ir_direction = "ir_direction"
    ir_angle = "ir_angle"
    ir_distance_smooth = "ir_distance_smooth"
    ir_direction_smooth = "ir_direction_smooth"
    ir_angle_smooth = "ir_angle_smooth"
    ################################
    # color sensor
    color = "color"
    reflect = "reflect"
    ambiente = "ambiente"


############################################################

ir_seeker = Sensor(Ports.in1, SensorModes.ir_gefilter)
gyro_sensor = Sensor(Ports.in2, None)
color_sensor = Sensor(Ports.in3, None)

gyro_sensor.start_reading_threads(ValueTypes.gyro_angle_smooth, 2, 5, 0.1)
ir_seeker.start_reading_threads(ValueTypes.ir_direction_smooth, 2, 5, 0.1)
ir_seeker.start_reading_threads(ValueTypes.ir_angle_smooth, 2, 5, 0.1)

############################################################
