from Utility import *
import time
from random import *
from SSH_Utility import ValueTypes
from SSH_Data import decode_input
color = ["none", "black", "blue", "green", "yellow", "red", "white", "brown"]

code = ["File CUsers\Kevin\Documents\GitHub\Tests\MCTUtility.py, line 1",
        "ir_1_Label.config(text='{:03d}'.format(signal_strenght_raw[0th",
        "File CUsers\Kevin\AppData\Local\Programs\Python\Python36\lib\t",
        "return self._configure('configure', cnf, kw)                  ",
        "File CUsers\Kevin\AppData\Local\Programs\Python\Python36\lib\t",
        "self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))   ",
        "_tkinter.TclError: invalid command name .!label6              "]


def get_prepared_value(valueType):
    return valueType + ":" + str(randint(0, 9)) + ";"


def get_code():
    ###############################################################################
    # Werte wegschicken

    output = "datas:"
    output += get_prepared_value(ValueTypes.gyro_angle.value)
    output += get_prepared_value(ValueTypes.gyro_angle_smooth.value)
    #################################
    output += get_prepared_value(ValueTypes.ir_direction.value)
    output += get_prepared_value(ValueTypes.ir_direction_smooth.value)
    output += get_prepared_value(ValueTypes.ir_angle.value)
    output += get_prepared_value(ValueTypes.ir_angle_smooth.value)
    output += get_prepared_value(ValueTypes.ir_distance.value)
    output += get_prepared_value(ValueTypes.ir_distance_smooth.value)
    #################################
    output += get_prepared_value(ValueTypes.color.value)
    output += get_prepared_value(ValueTypes.reflect.value)
    output += get_prepared_value(ValueTypes.ambiente.value)
    return output

while True:
    motor_update(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    decode_input(get_code())

    window.update_idletasks()
    window.update()
    time.sleep(2)
