from Graphics import button
from Graphics import ylabel
from Graphics import xlabel


def btnUp():
    global btnY
    btnY = btnY - 1
    button.place(x=btnX, y=btnY)
    ylabel.configure(text="Y:" + str(btnY))


##################################################################

def btnDown():
    global btnY
    btnY = btnY + 1
    button.place(x=btnX, y=btnY)
    ylabel.configure(text="Y:" + str(btnY))


def btnRigth():
    global btnX
    btnX = btnX + 1
    button.place(x=btnX, y=btnY)
    xlabel.configure(text="X:" + str(btnX))


##################################################################

def btnLeft():
    global btnX
    btnX = btnX - 1
    button.place(x=btnX, y=btnY)
    xlabel.configure(text="X:" + str(btnX))


##################################################################

def btnPlace():
    i = int(eingabe.get())
    button.place(x=i, y=20)
