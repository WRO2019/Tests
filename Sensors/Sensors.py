import threading
from ev3dev.ev3 import *
from time import sleep
from enum import Enum
import time
import logging
import Utility


############################################################
class Sensors:

    def __init__(self, port, mode, sensor_type):
        print(str(sensor_type) + " wurde initialisiert")
        self.port = port
        self.mode = mode
        self.sensor_type = sensor_type
        self.__smoothvalues = {}
        self.sensor = Sensor(self.port.value)
        self.__isreadingruning = True
        if mode is not None:
            self.sensor.mode = self.mode

    ############################################################
    # Starten des Glätens
    def start_reading_threads(self, value_type, threads, messwerte, pause):
        print("Starte " + str(threads) + " Threads")
        gesamtzeit = pause * messwerte  # Zeit eines Durchlaufs(Smoothen Wetres)
        startdifference = gesamtzeit / threads  # Versatz der Threads
        if threads == 1:
            startdifference = 0
        for i in range(threads):
            thread = threading.Thread(target=self.__reading_values, args=(messwerte, pause, value_type,))
            thread.start()
            print("Thread gestartet: " + str(time.time()))
            sleep(startdifference)

    ############################################################
    # Werte glätten nach angegebenen Parametern
    def __reading_values(self, messwerte, pause, value_type):
        print(str(value_type) + "-reading Thread started")
        while self.__isreadingruning:
            werte = []
            for x in range(messwerte):
                werte.append(self.sensor.value())
                sleep(pause)
            gesamt = 0
            for wert in werte:
                gesamt += wert
                print("add " + str(wert))
            if gesamt != 0:
                self.__smoothvalues[value_type] = gesamt / messwerte

    ############################################################

    def get_value(self, value_type):
        if value_type == ValueTypes.raw:
            return self.sensor.value()
        elif value_type == ValueTypes.gyro_angel:
            return self.__get_gyro_angel()
        elif value_type == ValueTypes.ir_angel:
            return self.sensor.value()
        elif value_type == ValueTypes.ir_distance:
            return self.__get_ir_distance()
        elif value_type == ValueTypes.ir_angel_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value" + str(self.__smoothvalues)
        elif value_type == ValueTypes.ir_distance_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value" + str(self.__smoothvalues)

    ############################################################

    def __get_gyro_angel(self):
        value = self.sensor.value()
        while value >= 360:
            value -= 360
        while value <= -360:
            value += 360
        return value

    ############################################################

    def __get_ir_distance(self):
        werte = []
        werte.append(self.sensor.value('1'))
        werte.append(self.sensor.value('2'))
        werte.append(self.sensor.value('3'))
        werte.append(self.sensor.value('4'))
        werte.append(self.sensor.value('5'))
        werte.append(self.sensor.value('6'))
        werte.sort()
        return werte[5]


########################################################################################################################
########################################################################################################################

class Ports(Enum):
    in1 = "in1"
    in2 = "in2"
    in3 = "in3"
    in4 = "in4"


############################################################

class SensorTypes(Enum):
    gyro_sensor = "gyro_sensor"
    ir_sensor = "ir_sensor"
    us_sensor = "us_sensor"
    button_sensor = "button_sensor"
    colour_sensor = "colour_sensor"


############################################################

class ValueTypes(Enum):
    raw = "raw"
    ir_distance = "ir_distance"
    ir_angel = "ir_angel"
    ir_distance_smooth = "ir_distance_smooth"
    ir_angel_smooth = "ir_angel_smooth"
    gyro_angel = "gyro_angel"

############################################################

class Colors(Enum):
    green = "green"
    blue = "blue"
    red = "red"
