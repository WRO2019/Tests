from ev3dev.ev3 import *
from time import sleep

mA = Motor("outA")

sleep(0.5)
print("Hallo, Helmut!")
mA.run_forever(speed_sp=500)
