from tkinter import *

w = 1000
h = 600
btnX = 0
btnY = 0

fenster = Tk()

def center_window(width=w, height=h):
    # get screen width and height
    screen_width = fenster.winfo_screenwidth()
    screen_height = fenster.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    fenster.geometry('%dx%d+%d+%d' % (width, height, x, y))

BtnImg = PhotoImage(file='C:\\Users\Kevin\Pictures\security.gif')
lImg = PhotoImage(file='C:\\Users\Kevin\Pictures\schwarz.gif')

fenster.title("Mein erstes PROGRAMM!!!")
fenster.geometry('{}x{}'.format(w, h))
fenster.configure(background='black')
fenster.resizable(width=True, height=True)

button = Button(fenster, text="Klick mich!")

def btnUp():
    global btnY
    btnY = btnY - 1
    button.place(x=btnX, y=btnY)
    ylabel.configure(text="Y:" + str(btnY))

def btnDown():
    global btnY
    btnY = btnY + 1
    button.place(x=btnX, y=btnY)
    ylabel.configure(text="Y:" + str(btnY))

def btnRigth():
    global btnX
    btnX = btnX + 1
    button.place(x=btnX, y=btnY)
    xlabel.configure(text="X:"+str(btnX))

def btnLeft():
    global btnX
    btnX = btnX - 1
    button.place(x=btnX, y=btnY)
    xlabel.configure(text="X:" + str(btnX))


btnUp = Button(fenster, text="A", command=btnUp)
btnDown = Button(fenster, text="V", command=btnDown)
btnRight = Button(fenster, text=">", command=btnRigth)
btnLeft = Button(fenster, text="<", command=btnLeft)

btnUp.place(x=900, y=500)
btnDown.place(x=900, y=550)
btnRight.place(x=950, y=550)
btnLeft.place(x=850, y=550)

xlabel = Label(fenster, text="X:"+str(btnX))
xlabel.pack(side=BOTTOM)
ylabel = Label(fenster, text="Y:"+str(btnY))
ylabel.pack(side=BOTTOM)

eingabe = Entry(fenster, width=40, bg="black", fg="green", bd=5)
eingabe.place(x=10, y=20)




def btnPlace():
    i = int(eingabe.get())
    button.place(x=i, y=20)

button.configure(bg="black", fg="green", bd=0, activebackground="black", activeforeground="green", image=BtnImg, command=btnPlace)
button.place(x=0, y=0)

center_window()

mainloop()

