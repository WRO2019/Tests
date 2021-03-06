import Motors_Utility
import math
import logging

motorSpeed = 800


def move(winkel, speed):
    winkel_neu = Motors_Utility.winkel_form(winkel)

    if winkel_neu < 0:  # Winkel positiv machen
        winkel_neu = winkel_neu * -1

    speed_two = speed * math.tan(math.radians(winkel_neu))
    # Utility.mA._speed_sp=
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
    # speed_two = round(speed_two, 2)
    logging.warning("Winkel: " + str(winkel))
    logging.warning("Speed_two: " + str(speed_two))
    logging.warning("Speed: " + str(speed))
    setMotors(winkel, speed_two, speed)


##########################################################################################################
# check welches Motorpaar speed bekommt
def setMotors(winkel, speed_two, speed):
    if Motors_Utility.isEqualTo(winkel, [0, 360, -360]):  # ohne speed_two wenn 45 Rheie und
        logging.warning("Bin bei 0/360/-360")
        Motors_Utility.mA.run_forever(speed_sp=speed)  # motoren Gleichen Speed benötigen
        Motors_Utility.mB.run_forever(speed_sp=speed)
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif Motors_Utility.isEqualTo(winkel, [45, -315]):
        logging.warning("Bin bei 45/-315")
        Motors_Utility.mA.run_forever(speed_sp=speed)
        Motors_Utility.mB.run_forever(speed_sp=speed)
    elif Motors_Utility.isEqualTo(winkel, [90, -270]):
        logging.warning("Bin bei 90/-270")
        Motors_Utility.mA.run_forever(speed_sp=speed)
        Motors_Utility.mB.run_forever(speed_sp=speed)
        Motors_Utility.mC.run_forever(speed_sp=1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Motors_Utility.isEqualTo(winkel, [135, -225]):
        logging.warning("Bin bei 135/-255")
        Motors_Utility.mC.run_forever(speed_sp=1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Motors_Utility.isEqualTo(winkel, [180, -180]):
        logging.warning("Bin bei 180/-180")
        Motors_Utility.mA.run_forever(speed_sp=-speed)
        Motors_Utility.mB.run_forever(speed_sp=-speed)
        Motors_Utility.mC.run_forever(speed_sp=1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif Motors_Utility.isEqualTo(winkel, [225, -135]):
        logging.warning("Bin bei 225/-135")
        Motors_Utility.mA.run_forever(speed_sp=-speed)
        Motors_Utility.mB.run_forever(speed_sp=-speed)
    elif Motors_Utility.isEqualTo(winkel, [270, -90]):
        logging.warning("Bin bei 270/-90")
        Motors_Utility.mA.run_forever(speed_sp=-speed)
        Motors_Utility.mB.run_forever(speed_sp=-speed)
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed)
    elif Motors_Utility.isEqualTo(winkel, [315, -45]):
        logging.warning("Bin bei 315/-45")
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed)

    ############################################################

    elif 0 < winkel < 90 or -270 > winkel > 360:  # Mit speed_two
        Motors_Utility.mA.run_forever(speed_sp=speed)
        Motors_Utility.mB.run_forever(speed_sp=speed)
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed_two)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed_two)
    elif 90 < winkel < 180 or -180 > winkel > -270:
        Motors_Utility.mA.run_forever(speed_sp=speed_two)
        Motors_Utility.mB.run_forever(speed_sp=speed_two)
        Motors_Utility.mC.run_forever(speed_sp=1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=-1.4 * speed)
    elif 180 < winkel < 270 or -90 > winkel > -180:
        Motors_Utility.mA.run_forever(speed_sp=-speed)
        Motors_Utility.mB.run_forever(speed_sp=-speed)
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed_two)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed_two)
    elif 270 < winkel < 360 or 0 > winkel > -90:
        Motors_Utility.mA.run_forever(speed_sp=speed_two)
        Motors_Utility.mB.run_forever(speed_sp=speed_two)
        Motors_Utility.mC.run_forever(speed_sp=-1.4 * speed)
        Motors_Utility.mD.run_forever(speed_sp=1.4 * speed)


##########################################################################################################

def stop():
    Motors_Utility.mA.stop()
    Motors_Utility.mB.stop()
    Motors_Utility.mC.stop()
    Motors_Utility.mD.stop()
    Motors_Utility.mA.reset()
    Motors_Utility.mB.reset()
    Motors_Utility.mC.reset()
    Motors_Utility.mD.reset()
