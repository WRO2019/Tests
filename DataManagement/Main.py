from Utility import *
from enum import Enum
gyro_sensor = "4"
ir_seeker = "2"
color_sensor = "0"


def get_prepared_value(sensor, valueType):
    return valueType + ":" + sensor + ";"


###############################################################################

output = "datas:"
output += get_prepared_value(gyro_sensor, ValueTypes.gyro_angle.value)
output += get_prepared_value(gyro_sensor, ValueTypes.gyro_angle_smooth.value)
#################################
output += get_prepared_value(ir_seeker, ValueTypes.ir_direction.value)
output += get_prepared_value(ir_seeker, ValueTypes.ir_direction_smooth.value)
output += get_prepared_value(ir_seeker, ValueTypes.ir_angle.value)
output += get_prepared_value(ir_seeker, ValueTypes.ir_angle_smooth.value)
output += get_prepared_value(ir_seeker, ValueTypes.ir_distance.value)
output += get_prepared_value(ir_seeker, ValueTypes.ir_distance_smooth.value)
#################################
output += get_prepared_value(color_sensor, ValueTypes.color.value)
output += get_prepared_value(color_sensor, ValueTypes.reflect.value)
output += get_prepared_value(color_sensor, ValueTypes.ambiente.value)

###############################################################################
# Werte entschlüsseln

print(output)

if output[0:6] == "datas:":
    values_text = output[6:output.__len__()]
    values = []
    value_type = ""
    value = ""
    value_active = False
    for key in values_text:
        if value_active:  # Value
            if key != ";":
                value += key
            else:
                values.append(Value(value, value_type,))
                value_active = False
                value = ""
                value_type = ""
        else:  # Value Type
            if key != ":":
                value_type += key
            else:
                if key == ":":
                    value_active = True

    print(values)

    for value in values:
        if value.valueType == ValueTypes.ambiente.value:
            Values.ambiente = value.value
        elif value.valueType == ValueTypes.reflect.value:
            Values.reflect = value.value
        elif value.valueType == ValueTypes.color.value:
            Values.color = value.value
            ##
        elif value.valueType == ValueTypes.ir_distance_smooth.value:
            Values.ir_distance_smooth = value.value
        elif value.valueType == ValueTypes.ir_distance.value:
            Values.ir_distance = value.value
            ##
        elif value.valueType == ValueTypes.ir_angle_smooth.value:
            Values.ir_angle_smooth = value.value
        elif value.valueType == ValueTypes.ir_angle.value:
            Values.ir_angle = value.value
            ##
        elif value.valueType == ValueTypes.ir_direction_smooth.value:
            Values.ir_direction_smooth = value.value
        elif value.valueType == ValueTypes.ir_direction_smooth.value:
            Values.ir_direction_smooth = value.value
            ##
        elif value.valueType == ValueTypes.gyro_angle_smooth.value:
            Values.gyro_angle_smooth = value.value
        elif value.valueType == ValueTypes.gyro_angle.value:
            Values.gyro_angle = value.value
    print(Values.gyro_angle)
    print(Values.ir_angle_smooth)
    print(Values.color)

