import sys

import seaborn as sb
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datastream import Datastream


class Canvas(FigureCanvas):

    def __init__(self, parent=None, width=7, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.d = Datastream()

        self.setWindowTitle("Arduino Data Receiver")
        self.setGeometry(30, 30, 1280, 720)

        self.canvas = Canvas(self, width=7, height=5, dpi=100)
        # self.setCentralWidget(self.canvas)
        self.canvas.move(0, 0)

        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setText("Start")
        self.start_button.move(100, 600)
        # self.start_button.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.start_button.clicked.connect(self.startPlot)

        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setText("Stop")
        self.stop_button.move(250, 600)
        # self.stop_button.setGeometry(QtCore.QRect(400, 0, 200, 40))
        self.stop_button.clicked.connect(self.stopPlot)

        self.read_timer = QtCore.QTimer(self)
        self.read_timer.timeout.connect(self.readData)

        self.save_timer = QtCore.QTimer(self)
        self.save_timer.timeout.connect(self.d.hdfhandler)

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("MCP1 Temperature is:" + " " + str(self.d.MCP1_temp) + " °C")
        self.label_1.adjustSize()
        self.label_1.move(850, 50)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("MCP2 Temperature is:" + " " + str(self.d.MCP2_temp) + " °C")
        self.label_2.adjustSize()
        self.label_2.move(850, 100)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("Humidity is:" + " " + str(self.d.DHT_hum) + " %")
        self.label_3.adjustSize()
        self.label_3.move(850, 150)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setText("DHT Temperature is:" + " " + str(self.d.DHT_temp) + " °C")
        self.label_4.adjustSize()
        self.label_4.move(850, 200)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setText("DHT Heat Index is:" + " " + str(self.d.DHT_hi) + " °C")
        self.label_5.adjustSize()
        self.label_5.move(850, 250)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setText("MLX Ambient Temp is:" + " " + str(self.d.MLXAmb) + " °C")
        self.label_6.adjustSize()
        self.label_6.move(850, 300)

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setText("MLX Object Temp is:" + " " + str(self.d.MLXObj) + " °C")
        self.label_7.adjustSize()
        self.label_7.move(850, 350)

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setText("Moisture Level is:" + " " + str(self.d.Moist))
        self.label_8.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        self.label_8.adjustSize()
        self.label_8.move(850, 400)

        self.heat_map = sb.heatmap(self.d.Matrix, vmin=15, vmax=50, annot=True, fmt='', ax=self.canvas.axes)

    def plotData(self):
        self.heat_map.clear()
        self.heat_map = sb.heatmap(self.d.Matrix, vmin=15, vmax=50, annot=True, fmt='', ax=self.canvas.axes, cbar=False)
        self.canvas.draw()
        self.label_1.setText("MCP1 Temperature is:" + " " + str(self.d.MCP1_temp) + " °C")
        self.label_1.adjustSize()
        self.label_2.setText("MCP2 Temperature is:" + " " + str(self.d.MCP2_temp) + " °C")
        self.label_2.adjustSize()
        self.label_3.setText("Humidity is:" + " " + str(self.d.DHT_hum) + " %")
        self.label_3.adjustSize()
        self.label_4.setText("DHT Temperature is:" + " " + str(self.d.DHT_temp) + " °C")
        self.label_4.adjustSize()
        self.label_5.setText("DHT Heat Index is:" + " " + str(self.d.DHT_hi) + " °C")
        self.label_5.adjustSize()
        self.label_6.setText("MLX Ambient Temp is:" + " " + str(self.d.MLXAmb) + " °C")
        self.label_6.adjustSize()
        self.label_7.setText("MLX Object Temp is:" + " " + str(self.d.MLXObj) + " °C")
        self.label_7.adjustSize()
        self.label_8.setText("Moisture Level is:" + " " + str(self.d.Moist))

        if self.d.Moist >= 500:
            self.label_8.setStyleSheet("background-color: orange; border: 1px solid black;")
        elif self.d.Moist <= 250:
            self.label_8.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        else:
            self.label_8.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.label_8.adjustSize()

    def readData(self):
        self.d.readData()
        if self.d.READING_COMPLETED:
            self.plotData()
            self.d.READING_COMPLETED = False

    def startPlot(self):
        self.d.SerialBegin()
        self.d.createhdfs()
        self.read_timer.start()
        self.save_timer.start(10 * 60 * 1000)

    def stopPlot(self):
        self.read_timer.stop()
        self.save_timer.stop()
        self.d.savedata()
        self.d.cleardict()
        self.d.SerialStop()
        self.plotData()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()

    sys.exit(app.exec_())
