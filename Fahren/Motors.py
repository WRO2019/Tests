import Utility
import math
from time import sleep

motorSpeed = 800

def move(winkel, speed):
    winkel = winkel - 180
    winkel_neu = Utility.winkel_form(winkel)
    if winkel < 0:

        if winkel > -44:

            speed_neu = speed * math.sin(math.radians(winkel_neu))

            Utility.mA.run_forever(speed_sp=-speed_neu)

            Utility.mB.run_forever(speed_sp=-speed_neu)

            Utility.mC.run_forever(speed_sp=1.4 * speed)

            Utility.mD.run_forever(speed_sp=-1.4 * speed)

            sleep(0.01)

        elif winkel <= -45:

            if winkel <= -180:
                i = 1
            else:
                i = -1

            speed_neu = speed * math.sin(math.radians(winkel_neu))

            Utility.mA.run_forever(speed_sp=-speed_neu)

            Utility.mB.run_forever(speed_sp=-speed_neu)

            Utility.mC.run_forever(speed_sp=i * 1.4 * speed)

            Utility.mD.run_forever(speed_sp=i * -1.4 * speed)

            sleep(0.01)

    elif winkel == 0:

        Utility.mA.run_forever(speed_sp=-speed)

        Utility.mB.run_forever(speed_sp=-speed)

        Utility.mC.run_forever(speed_sp=-1.4 * speed)

        Utility.mD.run_forever(speed_sp=1.4 * speed)

        sleep(0.01)

    elif winkel > 0:

        if winkel < 44:

            speed_neu = speed * math.cos(math.radians(winkel_neu))

            Utility.mA.run_forever(speed_sp=-speed)

            Utility.mB.run_forever(speed_sp=-speed)

            Utility.mC.run_forever(speed_sp=-1.4 * speed_neu)

            Utility.mD.run_forever(speed_sp=1.4 * speed_neu)

            sleep(0.01)

        elif winkel == 180:
            speed_neu = speed * math.sin(math.radians(winkel_neu))

            Utility.mA.run_forever(speed_sp=speed)

            Utility.mB.run_forever(speed_sp=speed)

            Utility.mC.run_forever(speed_sp=1.4 * speed_neu)

            Utility.mD.run_forever(speed_sp=-1.4 * speed_neu)

        elif winkel >= 45:

            i = 1

            if winkel > 90:
                i = -1

            speed_neu = speed * math.sin(math.radians(winkel_neu))

            Utility.mA.run_forever(speed_sp=-speed)

            Utility.mB.run_forever(speed_sp=-speed)

            Utility.mC.run_forever(speed_sp=-1.4 * i * speed_neu)

            Utility.mD.run_forever(speed_sp=1.4 * i * speed_neu)

            sleep(0.01)


def stop():
    Utility.mA.stop()
    Utility.mB.stop()
    Utility.mC.stop()
    Utility.mD.stop()
    Utility.mA.reset()
    Utility.mB.reset()
    Utility.mC.reset()
    Utility.mD.reset()
