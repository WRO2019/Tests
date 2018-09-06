from SSH_Utility import *
from Utility import *

def decode_input(input):
    if input[0:6] == "datas:":
        values_text = input[6:input.__len__()]
        values = []
        value_type = ""
        value = ""
        value_active = False
        for key in values_text:
            if value_active:  # Value
                if key != ";":
                    value += key
                else:
                    value = int(value)
                    values.append(Value(value, value_type, ))
                    value_active = False
                    value = ""
                    value_type = ""
            else:  # Value Type
                if key != ":":
                    value_type += key
                else:
                    if key == ":":
                        value_active = True
        # Werte zuweisen
        for value in values:
            if value.valueType == ValueTypes.ambiente.value:
                Values.ambiente = value.value

            elif value.valueType == ValueTypes.reflect.value:
                Values.reflect = value.value
                color_sensor_update(value.value, "--", Values.color)

            elif value.valueType == ValueTypes.color.value:
                Values.color = value.value
                color_sensor_update(Values.reflect, "--", value.value)
                ##
            elif value.valueType == ValueTypes.ir_distance_smooth.value:
                Values.ir_distance_smooth = value.value
                ir_sensor_update(Values.ir_direction, Values.ir_distance, value.value)

            elif value.valueType == ValueTypes.ir_distance.value:
                Values.ir_distance = value.value
                ir_sensor_update(value.value, Values.ir_distance, Values.ir_distance_smooth)
                ##
            elif value.valueType == ValueTypes.ir_angle_smooth.value:
                Values.ir_angle_smooth = value.value

            elif value.valueType == ValueTypes.ir_angle.value:
                Values.ir_angle = value.value
                ##
            elif value.valueType == ValueTypes.ir_direction_smooth.value:
                Values.ir_direction_smooth = value.value

            elif value.valueType == ValueTypes.ir_direction.value:
                Values.ir_direction = value.value
                ##
            elif value.valueType == ValueTypes.gyro_angle_smooth.value:
                Values.gyro_angle_smooth = value.value
                gyro_sensor_update(Values.gyro_angle, value.value)

            elif value.valueType == ValueTypes.gyro_angle.value:
                Values.gyro_angle = value.value
                gyro_sensor_update(value.value, Values.gyro_angle_smooth)
    else:
        console_print(input)
