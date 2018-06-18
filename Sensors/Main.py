import Sensors
import Utility
import logging
from time import sleep
# def __init__(self, port, mode=None, sensor_type=None, ir_directions=None):
# def start_reading_threads(self, value_type, threads, messwerte, pause)
ir_seeker = Sensors.Sensors(Sensors.Ports.in1, 'AC-ALL', Sensors.SensorTypes.ir_sensor, Utility.directions)
ir_seeker.start_reading_threads(Sensors.ValueTypes.ir_distance_smooth, 2, 5, 0.2)
while True:
    print(str(ir_seeker.get_value(Sensors.ValueTypes.ir_distance_smooth)))
    sleep(0.5)
