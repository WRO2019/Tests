from time import sleep
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

