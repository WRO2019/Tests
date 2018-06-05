import Utility
import threading
from ev3dev.ev3 import *
from time import sleep


############################################################

class Sensors:

    def __init__(self, port, mode=None, specific_sensor=None):
        self.port = port
        self.mode = mode
        self.specific_sensor = specific_sensor
        self.__smoothvalue = 0
        self.sensor = Sensor(self.port)
        self.__isreadingruning = False
        if mode is not None:
            self.sensor.mode = self.mode

    ############################################################
    # Starten des Glätens
    def start_reading_threads(self, threads, messwerte, pause):
        gesamtzeit = pause * messwerte  # Zeit eines Durchlaufs(Smoothen Wetres)
        startdifference = gesamtzeit / threads  # Versatz der Threads
        if threads == 1:
            startdifference = 0
        for i in range(threads):
            thread = threading.Thread(target=self.__reading_values, args=(messwerte, pause,))
            thread.start()
            sleep(startdifference)

    ############################################################
    # Werte glätten nach angegebenen Parametern
    def __reading_values(self, messwerte, pause):
        while self.__isreadingruning:
            werte = []
            for x in range(messwerte):
                werte.append(self.sensor.value())
                sleep(pause)
            gesamt = 0;
            for wert in werte:
                gesamt += wert
            self.__smoothvalue = gesamt / werte.count()

    ############################################################

    def get_smooth_value(self):
        return self.__smoothvalue

    ############################################################
    # Spezifische Werte(muster) für den Sensor ausgeben             Nicht Fertig
    def get_sensor_specific_value(self):
        sensor = self.specific_sensor
        if sensor is None:
            return None
        elif sensor is Utility.Sensors.gyro_sensor:
            value = self.sensor.value
            while value >= 360:
                value -= 360
            while value <= -360:
                value += 360
            return value


############################################################
