from time import sleep
from Sensors import *
from Utility import *

# Sensoren erstellen(Port, Mode)
ir_seeker = Ir_Seeker(Ports.in1)
color_sensor = Color_Sensor(Ports.in2)
gyro_sensor = Gyro_Sensor(Ports.in3)
ultrasonic_sensor = Ultrasonic_Sensor(Ports.in4)

ir_seeker.start_ir_direction_smooth()
ir_seeker.start_ir_distance_smooth()
gyro_sensor.start_gyro_angel_smooth()

while True:
    print("Ir Distance:")
    print(ir_seeker.get_value(ValueTypes.ir_distance_smooth))
    print(ir_seeker.get_value(ValueTypes.ir_distance))
    print("Ir Angel")
    print(ir_seeker.get_value(ValueTypes.ir_angle_smooth))
    print(ir_seeker.get_value(ValueTypes.ir_angle))
    print("Ir Direction")
    print(ir_seeker.get_value(ValueTypes.ir_direction_smooth))
    print(ir_seeker.get_value(ValueTypes.ir_direction))
    print("Color Sensor")
    print(color_sensor.get_value(ValueTypes.color))
    print(color_sensor.get_value(ValueTypes.ambiente))
    print(color_sensor.get_value(ValueTypes.reflect))
    print("gyro")
    print(gyro_sensor.get_value(ValueTypes.gyro_angle_smooth))
    print(gyro_sensor.get_value(ValueTypes.gyro_angle))
    print("Ultraschall")
    print(ultrasonic_sensor.get_value(ValueTypes.ultrasonic_distance))
    print("------------------------------------")
    sleep(5)
