import Utility
from time import sleep

diference = 0


############################################################

def get_ir_direction():
    return Utility.irSeeker.value()


############################################################

def get_ir_angel():
    werte = []
    for x in range(0, 10):
        werte.append(Utility.directions[Utility.irSeeker.value()])
        sleep(0.01)
    gesamt = 0
    for x in werte:
        gesamt = gesamt + x

    return gesamt / len(werte)


############################################################

def get_ir_distance():
    return Utility.irSeeker.value("1")  # Falsch


############################################################

def get_ultrasonic_distance():
    return Utility.ultrasonic_Sensor.value()


############################################################

def get_gyro_angel():
    wert = Utility.gyro_sensor.value() + diference
    if wert >= 360:
        Utility.diference = diference - 360
        wert = wert + diference
    elif wert <= -360:
        Utility.diference = diference + 360
        wert = wert + diference
    if -360 < wert < 360:
        return wert
    else:
        return 0
