from tkinter import *
from PIL import ImageTk
from PIL import Image
import getpass

window = Tk()  # Fenster wir erstellt


# Höhe und Breite des Fensters wird an den Monitor angepasst
w = int(window.winfo_screenwidth() / 2)
h = window.winfo_screenheight()

userName = getpass.getuser()

# Konfiguriert Bild Adresse
ir_ImgFile = [f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor0.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor1.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor2.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor3.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor4.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor5.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor6.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor7.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor8.gif',
              f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor9.gif']

color_ImgFile = f"C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\Farbsensor.gif"

gyro_ImgFile = f"C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\Gyrosensor.gif"

robot_ImgFile = f"C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\Roboter.gif"

btn_ImgFile = f"C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\Button.gif"

console_ImgFile = f"C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\Console.gif"
console_Img = PhotoImage(file=console_ImgFile)

raw = True

resolution = window.winfo_screenheight() / 1080

line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""

# rechnet Bild-Größen im richtigen Verhältniss um
ir_ImgWidth = int(620 * resolution)
ir_ImgHeight = int((ir_ImgWidth / 1520) * 1280)
ir_ImgX = int(430 * resolution)
ir_ImgY = int(10 * resolution)

color_ImgWidth = int(400 * resolution)
color_ImgHeight = int((color_ImgWidth / 1248) * 642)
color_ImgX = int(50 * resolution)
color_ImgY = int(570 * resolution)

gyro_ImgWidth = int(328 * resolution)
gyro_ImgHeight = int((gyro_ImgWidth / 1024) * 640)
gyro_ImgX = int(530 * resolution)
gyro_ImgY = int(570 * resolution)

robot_ImgWidth = int(500 * resolution)
robot_ImgHeight = robot_ImgWidth
robot_ImgX = int(0 * resolution)
robot_ImgY = int(30 * resolution)

console_ImgX = int(22 * resolution)
console_ImgY = int(895 * resolution)


# Foto Widget wird erstellt
ir_ImgLabel = Label()
ir_ImgLabel.place(x=ir_ImgX, y=ir_ImgY)

color_ImgLabel = Label()
color_ImgLabel.place(x=color_ImgX, y=color_ImgY)

gyro_ImgLabel = Label()
gyro_ImgLabel.place(x=gyro_ImgX, y=gyro_ImgY)

robot_ImgLabel = Label()
robot_ImgLabel.place(x=robot_ImgX, y=robot_ImgY)

console_ImgLabel = Label(image=console_Img, bd=0)
console_ImgLabel.place(x=console_ImgX, y=console_ImgY)


# Text Labels werden erstellt und konfiguriert
ir_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_3_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_4_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_5_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
ir_5_Label.place(x=int(ir_ImgX + 343 * resolution), y=int(ir_ImgY + 100 * resolution))
ir_4_Label.place(x=int(ir_ImgX + 230 * resolution), y=int(ir_ImgY + 135 * resolution))
ir_3_Label.place(x=int(ir_ImgX + 190 * resolution), y=int(ir_ImgY + 240 * resolution))
ir_2_Label.place(x=int(ir_ImgX + 220 * resolution), y=int(ir_ImgY + 350 * resolution))
ir_1_Label.place(x=int(ir_ImgX + 343 * resolution), y=int(ir_ImgY + 380 * resolution))

color_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
color_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 23))
color_1_Label.place(x=int(color_ImgX + 273 * resolution), y=int(color_ImgY + 50 * resolution))
color_2_Label.place(x=int(color_ImgX + 245 * resolution), y=int(color_ImgY + 110 * resolution))

gyro_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
gyro_1_Label.place(x=int(gyro_ImgX + 204 * resolution), y=int(gyro_ImgY + 80 * resolution))

