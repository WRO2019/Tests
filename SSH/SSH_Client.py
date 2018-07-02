from time import sleep

import SSH_Utility
import paramiko


device_name = '192.168.0.1'
username = 'robot'
password = 'maker'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ## to avoid missing_host_key error
ssh.connect(device_name, username=username, password=password, allow_agent=False, look_for_keys=False)

channel = ssh.invoke_shell()


stdin, stdout, stderr = ssh.exec_command("python3 SSH_EV3.py",  get_pty=True)
stdin.close()
while True:
    for line in stdout.read().splitlines():
        print(line)
