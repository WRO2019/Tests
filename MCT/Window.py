from tkinter import *
from PIL import ImageTk
from PIL import Image
import getpass

# Bild Adresse
userName = getpass.getuser()
ir_ImgFiles = [f'C:\\Users\{userName}\Documents\GitHub\Tests\MCT\images\IRsensor0.gif',
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


class MCTWindow:
    window = Tk()  # Fenster wir erstellt
    __isModeRaw = True
    __ir_distance_label = Label()
    __ir_angle_label = Label()
    __color_a_label = Label()
    __color_c_label = Label()
    __gyro_label = Label()
    __robot_1_label = Label()
    __robot_2_label = Label()
    __robot_3_label = Label()
    __robot_4_label = Label()
    __console_label = Label()

    __ir_image = Label()
    __color_image = Label()
    __gyro_image = Label()
    __robot_image = Label()
    __console_image = Label()

    def __init__(self):
        self.window.title("MCT - Misson Contoll Terminal")
        self.window.geometry(
            '%dx%d+%d+%d' % (int(self.window.winfo_screenwidth() / 2), self.window.winfo_screenheight(), -7, 0))
        self.window.configure(background='black')
        self.__resolution = self.window.winfo_screenheight() / 1080
        self.__ir_img_x = int(430 * self.__resolution)
        self.__ir_img_y = int(10 * self.__resolution)
        self.__color_img_x = int(50 * self.__resolution)
        self.__color_img_y = int(570 * self.__resolution)
        self.__gyro_img_x = int(530 * self.__resolution)
        self.__gyro_img_y = int(570 * self.__resolution)
        self.__robot_img_x = int(0)
        self.__robot_img_y = int(30 * self.__resolution)
        self.__console_img_x = int(22 * self.__resolution)
        self.__console_img_y = int(896 * self.__resolution)

        self.__create_pictures()
        self.__create_labels()
        self.__create_buttons()
        self.window.update_idletasks()
        self.window.update()

    def __create_pictures(self):
        global color_tk_image
        global gyro_tk_image
        global ir_tk_image
        global robot_tk_image
        global console_img

        ir_img_width = int(620 * self.__resolution)
        ir_img_height = int((ir_img_width / 1520) * 1280)
        ir_tk_image = ImageTk.PhotoImage(
            Image.open(ir_ImgFiles[0]).resize((ir_img_width, ir_img_height)))
        self.__ir_image = Label(image=ir_tk_image, borderwidth=0)
        self.__ir_image.place(x=self.__ir_img_x, y=self.__ir_img_y)

        color_img_width = int(400 * self.__resolution)
        color_img_height = int((color_img_width / 1248) * 642)
        color_tk_image = ImageTk.PhotoImage(
            Image.open(color_ImgFile).resize((color_img_width, color_img_height)))
        self.__color_image = Label(image=color_tk_image, borderwidth=0)
        self.__color_image.place(x=self.__color_img_x, y=self.__color_img_y)

        gyro_img_width = int(328 * self.__resolution)
        gyro_img_height = int((gyro_img_width / 1024) * 640)
        gyro_tk_image = ImageTk.PhotoImage(
            Image.open(gyro_ImgFile).resize((gyro_img_width, gyro_img_height)))
        self.__gyro_image = Label(image=gyro_tk_image, borderwidth=0)
        self.__gyro_image.place(x=self.__gyro_img_x, y=self.__gyro_img_y)

        robot_img_width = int(500 * self.__resolution)
        robot_img_height = robot_img_width
        robot_tk_image = ImageTk.PhotoImage(
            Image.open(robot_ImgFile).resize((robot_img_width, robot_img_height)))
        self.__robot_image = Label(image=robot_tk_image, borderwidth=0)
        self.__robot_image.place(x=self.__robot_img_x, y=self.__robot_img_y)

        console_img = PhotoImage(file=console_ImgFile)
        self.__console_image = Label(image=console_img, borderwidth=0)
        self.__console_image.place(x=self.__console_img_x, y=self.__console_img_y)

    def __create_labels(self):
        self.__ir_distance_label = Label(background="black", borderwidth=0, fg="green", text="000",
                                         font=("Consolas", 25))
        self.__ir_angle_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__ir_distance_label.place(x=int(self.__ir_img_x + 343 * self.__resolution),
                                       y=int(self.__ir_img_y + 100 * self.__resolution))
        self.__ir_angle_label.place(x=int(self.__ir_img_x + 230 * self.__resolution),
                                    y=int(self.__ir_img_y + 135 * self.__resolution))

        self.__color_a_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__color_c_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 23))
        self.__color_r_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 23))
        self.__color_a_label.place(x=int(self.__color_img_x + 250 * self.__resolution),
                                   y=int(self.__color_img_y + 40 * self.__resolution))
        self.__color_c_label.place(x=int(self.__color_img_x + 250 * self.__resolution),
                                   y=int(self.__color_img_y + 90 * self.__resolution))
        self.__color_r_label.place(x=int(self.__color_img_x + 250 * self.__resolution),
                                   y=int(self.__color_img_y + 140 * self.__resolution))

        self.__gyro_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__gyro_label.place(x=int(self.__gyro_img_x + 204 * self.__resolution),
                                y=int(self.__gyro_img_y + 80 * self.__resolution))

        self.__robot_1_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__robot_2_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__robot_3_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__robot_4_label = Label(background="black", borderwidth=0, fg="green", text="000", font=("Consolas", 25))
        self.__robot_1_label.place(x=int(self.__robot_img_x + 215 * self.__resolution),
                                   y=0)  # vielleicht y = 0 falsch positioniert!
        self.__robot_2_label.place(x=int(self.__robot_img_x + 395 * self.__resolution),
                                   y=int(self.__robot_img_y + 360 * self.__resolution))
        self.__robot_3_label.place(x=int(self.__robot_img_x + 215 * self.__resolution),
                                   y=int(self.__robot_img_y + 490 * self.__resolution))
        self.__robot_4_label.place(x=int(self.__robot_img_x + 35 * self.__resolution),
                                   y=int(self.__robot_img_y + 360 * self.__resolution))

        self.__console_label = Label(borderwidth=0, bg="black", fg="green")
        self.__console_label.config(text="000", font=("Consolas", 12), anchor=W, justify=LEFT)
        self.__console_label.place(x=int(self.__console_img_x + 10 * self.__resolution),
                                   y=int(self.__console_img_y + 8 * self.__resolution))

    def __create_buttons(self):
        global start_btn
        global stop_btn
        global upload_btn
        global raw_btn
        global smooth_btn
        global btn_tk_image

        btn_img_height = 50
        btn_img_width = 200

        btn_tk_image = ImageTk.PhotoImage(
            Image.open(btn_ImgFile).resize((int(btn_img_width * self.__resolution), int(btn_img_height * self.__resolution))))

        start_btn = Button(self.window, text="START", command=self.__start_programm, bg="black", fg="green",
                           activebackground="black", activeforeground="green", bd=0, font=("Consolas", 25),
                           image=btn_tk_image, compound=CENTER)
        stop_btn = Button(self.window, text="STOP", command=self.__stop_programm, bg="black", fg="green",
                          activebackground="black",
                          activeforeground="green", bd=0, font=("Consolas", 25), image=btn_tk_image, compound=CENTER)
        upload_btn = Button(self.window, text="UPLOAD", command=self.__upload_programm, bg="black", fg="green",
                            activebackground="black", activeforeground="green", bd=0, font=("Consolas", 25),
                            image=btn_tk_image, compound=CENTER)
        raw_btn = Radiobutton(self.window, text="RAW DATA", value=1, bg="black", fg="green", font=("Consolas", 15),
                              activebackground="black", activeforeground="green", selectcolor="black",
                              command=self.__state_raw)
        smooth_btn = Radiobutton(self.window, text="SMOOTHED DATA", value=2, bg="black", fg="green",
                                 font=("Consolas", 15),
                                 activebackground="black", activeforeground="green", selectcolor="black",
                                 command=self.__state_smooth)

        raw_btn.select()
        smooth_btn.deselect()

        start_btn.place(x=int(20 * self.__resolution), y=int(820 * self.__resolution))
        stop_btn.place(x=int(260 * self.__resolution), y=int(820 * self.__resolution))
        upload_btn.place(x=int(500 * self.__resolution), y=int(820 * self.__resolution))
        raw_btn.place(x=int(730 * self.__resolution), y=int(815 * self.__resolution))
        smooth_btn.place(x=int(730 * self.__resolution), y=int(845 * self.__resolution))

    def ir_sensor_update(self, direction_raw, direction_smooth, angle_raw, angle_smooth, distance_raw,
                         distance_smooth):
        global ir_tk_image

        if self.__isModeRaw:
            self.__ir_distance_label.config(text="D:" + str(distance_raw))
            self.__ir_angle_label.config(text="A:" + str(angle_raw))

            if direction_raw in range(0, 9):
                ir_img_width = int(620 * self.__resolution)
                ir_img_height = int((ir_img_width / 1520) * 1280)
                ir_tk_image = ImageTk.PhotoImage(
                    Image.open(ir_ImgFiles[direction_raw]).resize(
                        (ir_img_width, ir_img_height)))
                self.__ir_image.config(image=ir_tk_image, borderwidth=0)

        else:
            self.__ir_distance_label.config(text="D:" + str(distance_smooth))
            self.__ir_angle_label.config(text="A:" + str(angle_smooth))

            if direction_smooth in range(0, 9):
                ir_img_width = int(620 * self.__resolution)
                ir_img_height = int((ir_img_width / 1520) * 1280)
                ir_tk_image = ImageTk.PhotoImage(
                    Image.open(ir_ImgFiles[int(direction_smooth)]).resize(
                        (ir_img_width, ir_img_height)))
                self.__ir_image.config(image=ir_tk_image, borderwidth=0)

        self.window.update_idletasks()
        self.window.update()

    def color_sensor_update(self, color, ambiente, reflect):
        self.__color_c_label.config(text="C: " + str(color))
        self.__color_a_label.config(text="A: " + str(ambiente))
        self.__color_r_label.config(text="R: " + str(reflect))
        self.window.update_idletasks()
        self.window.update()

    def gyro_sensor_update(self, value_raw, value_smooth):
        if self.__isModeRaw:
            self.__gyro_label.config(text=str(value_raw) + "°")
        else:
            self.__gyro_label.config(text=str(value_smooth) + "°")
        self.window.update_idletasks()
        self.window.update()

    def motor_update(self, value1, value2, value3, value4):
        self.__robot_1_label.config(text=str(value1))
        self.__robot_2_label.config(text=str(value2))
        self.__robot_3_label.config(text=str(value3))
        self.__robot_4_label.config(text=str(value4))
        self.window.update_idletasks()
        self.window.update()

    def console_print(self, string):
        self.__console_label.config(text=str(string))
        self.window.update_idletasks()
        self.window.update()

    def __start_programm(self):
        print("started Programm!")

    def __stop_programm(self):
        print("stoped Programm!")

    def __upload_programm(self):
        print("uploaded Programm!")

    def __state_raw(self):
        self.__isModeRaw = True
        self.window.update_idletasks()
        self.window.update()

    def __state_smooth(self):
        self.__isModeRaw = False
        self.window.update_idletasks()
        self.window.update()
