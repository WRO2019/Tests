import threading
from ev3dev.ev3 import Sensor as EV3Sensor
from time import sleep
import time
from Utility import ValueTypes
import Utility


############################################################

class Sensor:

    def __init__(self, port, mode):
        print("Sensor wurde initialisiert")
        self.port = port
        self.mode = mode
        self.__smoothvalues = {}
        self.sensor = EV3Sensor(self.port.value)
        self.isreadingruning = {}
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
        print(str(value_type) + "-reading Thread-" + str(number) + " started")
        if value_type == ValueTypes.ir_distance_smooth:
            print("IR-Distance")
            while self.isreadingruning[value_type]:
                werte = []
                for x in range(messwerte):
                    wert = self.__get_ir_distance()
                    if wert is not None:
                        werte.append(wert)
                    sleep(pause)
                gesamt = 0
                for wert in werte:
                    gesamt += wert
                    print("Thread-" + str(number) + "added: " + str(wert))
                print("len: " + str(len(werte)))
                if len(werte) != 0:
                    self.__smoothvalues[value_type] = gesamt / len(werte)
        else:
            while self.isreadingruning[value_type]:
                werte = []
                for x in range(messwerte):
                    try:
                        wert = self.sensor.value()
                        if wert is not None:
                            werte.append(wert)
                    except ValueError:
                        print("Fehler smoth")
                    sleep(pause)
                gesamt = 0
                for wert in werte:
                    gesamt += wert
                    print("Thread-" + str(number) + "added: " + str(wert))
                print("len: " + str(len(werte)))
                if len(werte) != 0:
                    self.__smoothvalues[value_type] = gesamt / len(werte)

    ############################################################

    def get_value(self, value_type):
        if value_type == ValueTypes.raw:
            return self.sensor.value()
        ################################
        elif value_type == ValueTypes.gyro_angle:
            return self.__get_gyro_angel()
        ################################
        elif value_type == ValueTypes.gyro_angle_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value"
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
            if self.__smoothvalues.__contains__(value_type):
                return Utility.ir_seeker_angle_area / 9 * self.__smoothvalues[value_type]
            else:
                return "No Smooth Value"
        ################################
        elif value_type == ValueTypes.ir_direction_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value"
        ################################
        elif value_type == ValueTypes.ir_distance_smooth:
            if self.__smoothvalues.__contains__(value_type):
                return self.__smoothvalues[value_type]
            else:
                return "No Smooth Value"
        ################################
        elif value_type == ValueTypes.color:
            self.sensor.mode = Utility.SensorModes.color
            return Utility.colors[self.sensor.value()]
        ################################
        elif value_type == ValueTypes.reflect:
            self.sensor.mode = Utility.SensorModes.reflect
            return Utility.colors[self.sensor.value()]
        ################################
        elif value_type == ValueTypes.ambiente:
            self.sensor.mode = Utility.SensorModes.ambiente
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
        try:
            werte.append(self.sensor.value('1'))
            werte.append(self.sensor.value('2'))
            werte.append(self.sensor.value('3'))
            werte.append(self.sensor.value('4'))
            werte.append(self.sensor.value('5'))
            werte.sort()
            return werte[4]
        except ValueError:
            print("Fehler bei distance")
