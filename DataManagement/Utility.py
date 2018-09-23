from enum import Enum


class Values():
    gyro_angle = None
    gyro_angle_smooth = None
    ################################
    # ir seeker
    ir_distance = None
    ir_direction = None
    ir_angle = None
    ir_distance_smooth = None
    ir_direction_smooth = None
    ir_angle_smooth = None
    ################################
    # color sensor
    color = None
    reflect = None
    ambiente = None


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
    ir_distance_smooth = "ir_distance_smooth"
    ir_direction_smooth = "ir_direction_smooth"
    ir_angle_smooth = "ir_angle_smooth"
    ir_angle = "ir_angle"
    ################################
    # color sensor
    color = "color"
    reflect = "reflect"
    ambiente = "ambiente"


class Value():
    valueType: ""
    value: "Test"

    def __init__(self, value, name):
        self.valueType = name
        self.value = value
