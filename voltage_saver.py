from sql_connector import *
from time import sleep
import threading
from arduino_serial import *

class Voltage_saver():
    def __init__(self):
        self.sql =sql_connector()

    def save_voltage(self,v):

        self.__write_vol(v)

    def __write_vol(self,v):
        sql = "INSERT INTO `spaceapp_laravel`.`voltages` (`ID`, `email`, `datatime`)  VALUES (NULL,"+v+",CURRENT_TIMESTAMP)"
        self.sql.Q(sql)
    def voltage_loop(self,interval):
        while True:
            v = read_vol_serial()
            self.save_voltage(v)
            sleep(interval)
def read_vol_serial():
    seria = a_serial()
    voltage_data = seria.votage()
    return voltage_data

def vol_start( ):
    a =Voltage_saver()
    while True:
        a.voltage_loop(interval=0.001)

def therad_voltage_start():
    t = threading.Thread(name='vol_t', target=vol_start)
    t.start()

if __name__ == "__main__":
    therad_voltage_start()
