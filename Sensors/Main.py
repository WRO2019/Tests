from time import sleep
from Sensors import Sensor
import Utility

# def __init__(self, port, mode, sensor_type):
# def start_reading_threads(self, value_type, threads, messwerte, pause)
ir_seeker = Sensor(Utility.Ports.in1, 'AC-ALL', Utility.SensorTypes.ir_sensor)
ir_seeker.start_reading_threads(Sensor.ValueTypes.ir_distance_smooth, 2, 5, 0.2)
while True:
    print(str(ir_seeker.get_value(Utility.ValueTypes.ir_distance_smooth)))
    sleep(0.5)
