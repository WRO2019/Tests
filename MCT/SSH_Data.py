from SSH_Utility import *


def decode_input(window, input):
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
                    value = int(float(value))
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
                window.color_sensor_update(Values.color, value.value, Values.reflect)

            elif value.valueType == ValueTypes.reflect.value:
                Values.reflect = value.value
                window.color_sensor_update(Values.color, Values.ambiente, value.value)

            elif value.valueType == ValueTypes.color.value:
                Values.color = value.value
                window.color_sensor_update(value.value, Values.ambiente, Values.reflect)
                ##
            elif value.valueType == ValueTypes.ir_distance_smooth.value:
                Values.ir_distance_smooth = value.value
                window.ir_sensor_update(Values.ir_direction, Values.ir_direction_smooth, Values.ir_angle,
                                        Values.ir_angle_smooth, Values.ir_distance, value.value)
            elif value.valueType == ValueTypes.ir_distance.value:
                Values.ir_distance = value.value
                window.ir_sensor_update(Values.ir_direction, Values.ir_direction_smooth, Values.ir_angle,
                                        Values.ir_angle_smooth, value.value, Values.ir_distance_smooth)
                ##
            elif value.valueType == ValueTypes.ir_angle_smooth.value:
                Values.ir_angle_smooth = value.value
                window.ir_sensor_update(Values.ir_direction, Values.ir_direction_smooth, Values.ir_angle,
                                        value.value, Values.ir_distance, Values.ir_distance_smooth)
            elif value.valueType == ValueTypes.ir_angle.value:
                Values.ir_angle = value.value
                window.ir_sensor_update(Values.ir_direction, Values.ir_direction_smooth, value.value,
                                        Values.ir_angle_smooth, Values.ir_distance, Values.ir_distance_smooth)
                ##
            elif value.valueType == ValueTypes.ir_direction_smooth.value:
                Values.ir_direction_smooth = value.value
                window.ir_sensor_update(Values.ir_direction, value.value, Values.ir_angle,
                                        Values.ir_angle_smooth, Values.ir_distance, Values.ir_distance_smooth)

            elif value.valueType == ValueTypes.ir_direction.value:
                Values.ir_direction = value.value
                window.ir_sensor_update(value.value, Values.ir_direction_smooth, Values.ir_angle,
                                        Values.ir_angle_smooth, Values.ir_distance, Values.ir_distance_smooth)
                ##
            elif value.valueType == ValueTypes.gyro_angle_smooth.value:
                Values.gyro_angle_smooth = value.value
                window.gyro_sensor_update(Values.gyro_angle, value.value)

            elif value.valueType == ValueTypes.gyro_angle.value:
                Values.gyro_angle = value.value
                window.gyro_sensor_update(value.value, Values.gyro_angle_smooth)
    else:
        window.console_print(input)
