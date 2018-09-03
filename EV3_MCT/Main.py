from Sensors import *
from Utility import *

ir_seeker = Sensor(Ports.in1, SensorModes.ir_gefilter)
gyro_sensor = Sensor(Ports.in2, None)
color_sensor = Sensor(Ports.in3, None)

gyro_sensor.start_reading_threads(ValueTypes.gyro_angle_smooth, 2, 5, 0.1)
ir_seeker.start_reading_threads(ValueTypes.ir_direction_smooth, 2, 5, 0.1)
ir_seeker.start_reading_threads(ValueTypes.ir_angle_smooth, 2, 5, 0.1)

def get_prepared_value(sensor, valueType):
    return valueType + ":" + sensor.get_value(valueType) + ";"

###############################################################################
# Werte wegschicken

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

print(output)

