import threading
from ev3dev.ev3 import Sensor as EV3Sensor
from time import sleep
from Utility import *
import Utility


############################################################

class Ir_Seeker:
    def __init__(self, port):
        self.port = port
        self.__smoothvalues = {}
        self.sensor = EV3Sensor(self.port.value)
        self.isreadingruning = {}
        self.__lastValues = {}
        self.sensor.mode = SensorModes.ir_gefilter.value
        print("Ir-Seeker wurde initialisiert")

    def start_ir_direction_smooth(self):
        for i in range(2):
            self.isreadingruning[ValueTypes.ir_direction_smooth] = True
            thread = threading.Thread(target=self.__reading_values, args=(5, 0.2, ValueTypes.ir_direction_smooth,))
            thread.start()
            sleep(0.5)
        print("Ir-direction-smooth wurde gestartet")

    def start_ir_distance_smooth(self):
        for i in range(2):
            self.isreadingruning[ValueTypes.ir_distance_smooth] = True
            thread = threading.Thread(target=self.__reading_values, args=(5, 0.2, ValueTypes.ir_distance_smooth,))
            thread.start()
            sleep(0.5)
        print("Ir-distance-smooth wurde gestartet")

    def __reading_values(self, messwerte, pause, value_type):
        if value_type == ValueTypes.ir_distance_smooth:
            while self.isreadingruning[value_type]:
                werte = []
                for x in range(messwerte):
                    try:
                        wert = self.__get_ir_distance()
                        if wert is not None:
                            werte.append(wert)
                    except ValueError:
                        break
                    sleep(pause)
                gesamt = 0
                for wert in werte:
                    gesamt += wert
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
                        break
                    sleep(pause)
                gesamt = 0
                for wert in werte:
                    gesamt += wert
                if len(werte) != 0:
                    self.__smoothvalues[value_type] = gesamt / len(werte)

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
            None

    def get_value(self, value_type):
        try:
            if value_type == ValueTypes.ir_direction:
                value = self.sensor.value()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
            ################################
            elif value_type == ValueTypes.ir_distance:
                value = self.__get_ir_distance()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
            ################################
            elif value_type == ValueTypes.ir_angle:
                value = Utility.ir_seeker_angle_area / 9 * self.sensor.value()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
            ################################
            elif value_type == ValueTypes.ir_angle_smooth:
                if self.__smoothvalues.__contains__(ValueTypes.ir_direction_smooth):
                    value = Utility.ir_seeker_angle_area / 9 * self.__smoothvalues[ValueTypes.ir_direction_smooth]
                    if value is not None:
                        self.__lastValues[value_type] = value
                        return value
                    elif self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
                else:
                    if self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
            ################################
            elif value_type == ValueTypes.ir_direction_smooth:
                if self.__smoothvalues.__contains__(value_type):
                    value = self.__smoothvalues[value_type]
                    if value is not None:
                        self.__lastValues[value_type] = value
                        return value
                    elif self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
                else:
                    if self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
            ################################
            elif value_type == ValueTypes.ir_distance_smooth:
                if self.__smoothvalues.__contains__(value_type):
                    value = self.__smoothvalues[value_type]
                    if value is not None:
                        self.__lastValues[value_type] = value
                        return value
                    elif self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
                else:
                    if self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
        except ValueError:
            if self.__lastValues.__contains__(value_type):
                return self.__lastValues[value_type]
            else:
                return None


############################################################

class Gyro_Sensor:
    def __init__(self, port):
        self.port = port
        self.__smoothvalues = {}
        self.sensor = EV3Sensor(self.port.value)
        self.isreadingruning = {}
        self.__lastValues = {}
        print("Gyro-Sensor wurde initialisiert")

    def start_gyro_angel_smooth(self):
        for i in range(2):
            self.isreadingruning[ValueTypes.gyro_angle_smooth] = True
            thread = threading.Thread(target=self.__reading_values, args=(5, 0.2, ValueTypes.gyro_angle_smooth,))
            thread.start()
            sleep(0.5)
        print("Gyro-Angel-smooth wurde gestartet")

    def __reading_values(self, messwerte, pause, value_type):
        while self.isreadingruning[value_type]:
            werte = []
            for x in range(messwerte):
                try:
                    wert = self.__get_gyro_angel()
                    if wert is not None:
                        werte.append(wert)
                except ValueError:
                    break
                sleep(pause)
            gesamt = 0
            for wert in werte:
                gesamt += wert
            if len(werte) != 0:
                self.__smoothvalues[value_type] = gesamt / len(werte)

    def __get_gyro_angel(self):
        try:
            value = self.sensor.value()
            while value >= 360:
                value -= 360
            while value <= -360:
                value += 360
            return value
        except ValueError:
            return None

    def get_value(self, value_type):
        try:
            if value_type == ValueTypes.gyro_angle:
                value = self.__get_gyro_angel()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None

            ################################
            elif value_type == ValueTypes.gyro_angle_smooth:
                if self.__smoothvalues.__contains__(value_type):
                    value = self.__smoothvalues[value_type]
                    if value is not None:
                        self.__lastValues[value_type] = value
                        return value
                    elif self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
                else:
                    if self.__lastValues.__contains__(value_type):
                        return self.__lastValues[value_type]
                    else:
                        return None
        except ValueError:
            if self.__lastValues.__contains__(value_type):
                return self.__lastValues[value_type]
            else:
                return None


############################################################

class Color_Sensor:
    def __init__(self, port):
        self.port = port
        self.__smoothvalues = {}
        self.__lastValues = {}
        self.sensor = EV3Sensor(self.port.value)
        self.isreadingruning = {}
        print("Color-Sensor wurde initialisiert")

    def get_value(self, value_type):
        try:
            if value_type == ValueTypes.color:
                self.sensor.mode = Utility.SensorModes.color.value
                value = Utility.colors[self.sensor.value()]
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
            ################################
            elif value_type == ValueTypes.reflect:
                self.sensor.mode = Utility.SensorModes.reflect.value
                value = self.sensor.value()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
            ################################
            elif value_type == ValueTypes.ambiente:
                self.sensor.mode = Utility.SensorModes.ambiente.value
                value = self.sensor.value()
                if value is not None:
                    self.__lastValues[value_type] = value
                    return value
                elif self.__lastValues.__contains__(value_type):
                    return self.__lastValues[value_type]
                else:
                    return None
        except ValueError:
            if self.__lastValues.__contains__(value_type):
                return self.__lastValues[value_type]
            else:
                return None


############################################################

class Ultrasonic_Sensor:
    def __init__(self, port):
        self.port = port
        self.__smoothvalues = {}
        self.sensor = EV3Sensor(self.port.value)
        self.__lastValue = None
        self.isreadingruning = {}
        self.sensor.mode = 'US-DIST-CM'
        print("Ultraschall-Sensor wurde initialisiert")

    def get_value(self, value_type):
        try:
            if value_type == ValueTypes.ultrasonic_distance:
                value = self.sensor.value()
                if value is not None:
                    self.__lastValue = value
                    return value
                elif self.__lastValue is not None:
                    return self.__lastValue
        except ValueError:
            if self.__lastValue is not None:
                return self.__lastValue
            else:
                return None
