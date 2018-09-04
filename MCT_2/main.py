from Utility import *
import time
from random import *

color = ["none", "black", "blue", "green", "yellow", "red", "white", "brown"]

code = ["File CUsers\Kevin\Documents\GitHub\Tests\MCTUtility.py, line 1",
        "ir_1_Label.config(text='{:03d}'.format(signal_strenght_raw[0th",
        "File CUsers\Kevin\AppData\Local\Programs\Python\Python36\lib\t",
        "return self._configure('configure', cnf, kw)                  ",
        "File CUsers\Kevin\AppData\Local\Programs\Python\Python36\lib\t",
        "self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))   ",
        "_tkinter.TclError: invalid command name .!label6              "]

while True:
    ir_sensor_update(randint(0, 9), [randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999)], [uniform(0, 999), uniform(0, 999), uniform(0, 999), uniform(0, 999), uniform(0, 999)])
    color_sensor_update(randint(0, 100), uniform(0, 100), color[randint(0, 7)])
    gyro_sensor_update(randint(-360, 360), uniform(-360, 360))
    motor_update(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    console_print(code[randint(0, 6)])

    window.update_idletasks()
    window.update()
    time.sleep(0.2)
