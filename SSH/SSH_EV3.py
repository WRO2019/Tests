from ev3dev.ev3 import *
from time import sleep

mA = Motor("outA")
i = 0

sleep(0.5)
i = 0


while True:
    i = i + 1
    print("Ich bins!")
    print("Helmut! Zum", i, ". Mal")


