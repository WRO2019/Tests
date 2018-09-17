from ev3dev.ev3 import *

#####################################################
mA = Motor("outA")  # Motors   # Links
mB = Motor("outB")  # Rechts
mC = Motor("outD")  # Hinten
mD = Motor("outC")  # Vorne


######################################################

def winkel_form(winkel):
    # positive Werte
    # Winkel des Dreicks wird aus Richtung errechnet
    if 0 < winkel < 45:
        return 45 - winkel
    elif 45 < winkel < 90:
        return winkel - 45
    elif 90 < winkel < 135:
        return 135 - winkel
    elif 135 < winkel < 180:
        return winkel - 135
    elif 180 < winkel < 225:
        return 225 - winkel
    elif 225 < winkel < 270:
        return winkel - 225
    elif 270 < winkel < 315:
        return 315 - winkel
    elif 315 < winkel < 360:
        return winkel - 315

    ######################################################
    # negative Werte
    elif 0 > winkel > -45:
        return -45 - winkel
    elif -45 > winkel > -90:
        return winkel + 45
    elif -90 > winkel > -135:
        return -135 - winkel
    elif -135 > winkel > -180:
        return winkel + 135
    elif -180 > winkel > -225:
        return -225 - winkel
    elif -225 > winkel > -270:
        return winkel + 225
    elif -270 > winkel > -315:
        return -315 - winkel
    elif -315 > winkel > -360:
        return winkel + 315


######################################################

def isEqualTo(wert, werte):
    for i in werte:
        if i == wert:
            return True
            break
    return False
