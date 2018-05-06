from ev3dev.ev3 import *

#####################################################
mA = Motor("outA")  # Motors    # Links
mB = Motor("outB")  # Rechts
mC = Motor("outC")  # Hinten
mD = Motor("outD")  # Vorne


######################################################

def winkel_form(winkel):
    if winkel < 0:

        if winkel > -44:

            winkel_neu = 45 - abs(winkel)

            return winkel_neu

        elif winkel == 45:

            winkel_neu = 0

            return winkel_neu

        elif winkel < -45:

            winkel_neu = 90 - abs(winkel)

            return winkel_neu

    elif winkel >= 0:

        if winkel < 44:

            winkel_neu = 45 - abs(winkel)

            return winkel_neu

        elif winkel == 45:

            winkel_neu = 0

            return winkel_neu

        elif winkel > 45:

            winkel_neu = 90 - abs(winkel)

            return winkel_neu
