import time
import serial
class a_serial():
    def __init__(self):
        self.ser = serial.Serial(

            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        counter = 0
    def read_line(self):
        return self.ser.readline()
    def close_connection(self):
        self.ser.close()
    def to_int(self,x):
        b = x.split('\n')
        if b[0] == None:
            return 0
        else:
            c = b[0].split('\r')
            return c[0]

    def votage(self):
        x = self.read_line()
        return self.to_int(x)

if __name__ == "__main__":
    a = a_serial()
    for i in range(0,10):
        w = a.votage()
        print(w)
        time.sleep(0.001)
    a.close_connection()