from Window import *
from time import sleep
wind = MCTWindow()
wind.ir_sensor_update(7,7,7,7,7,7)
wind.console_print("Test")
wind.gyro_sensor_update(5, 7)
wind.color_sensor_update(50, "Brown", 20)
wind.motor_update(10,20,30,40)


while True:
    wind.window.update()
    wind.window.update_idletasks()
