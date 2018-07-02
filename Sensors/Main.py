from time import sleep
from Sensors import Sensor
from Utility import *

# Sensoren erstellen(Port, Mode)
ir_seeker = Sensor(Ports.in1, 'AC-ALL')
color_sensor = Sensor(Ports.in2, SensorModes.color.value)
gyro_sensor = Sensor(Ports.in2, None)

# Threads starten für smooth(ValueType, Threads, Messwerte, Pause)
ir_seeker.start_reading_threads(ValueTypes.ir_direction_smooth, 2, 5, 0.2)
