from Utility import *
import time
from random import randint

color = ["none", "black", "blue", "green", "yellow", "red", "white", "brown"]

while True:
    ir_sensor_update(randint(1, 9), [randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999)])
    color_sensor_update(randint(0, 100), color[randint(0, 7)])
    gyro_sensor_update(randint(-360, 360))
    motor_update(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

    window.update_idletasks()
    window.update()
    time.sleep(0.2)
