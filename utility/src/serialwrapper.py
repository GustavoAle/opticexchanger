import serial
import serial.tools.list_ports

class SerialWrapper(object):
    __serial = None
    __connected = None

    def __init__(self):
        self.__connected__ = False
        self.__serial = serial.Serial()

    #***************************************************************************
    #                               IS methods
    #***************************************************************************

    def is_connected(self):
        self.__connected = self.__serial.is_open
        return self.__connected

    #***************************************************************************
    #                               GET methods
    #***************************************************************************

    def get_comports(self):
        __aux = []
        __comports = serial.tools.list_ports.comports()
        for port in __comports:
            __aux.append(port.device)

        return __aux

    def get_serial(self):
        return self.__serial

    def get_connectedcomport(self):
        if self.is_connected():
            return self.__serial.port
        return None

    def get_port(self):
        return self.__serial.port

    #***************************************************************************
    #                              SET methods
    #***************************************************************************

    def set_port(self,__port):
        self.__serial.port = __port

    #***************************************************************************
    #                              OTHER methods
    #***************************************************************************

    def connect(self,__port,__baudrate=115200):
        self.__serial.port = __port
        self.__serial.baudrate = __baudrate
        self.__serial.open()
