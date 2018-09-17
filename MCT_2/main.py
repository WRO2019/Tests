from Utility import *
import time
from random import *
from SSH_Data import decode_input
import paramiko
import threading

device_name = '192.168.0.1'
username = 'robot'
password = 'maker'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  ## to avoid missing_host_key error
try:
    ssh.connect(device_name, username=username, password=password, allow_agent=False, look_for_keys=False)
except TimeoutError:
    print("EV3 ist nicht verbunden!")
    exit()

channel = ssh.invoke_shell()

stdin, stdout, stderr = ssh.exec_command("python3 Main.py", get_pty=True)
stdin.close()


def readingSSH():
    for line in iter(lambda: stdout.readline(2048), ""):
        if line is not None:
            motor_update(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
            decode_input(str(line))
            window.update_idletasks()
            window.update()


ssh_thread = threading.Thread(target=readingSSH(), args=())
ssh_thread.start()
