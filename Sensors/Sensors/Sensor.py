import threading
from ev3dev.ev3 import *
from time import sleep
from Sensors import Utility
from Sensors.Utility import ValueTypes


############################################################
class Sensor:

    def __init__(self, port, mode, sensor_type):
        print(str(sensor_type) + " wurde initialisiert")
        self.port = port
        self.mode = mode
        self.sensor_type = sensor_type
        self.__smoothvalues = {}
        self.sensor = Sensor(self.port.value)
        self.isreadingruning = []
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
        self.isreadingruning[value_type] = True
        for i in range(threads):
            thread = threading.Thread(target=self.__reading_values, args=(messwerte, pause, value_type, i,))
            thread.start()
            print("Thread gestartet: " + str(time.time()))
            sleep(startdifference)

    ############################################################
    # Werte glätten nach angegebenen Parametern
    def __reading_values(self, messwerte, pause, value_type, number):
        print(str(value_type) + "-reading Thread-" + number + " started")
        while self.isreadingruning[value_type]:
            werte = []
            for x in range(messwerte):
                werte.append(self.sensor.value())
                sleep(pause)
            gesamt = 0
            for wert in werte:
                gesamt += wert
                print("Thread-" + number + "added: " + str(wert))
            if gesamt != 0:
                self.__smoothvalues[value_type] = gesamt / messwerte

    ############################################################

    def get_value(self, value_type):
        if value_type == ValueTypes.raw:
            return self.sensor.value()
        ################################
        elif value_type == ValueTypes.gyro_angle:
            return self.__get_gyro_angel()
        ################################
        elif value_type == ValueTypes.ir_direction:
            return self.sensor.value()
        ################################
        elif value_type == ValueTypes.ir_distance:
            return self.__get_ir_distance()
        ################################
        elif value_type == ValueTypes.ir_angle:
            return Utility.ir_seeker_angle_area / 9 * self.sensor.value()
        ################################
        elif value_type == ValueTypes.ir_angle_smooth:
            return Utility.ir_seeker_angle_area / 9 * self.__smoothvalues[value_type]
        ################################
        elif value_type == ValueTypes.ir_direction_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value" + str(self.__smoothvalues)
        ################################
        elif value_type == ValueTypes.ir_distance_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value" + str(self.__smoothvalues)
        ################################
        elif value_type == ValueTypes.color:
            return Utility.colors[self.sensor.value()]

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
