from time import sleep
import Motors

runing = True
counter = 0
while runing:
    Motors.move(180, 400)
    counter = counter + 1
    sleep(1)
    if counter > 30:
        runing = False
Motors.stop()