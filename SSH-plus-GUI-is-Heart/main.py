from tkinter import *
from PIL import ImageTk
from PIL import Image
import time
import paramiko

window = Tk()  # Fenster wir erstellt


# Höhe und Breite des Fensters wird an den Monitor angepasst
w = int(window.winfo_screenwidth() / 2)
h = window.winfo_screenheight()

# Konfiguriert Bild Adresse
ImgFile = ['C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor0.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor1.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor2.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor3.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor4.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor5.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor6.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor7.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor8.gif',
           'C:\\Users\Roboscope\Documents\GitHub\Tests\MCT\PuttyAPI.gif\IRsensor9.gif']

ImgNumber = 3
IrDirection = "up"

# rechnet Bild-Größen im richtigen Verhältniss um
IrImgWidth = 700
IrImgHeight = int((IrImgWidth / 1520) * 1280)

# Fenster wird Konfiguriert
window.title("MCT - Misson Contoll Terminal")
window.geometry('%dx%d+%d+%d' % (w, h, -7, 0))
window.configure(background='black')

ImgLabel = Label()  # Foto Widget wird erstellt
ImgLabel.pack()



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

stdin, stdout, stderr = ssh.exec_command("python3 IR_test.py",  get_pty=True)
stdin.close()




def ir_sensor_update(ImgNumber):  # lässt die verschiedenen Bilder von Ir-Sensor rückwärts und dann vorwärts laufen

    # definiert alle Varialen als global
    global IrImg
    global ImgLabel
    global IrDirection
    global tkimage


    # updatet Bild
    IrImg = Image.open(ImgFile[ImgNumber])
    tkimage = ImageTk.PhotoImage(IrImg.resize((IrImgWidth, IrImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    ImgLabel.config(image=tkimage, borderwidth=0)


for line in iter(lambda: stdout.readline(2048), ""):
    i = int(line)
    ir_sensor_update(i)
    print(i)
    window.update_idletasks()
    window.update()
