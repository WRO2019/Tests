from tkinter import *
from PIL import ImageTk
from PIL import Image

window = Tk()  # Fenster wir erstellt


# Höhe und Breite des Fensters wird an den Monitor angepasst
w = int(window.winfo_screenwidth() / 2)
h = window.winfo_screenheight()


# Konfiguriert Bild Adresse
ir_ImgFile = ['C:\\Users\Kevin\Desktop\MCT\images\IRsensor1.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor2.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor3.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor4.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor5.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor6.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor7.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor8.gif',
              'C:\\Users\Kevin\Desktop\MCT\images\IRsensor9.gif']

color_ImgFile = "C:\\Users\Kevin\Desktop\MCT\images\Farbsensor.gif"

gyro_ImgFile = "C:\\Users\Kevin\Desktop\MCT\images\Gyrosensor.gif"

robot_ImgFile = "C:\\Users\Kevin\Desktop\MCT\images\Roboter.gif"


# rechnet Bild-Größen im richtigen Verhältniss um
ir_ImgWidth = 620
ir_ImgHeight = int((ir_ImgWidth / 1520) * 1280)
ir_ImgX = 430
ir_ImgY = 10

color_ImgWidth = 400
color_ImgHeight = int((color_ImgWidth / 1248) * 642)
color_ImgX = 50
color_ImgY = 570

gyro_ImgWidth = 328
gyro_ImgHeight = int((gyro_ImgWidth / 1024) * 640)
gyro_ImgX = 530
gyro_ImgY = 570

robot_ImgWidth = 500
robot_ImgHeight = robot_ImgWidth
robot_ImgX = 0
robot_ImgY = 30


# Foto Widget wird erstellt
ir_ImgLabel = Label()
ir_ImgLabel.place(x=ir_ImgX, y=ir_ImgY)

color_ImgLabel = Label()
color_ImgLabel.place(x=color_ImgX, y=color_ImgY)

gyro_ImgLabel = Label()
gyro_ImgLabel.place(x=gyro_ImgX, y=gyro_ImgY)

robot_ImgLabel = Label()
robot_ImgLabel.place(x=robot_ImgX, y=robot_ImgY)


# Text Labels werden erstellt und konfiguriert
ir_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_3_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_4_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_5_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_5_Label.place(x=ir_ImgX + 343, y=ir_ImgY + 100)
ir_4_Label.place(x=ir_ImgX + 230, y=ir_ImgY + 155 - 20)
ir_3_Label.place(x=ir_ImgX + 190, y=ir_ImgY + 240)
ir_2_Label.place(x=ir_ImgX + 220, y=ir_ImgY + 350)
ir_1_Label.place(x=ir_ImgX + 343, y=ir_ImgY + 380)

color_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
color_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 23))
color_1_Label.place(x=color_ImgX + 273, y=color_ImgY + 50)
color_2_Label.place(x=color_ImgX + 245, y=color_ImgY + 110)

gyro_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
gyro_1_Label.place(x=gyro_ImgX + 204, y=gyro_ImgY + 80)

robot_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_3_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_4_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_1_Label.place(x=robot_ImgX + 215, y=robot_ImgY - robot_ImgY)
robot_2_Label.place(x=robot_ImgX + 395, y=robot_ImgY + 360)
robot_3_Label.place(x=robot_ImgX + 215, y=robot_ImgY + 490)
robot_4_Label.place(x=robot_ImgX + 35, y=robot_ImgY + 360)


def ir_sensor_update(DC, AC):

    # definiert alle Varialen als global
    global ir_ImgLabel
    global ir_tkimage
    global ir_1_Label
    global ir_2_Label
    global ir_3_Label
    global ir_4_Label
    global ir_5_Label

    # updatet Text
    ir_1_Label.config(text='{:03d}'.format(AC[0]))
    ir_2_Label.config(text='{:03d}'.format(AC[1]))
    ir_3_Label.config(text='{:03d}'.format(AC[2]))
    ir_4_Label.config(text='{:03d}'.format(AC[3]))
    ir_5_Label.config(text='{:03d}'.format(AC[4]))

    # updatet Bild
    ir_img = Image.open(ir_ImgFile[DC - 1])
    ir_tkimage = ImageTk.PhotoImage(ir_img.resize((ir_ImgWidth, ir_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    ir_ImgLabel.config(image=ir_tkimage, borderwidth=0)


def color_sensor_update(brightness, color):
    global color_ImgFile
    global color_tkimage

    color_1_Label.config(text='{}{:03d}'.format("B:", brightness))
    color_2_Label.config(text='{:^8s}'.format("C:" + color))

    color_img = Image.open(color_ImgFile)
    color_tkimage = ImageTk.PhotoImage(color_img.resize((color_ImgWidth, color_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    color_ImgLabel.config(image=color_tkimage, borderwidth=0)


def gyro_sensor_update(value):
    global gyro_ImgFile
    global gyro_tkimage

    gyro_1_Label.config(text='{:>4}'.format('{:03d}'.format(value)))

    gyro_img = Image.open(gyro_ImgFile)
    gyro_tkimage = ImageTk.PhotoImage(gyro_img.resize((gyro_ImgWidth, gyro_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    gyro_ImgLabel.config(image=gyro_tkimage, borderwidth=0)


def motor_update(value1, value2, value3, value4):
    global robot_ImgFile
    global robot_tkimage

    robot_1_Label.config(text='{:03d}'.format(value1) + "%")
    robot_2_Label.config(text='{:03d}'.format(value2) + "%")
    robot_3_Label.config(text='{:03d}'.format(value3) + "%")
    robot_4_Label.config(text='{:03d}'.format(value4) + "%")

    robot_img = Image.open(robot_ImgFile)
    robot_tkimage = ImageTk.PhotoImage(robot_img.resize((robot_ImgWidth, robot_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    robot_ImgLabel.config(image=robot_tkimage, borderwidth=0)


# Fenster wird Konfiguriert
window.title("MCT - Misson Contoll Terminal")
window.geometry('%dx%d+%d+%d' % (w, h, -7, 0))
window.configure(background='black')
