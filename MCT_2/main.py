from Utility import *
import time
from random import *
from SSH_Utility import ValueTypes
from SSH_Data import decode_input
import paramiko

device_name = '192.168.0.1'
username = 'robot'
password = 'maker'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ## to avoid missing_host_key error
try:
    ssh.connect(device_name, username=username, password=password, allow_agent=False, look_for_keys=False)
except TimeoutError:
    print("EV3 ist nicht verbunden!")
    exit()

channel = ssh.invoke_shell()

stdin, stdout, stderr = ssh.exec_command("python3 Main.py",  get_pty=True)
stdin.close()

for line in iter(lambda: stdout.readline(2048), ""):
    #i = int(line)
    print(line)

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