robot_1_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_2_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_3_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_4_Label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
robot_1_Label.place(x=int(robot_ImgX + 215 * resolution), y=0)                                                  # vielleicht y = 0 falsch positioniert!
robot_2_Label.place(x=int(robot_ImgX + 395 * resolution), y=int(robot_ImgY + 360 * resolution))
robot_3_Label.place(x=int(robot_ImgX + 215 * resolution), y=int(robot_ImgY + 490 * resolution))
robot_4_Label.place(x=int(robot_ImgX + 35 * resolution), y=int(robot_ImgY + 360 * resolution))

console_1_Label = Label(borderwidth=0, bg="black", fg="green")
console_1_Label.config(text="", font=("Consolas", 12), anchor=W, justify=LEFT)
console_1_Label.place(x=int(console_ImgX + 10 * resolution), y=int(console_ImgY + 8 * resolution))


def ir_sensor_update(direction, signal_strenght_raw, signal_strenght_smooth):

    # definiert alle Varialen als global
    global ir_ImgLabel
    global ir_tkimage
    global ir_1_Label
    global ir_2_Label
    global ir_3_Label
    global ir_4_Label
    global ir_5_Label
    global raw

    # updatet Text

    if raw:
        ir_1_Label.config(text='{:03d}'.format(signal_strenght_raw[0]))
        ir_2_Label.config(text='{:03d}'.format(signal_strenght_raw[1]))
        ir_3_Label.config(text='{:03d}'.format(signal_strenght_raw[2]))
        ir_4_Label.config(text='{:03d}'.format(signal_strenght_raw[3]))
        ir_5_Label.config(text='{:03d}'.format(signal_strenght_raw[4]))

        ir_5_Label.place(x=int(ir_ImgX + 343 * resolution), y=int(ir_ImgY + 100 * resolution))
        ir_4_Label.place(x=int(ir_ImgX + 230 * resolution), y=int(ir_ImgY + 135 * resolution))
        ir_3_Label.place(x=int(ir_ImgX + 190 * resolution), y=int(ir_ImgY + 240 * resolution))
        ir_2_Label.place(x=int(ir_ImgX + 220 * resolution), y=int(ir_ImgY + 350 * resolution))
        ir_1_Label.place(x=int(ir_ImgX + 343 * resolution), y=int(ir_ImgY + 380 * resolution))

    else:
        ir_1_Label.config(text='{0:.2f}'.format(signal_strenght_smooth[0]))
        ir_2_Label.config(text='{0:.2f}'.format(signal_strenght_smooth[1]))
        ir_3_Label.config(text='{0:.2f}'.format(signal_strenght_smooth[2]))
        ir_4_Label.config(text='{0:.2f}'.format(signal_strenght_smooth[3]))
        ir_5_Label.config(text='{0:.2f}'.format(signal_strenght_smooth[4]))

        ir_5_Label.place(x=int(ir_ImgX + 313 * resolution), y=int(ir_ImgY + 80 * resolution))
        ir_4_Label.place(x=int(ir_ImgX + 195 * resolution), y=int(ir_ImgY + 135 * resolution))
        ir_3_Label.place(x=int(ir_ImgX + 160 * resolution), y=int(ir_ImgY + 240 * resolution))
        ir_2_Label.place(x=int(ir_ImgX + 195 * resolution), y=int(ir_ImgY + 350 * resolution))
        ir_1_Label.place(x=int(ir_ImgX + 313 * resolution), y=int(ir_ImgY + 400 * resolution))

    # updatet Bild
    ir_img = Image.open(ir_ImgFile[direction])
    ir_tkimage = ImageTk.PhotoImage(ir_img.resize((ir_ImgWidth, ir_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    ir_ImgLabel.config(image=ir_tkimage, borderwidth=0)


def color_sensor_update(brightness_raw, brightness_smooth, color):
    global color_ImgFile
    global color_tkimage

    if raw:
        color_1_Label.config(text='{}{:03d}'.format("B:", brightness_raw))
        color_1_Label.place(x=int(color_ImgX + 273 * resolution), y=int(color_ImgY + 50 * resolution))
    else:
        color_1_Label.config(text="B:" + '{0:.2f}'.format(brightness_smooth))
        color_1_Label.place(x=int(color_ImgX + 240 * resolution), y=int(color_ImgY + 50 * resolution))

    color_2_Label.config(text='{:^8s}'.format("C:" + color))

    color_img = Image.open(color_ImgFile)
    color_tkimage = ImageTk.PhotoImage(color_img.resize((color_ImgWidth, color_ImgHeight)))  # verkleinert das Bild (PIL Library benötigt)
    color_ImgLabel.config(image=color_tkimage, borderwidth=0)


def gyro_sensor_update(value_raw, value_smooth):
    global gyro_ImgFile
    global gyro_tkimage

    if raw:
        gyro_1_Label.config(text='{:>4}'.format('{:03d}'.format(value_raw)))
        gyro_1_Label.place(x=int(gyro_ImgX + 204 * resolution), y=int(gyro_ImgY + 80 * resolution))
    else:
        gyro_1_Label.config(text='{:>6}'.format('{0:.2f}'.format(value_smooth)))
        gyro_1_Label.place(x=int(gyro_ImgX + 180 * resolution), y=int(gyro_ImgY + 80 * resolution))

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


def console_print(string):
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6

    if line6 == "":
        if line1 == "":
            line1 = string
        elif line2 == "":
            line2 = string
        elif line3 == "":
            line3 = string
        elif line4 == "":
            line4 = string
        elif line5 == "":
            line5 = string
        else:
            line6 = string
    else:
        line1 = line2
        line2 = line3
        line3 = line4
        line4 = line5
        line5 = line6
        line6 = string

    console_1_Label.config(text="{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(line1, line2, line3, line4, line5, line6))


def start_programm():
    print("started Programm!")


def stop_programm():
    print("stoped Programm!")


def upload_programm():
    print("uploaded Programm!")


def state_raw():
    global raw

    raw = True


def state_smooth():
    global raw

    raw = False


# Fenster wird konfiguriert
window.title("MCT - Misson Contoll Terminal")
window.geometry('%dx%d+%d+%d' % (w, h, -7, 0))
window.configure(background='black')


# Buttons werden konfiguriert

btn_ImgHeight = 50
btn_ImgWidth = 200

btn_Img = Image.open(btn_ImgFile)                                                          # btn Imge wird resized
btn_tkimage = ImageTk.PhotoImage(btn_Img.resize((int(btn_ImgWidth * resolution), int(btn_ImgHeight * resolution))))

start_btn = Button(window, text="START", command=start_programm, bg="black", fg="green", activebackground="black", activeforeground="green", bd=0, font=("Consolas", 25), image=btn_tkimage, compound=CENTER)
stop_btn = Button(window, text="STOP", command=stop_programm, bg="black", fg="green", activebackground="black", activeforeground="green", bd=0, font=("Consolas", 25), image=btn_tkimage, compound=CENTER)
upload_btn = Button(window, text="UPLOAD", command=upload_programm, bg="black", fg="green", activebackground="black", activeforeground="green", bd=0, font=("Consolas", 25), image=btn_tkimage, compound=CENTER)
raw_btn = Radiobutton(window, text="RAW DATA", value=1, bg="black", fg="green", font=("Consolas", 15), activebackground="black", activeforeground="green", selectcolor="black", command=state_raw)
smooth_btn = Radiobutton(window, text="SMOOTHED DATA", value=2, bg="black", fg="green", font=("Consolas", 15), activebackground="black", activeforeground="green", selectcolor="black", command=state_smooth)

raw_btn.select()
smooth_btn.deselect()

start_btn.place(x=int(20 * resolution), y=int(820 * resolution))
stop_btn.place(x=int(260 * resolution), y=int(820 * resolution))
upload_btn.place(x=int(500 * resolution), y=int(820 * resolution))
raw_btn.place(x=int(730 * resolution), y=int(815 * resolution))
smooth_btn.place(x=int(730 * resolution), y=int(845 * resolution))
