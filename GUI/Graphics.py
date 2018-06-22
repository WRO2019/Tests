from tkinter import *
import Buttons

window_width = 1000
window_height = 600
btnX = 0
btnY = 0



##################################################################

def center_window(width=window_width, height=window_height):
    # get screen width and height
    screen_width = fenster.winfo_screenwidth()
    screen_height = fenster.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    fenster.geometry('%dx%d+%d+%d' % (width, height, x, y))

##################################################################


fenster = Tk()
BtnImg = PhotoImage(file='C:\\Users\Lukas\Desktop\LT_Logo.png')

fenster.title("Mein erstes PROGRAMM!!!")
fenster.geometry('{}x{}'.format(window_width, window_height))
fenster.configure(background='black')
fenster.resizable(width=True, height=True)

#############################
button = Button(fenster)
button.configure(bg="black", fg="green", bd=0, activebackground="black", activeforeground="green",
                 image=BtnImg, command=Buttons.btnPlace)
btnUp = Button(fenster, text="A", command=Buttons.btnUp)
btnDown = Button(fenster, text="V", command=Buttons.btnDown)
btnRight = Button(fenster, text=">", command=Buttons.btnRigth)
btnLeft = Button(fenster, text="<", command=Buttons.btnLeft)
btnUp.place(x=900, y=500)
btnDown.place(x=900, y=550)
btnRight.place(x=950, y=550)
btnLeft.place(x=850, y=550)
#############################

xlabel = Label(fenster, text="X:"+str(btnX))
xlabel.pack(side=BOTTOM)
ylabel = Label(fenster, text="Y:"+str(btnY))
ylabel.pack(side=BOTTOM)

eingabe = Entry(fenster, width=40, bg="black", fg="green", bd=5)
eingabe.place(x=10, y=20)


button.place(x=0, y=0)
center_window()
mainloop()
