from Window import *

wind = MCTWindow()
wind.ir_sensor_update(7,7,7,7,7,7)
wind.console_print("Test")
wind.gyro_sensor_update(5, 7)
wind.color_sensor_update(50, "Brown", 20)
<<<<<<< HEAD

wind.motor_update(10, 20, 30, 40)
wind.motor_update(10,20,30,40)
wind.ultrasonic_sensor_update(20)

=======
wind.motor_update(10, 20, 30, 40)
wind.ultrasonic_sensor_update(20)
>>>>>>> 8f4c9165db85ca408c022ddcfffc431cc8033d4e


while True:
    wind.window.update()
    wind.window.update_idletasks()
