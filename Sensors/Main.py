import Sensors
import logging

############################################################
# Printing Sensors-Values

while True:
    logging.warning("IR-Angel: " + str(Sensors.get_ir_angel()))
    logging.warning("IR-Direction: " + str(Sensors.get_ir_direction()))
    logging.warning("IR-Distance: " + str(Sensors.get_ir_distance()))
    logging.warning("Ultrasonis-Distance: " + str(Sensors.get_ultrasonic_distance()))
    logging.warning("Gyron-Angel: " + str(Sensors.get_gyro_angel()))
    logging.warning("---------------------------------------------")
