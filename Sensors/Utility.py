from enum import Enum

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
    ################################
    # ultrasonic distance
    ultrasonic_distance = "ultrasonic_distance"

############################################################
