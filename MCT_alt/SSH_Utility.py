from enum import Enum

class Values():
    gyro_angle = 404
    gyro_angle_smooth = 404
    ################################
    # ir seeker
    ir_distance = 404
    ir_direction = 404
    ir_angle = 404
    ir_distance_smooth = 404
    ir_direction_smooth = 404
    ir_angle_smooth = 404
    ################################
    # color sensor
    color = 404
    reflect = 404
    ambiente = 404


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
