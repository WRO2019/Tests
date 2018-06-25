from Sensors import Sensor
from time import sleep
# def __init__(self, port, mode=None, sensor_type=None, ir_directions=None):
# def start_reading_threads(self, value_type, threads, messwerte, pause)
ir_seeker = Sensor.Sensor(Sensor.Ports.in1, 'AC-ALL', Sensor.SensorTypes.ir_sensor)
ir_seeker.start_reading_threads(Sensor.ValueTypes.ir_distance_smooth, 2, 5, 0.2)
while True:
    print(str(ir_seeker.get_value(Sensor.ValueTypes.ir_distance_smooth)))
    sleep(0.5)
