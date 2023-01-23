import serial
import time
from datetime import datetime
import h5py
import numpy as np

BEGIN = b'B'
STOP = b'S'


class Datastream:

    def __init__(self):
        self.SerialData = serial.Serial('com17', 9600)

        self.Matrix = [[0.0 for x in range(8)] for y in range(8)]  # create a Matrix full of zeros
        self.x = 0  # initialize variables to zero
        self.y = 0
        self.READING_TABLE = False
        self.READING_COMPLETED = False

        self.MCP1_temp = 0.0
        self.MCP2_temp = 0.0
        self.DHT_hum = 0.0
        self.DHT_temp = 0.0
        self.DHT_hi = 0.0
        self.MLXAmb = 0.0
        self.MLXObj = 0.0
        self.Moist = 0

        self.Thermal_table_dict = {}
        self.MCP1_temp_dict = {}
        self.MCP2_temp_dict = {}
        self.DHT_hum_dict = {}
        self.DHT_temp_dict = {}
        self.DHT_hi_dict = {}
        self.MLXAmb_dict = {}
        self.MLXObj_dict = {}
        self.Moist_dict = {}

        # self.createhdfs()

    def readData(self):
        if (self.SerialData.inWaiting() > 0):  # if there are data sent from arduino
            myData = self.SerialData.readline()  # read the first line

            if self.READING_TABLE == True and b']' not in myData:  # if we have started reading the matrix sent from arduino
                numbers_list = myData.split(b',')  # split the line using the ',' as a seperator
                for i in range(8):  # fill the row of the matrix
                    self.Matrix[self.y][self.x] = float(numbers_list[i])  # save in the Matrix the data transformed in floats
                    self.x = self.x + 1  # go to the next column
                self.y = self.y + 1  # go to the next row
                self.x = 0  # go to the first column again

            if b'[' in myData:  # if in the current line there is the '[' means that a new image is sent
                self.READING_TABLE = True  # in that case we start to read
                numbers = myData.split(b'[')  # split the data using the '[' as seperator
                numbers_list = numbers[1].split(b',')  # split them again using the ',' as seperator
                for i in range(8):  # fill the row of the matrix
                    self.Matrix[self.y][self.x] = float(
                        numbers_list[i])  # save in the Matrix the data transformed in floats
                    self.x = self.x + 1  # go to the next column
                self.y = self.y + 1  # go to the next row
                self.x = 0  # go to the first column again

            elif b']' in myData:  # if in the current line there is the ']' means that we have finished reading data
                self.READING_TABLE = False  # finished reading table
                self.x = 0  # re-initializing the variables
                self.y = 0
                self.Thermal_table_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.Matrix
                self.READING_COMPLETED = True

            elif b'x18' in myData:
                temp_list = myData.split(b':')
                self.MCP1_temp = float(temp_list[1])
                self.MCP1_temp_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.MCP1_temp

            elif b'x19' in myData:
                temp_list = myData.split(b':')
                self.MCP2_temp = float(temp_list[1])
                self.MCP2_temp_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.MCP2_temp

            elif b'DHTHum' in myData:
                temp_list = myData.split(b':')
                self.DHT_hum = float(temp_list[1])
                self.DHT_hum_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.DHT_hum

            elif b'DHTTemp' in myData:
                temp_list = myData.split(b':')
                self.DHT_temp = float(temp_list[1])
                self.DHT_temp_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.DHT_temp

            elif b'DHTHI' in myData:
                temp_list = myData.split(b':')
                self.DHT_hi = float(temp_list[1])
                self.DHT_hi_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.DHT_hi

            elif b'MLXAmb' in myData:
                temp_list = myData.split(b':')
                self.MLXAmb = float(temp_list[1])
                self.MLXAmb_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.MLXAmb

            elif b'MLXObj' in myData:
                temp_list = myData.split(b':')
                self.MLXObj = float(temp_list[1])
                self.MLXObj_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.MLXObj

            elif b'Moisture' in myData:
                temp_list = myData.split(b':')
                self.Moist = int(temp_list[1])
                self.Moist_dict[datetime.now().strftime('%Y-%m-%d-%H:%M:%S')] = self.Moist

    def SerialBegin(self):
        self.SerialData.write(BEGIN)

    def SerialStop(self):
        self.SerialData.write(STOP)
        self.READING_TABLE = False
        self.Matrix = [[0.0 for x in range(8)] for y in range(8)]
        self.MCP1_temp = 0.0
        self.MCP2_temp = 0.0
        self.DHT_hum = 0.0
        self.DHT_temp = 0.0
        self.DHT_hi = 0.0
        self.MLXAmb = 0.0
        self.MLXObj = 0.0
        self.Moist = 0

    def showmeasurements(self):

        print("--------------------------------------------------------")
        print(self.Matrix)
        print("MCP1 Temperature is:" + " " + str(self.MCP1_temp) + " °C")
        print("MCP2 Temperature is:" + " " + str(self.MCP2_temp) + " °C")
        print("Humidity is:" + " " + str(self.DHT_hum) + " %")
        print("DHT Temperature is:" + " " + str(self.DHT_temp) + " °C")
        print("DHT Heat Index is:" + " " + str(self.DHT_hi) + " °C")
        print("MLX Ambient Temp is:" + " " + str(self.MLXAmb) + " °C")
        print("MLX Object Temp is:" + " " + str(self.MLXObj) + " °C")
        print("Moisture Level is:" + " " + str(self.Moist))

    def printdictvalues(self):

        print("-------------")
        print(self.MCP1_temp_dict)
        print(self.MCP2_temp_dict)
        print(self.DHT_hum_dict)
        print(self.DHT_temp_dict)
        print(self.DHT_hi_dict)
        print(self.MLXAmb_dict)
        print(self.MLXObj_dict)
        print(self.Moist_dict)
        print(self.Thermal_table_dict)

    def createhdfs(self):

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.h1 = h5py.File("Thermal-" + timestamp + ".hdf5", 'w')
        self.h2 = h5py.File("MCP1-" + timestamp + ".hdf5", 'w')
        self.h3 = h5py.File("MCP2-" + timestamp + ".hdf5", 'w')
        self.h4 = h5py.File("DHThum-" + timestamp + ".hdf5", 'w')
        self.h5 = h5py.File("DHTtemp-" + timestamp + ".hdf5", 'w')
        self.h6 = h5py.File("DHThi-" + timestamp + ".hdf5", 'w')
        self.h7 = h5py.File("MLXAmb-" + timestamp + ".hdf5", 'w')
        self.h8 = h5py.File("MLXObj-" + timestamp + ".hdf5", 'w')
        self.h9 = h5py.File("Moist-" + timestamp + ".hdf5", 'w')

    def savedata(self):

        for k, v in self.Thermal_table_dict.items():
            self.h1.create_dataset(k, data=np.array(v))
        self.h1.close()
        for k, v in self.MCP1_temp_dict.items():
            self.h2.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h2.close()
        for k, v in self.MCP2_temp_dict.items():
            self.h3.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h3.close()
        for k, v in self.DHT_hum_dict.items():
            self.h4.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h4.close()
        for k, v in self.DHT_temp_dict.items():
            self.h5.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h5.close()
        for k, v in self.DHT_hi_dict.items():
            self.h6.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h6.close()
        for k, v in self.MLXAmb_dict.items():
            self.h7.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h7.close()
        for k, v in self.MLXObj_dict.items():
            self.h8.create_dataset(k, data=np.array(v, dtype=np.single))
        self.h8.close()
        for k, v in self.Moist_dict.items():
            self.h9.create_dataset(k, data=np.array(v, dtype=np.intc))
        self.h9.close()

    def cleardict(self):

        self.Thermal_table_dict.clear()
        self.MCP1_temp_dict.clear()
        self.MCP2_temp_dict.clear()
        self.DHT_hum_dict.clear()
        self.DHT_temp_dict.clear()
        self.DHT_hi_dict.clear()
        self.MLXAmb_dict.clear()
        self.MLXObj_dict.clear()
        self.Moist_dict.clear()

    def hdfhandler(self):
        self.savedata()
        self.cleardict()
        self.createhdfs()


if __name__ == '__main__':

    d = Datastream()
    time.sleep(0.5)
    d.SerialBegin()
    d.createhdfs()
    startTime = time.time()

    while (1):

        d.readData()

        if d.READING_COMPLETED:
            #time.sleep(0.5)
            d.showmeasurements()
            # d.printdictvalues()
            d.READING_COMPLETED = False

        if time.time() - startTime > 10 * 60:
            d.hdfhandler()
            startTime = time.time()
