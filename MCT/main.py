from tkinter import *
from PIL import ImageTk
from PIL import Image
import time

window = Tk()  # Fenster wir erstellt


# Höhe und Breite des Fensters wird an den Monitor angepasst
w = int(window.winfo_screenwidth() / 2)
h = window.winfo_screenheight()

# Konfiguriert Bild Adresse
ImgFile = ['C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor1.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor2.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor3.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor4.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor5.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor6.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor7.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor8.gif',
           'C:\\Users\Kevin\Desktop\MCT\PuttyAPI.gif\IRsensor9.gif']

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


def ir_sensor_update():  # lässt die verschiedenen Bilder von Ir-Sensor rückwärts und dann vorwärts laufen

    # definiert alle Varialen als global
    global IrImg
    global ImgLabel
    global ImgNumber
    global IrDirection
    global tkimage

    # checkt ob Lauflicht am Ende ist und sagt wohin das Lauflicht soll
    if ImgNumber == 0:
        IrDirection = "up"
    elif ImgNumber == 8:
        IrDirection = "down"

    # lässt Lauflicht in eine Richtung laufen
    if IrDirection == "up":
        ImgNumber = ImgNumber + 1
    elif IrDirection == "down":
        ImgNumber = ImgNumber - 1

    # updatet Bild
    IrImg = Image.open(ImgFile[ImgNumber])
    tkimage = ImageTk.PhotoImage(IrImg.resize((IrImgWidth, IrImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    ImgLabel.config(image=tkimage, borderwidth=0)


while True:
    ir_sensor_update()
    window.update_idletasks()
    window.update()
    time.sleep(0.2)
