import Utility
import math
import logging
motorSpeed = 800

def move(winkel, speed):
    winkel_neu = Utility.winkel_form(winkel)

    if winkel_neu < 0:  # Winkel positiv machen
        winkel_neu = winkel_neu * -1

    speed_two = speed * math.tan(math.radians(winkel_neu))
    #Utility.mA._speed_sp=
    ############################################################
    if 45 < winkel < 90:  # positive
        speed_two = speed_two * -1
    if 135 < winkel < 180:
        speed_two = speed_two * -1
    if 180 < winkel < 225:
        speed_two = speed_two * -1
    if 270 < winkel < 315:
        speed_two = speed_two * -1
    ############################################################
    if -45 > winkel > -90:  # negative
        speed_two = speed_two * -1
    if -135 > winkel > -180:
        speed_two = speed_two * -1
    if -180 > winkel > -225:
        speed_two = speed_two * -1
    if -270 > winkel > -315:
        speed_two = speed_two * -1
    ############################################################
    logging.warning("Winkel: " + str(winkel))
    logging.warning("Speed_two: " + str(speed_two))
    logging.warning("Speed: " + str(speed))
    setMotors(winkel, speed_two, speed)

##########################################################################################################
# check welches Motorpaar speed bekommt
def setMotors(winkel, speed_two, speed):

    if Utility.isEqualTo(winkel, [0, 360, -360]):  # ohne speed_two wenn 45 Rheie und
        logging.warning("Bin bei 0")
        Utility.mA.run_forever(speed_sp=speed)  # motoren Gleichen Speed benötigen
        Utility.mB.run_forever(speed_sp=speed)
        Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif Utility.isEqualTo(winkel, [45 , -315]):
        logging.warning("Bin bei 45")
        Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif Utility.isEqualTo(winkel, [90, -270]):
        logging.warning("Bin bei 90")
        Utility.mA.run_forever(speed_sp=-speed)
        Utility.mB.run_forever(speed_sp=-speed)
        Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif Utility.isEqualTo(winkel, [135, -225]):
        logging.warning("Bin bei 135")
        Utility.mA.run_forever(speed_sp=-speed)
        Utility.mB.run_forever(speed_sp=-speed)
    elif Utility.isEqualTo(winkel, [180, -180]):
        logging.warning("Bin bei 180")
        Utility.mA.run_forever(speed_sp=-speed)
        Utility.mB.run_forever(speed_sp=-speed)
        Utility.mC.run_forever(speed_sp=1.4 * speed)
        Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Utility.isEqualTo(winkel, [255, -135]):
        logging.warning("Bin bei 255")
        Utility.mC.run_forever(speed_sp=1.4 * speed)
        Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Utility.isEqualTo(winkel, [270, -90]):
        logging.warning("Bin bei 270")
        Utility.mA.run_forever(speed_sp=speed)
        Utility.mB.run_forever(speed_sp=speed)
        Utility.mC.run_forever(speed_sp=1.4 * speed)
        Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Utility.isEqualTo(winkel, [315, -45]):
        logging.warning("Bin bei 315")
        Utility.mA.run_forever(speed_sp=speed)
        Utility.mB.run_forever(speed_sp=speed)

    ############################################################

    elif 0 < winkel < 90 or -270 > winkel > 360:  # Mit speed_two
        Utility.mA.run_forever(speed_sp=speed_two)
        Utility.mB.run_forever(speed_sp=speed_two)
        Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif 90 < winkel < 180 or -180 > winkel > -270:
        Utility.mA.run_forever(speed_sp=-speed)
        Utility.mB.run_forever(speed_sp=-speed)
        Utility.mC.run_forever(speed_sp=1.4 * speed_two)
        Utility.mD.run_forever(speed_sp=-1.4 * speed_two)
    elif 180 < winkel < 270 or -90 > winkel > -180:
        Utility.mA.run_forever(speed_sp=speed_two)
        Utility.mB.run_forever(speed_sp=speed_two)
        Utility.mC.run_forever(speed_sp=1.4 * speed)
        Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif 270 < winkel < 360 or 0 > winkel > -90:
        Utility.mA.run_forever(speed_sp=speed)
        Utility.mB.run_forever(speed_sp=speed)
        Utility.mC.run_forever(speed_sp=1.4 * speed_two)
        Utility.mD.run_forever(speed_sp=-1.4 * speed_two)



##########################################################################################################

def stop():
    Utility.mA.stop()
    Utility.mB.stop()
    Utility.mC.stop()
    Utility.mD.stop()
    Utility.mA.reset()
    Utility.mB.reset()
    Utility.mC.reset()
    Utility.mD.reset()
