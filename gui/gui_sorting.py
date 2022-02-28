# Created by: PyQt5 UI code generator 5.15.6

# import PyQt5 modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
# import OPC UA Client (Pure Python OPC UA)
from opcua import Client
import logging
# import time 
import time

def getNodeValue(io_root,var_name):
# read node value
    client_node = client.get_node('.'.join((io_root,var_name)))
    return client_node.get_value()

def changeBoolNodeValue(var_name):
# switch node value (boolean)
    client_node = client.get_node('.'.join((io_root,var_name)))
    value = client_node.get_value()
    client_node = client.set_values([client_node] ,[not value])

def switchState(buttonName):
# invert node value (write) method called by button
    client_node = client.get_node('.'.join((io_root,buttonName)))
    value = client_node.get_value()
    client_node = client.set_values([client_node] ,[not value]) 

def changeColor(button):
# change button color if pressed
    # if button is checked
    if button.isChecked():
        # setting background color to light-blue
        button.setStyleSheet("background-color : lightgreen")
    # if it is unchecked
    else:
        # set background color back to light-grey
        button.setStyleSheet("background-color : #f0f0f0")

def changeColorLabel(label,value,color_on="lightgreen",color_off="#f0f0f0"):
# change color of a label
    if value:
        label.setStyleSheet("background-color : "+color_on)
    else:
        label.setStyleSheet("background-color : "+color_off)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(40, 90, 111, 41))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 140, 111, 41))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 190, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 240, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 290, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 340, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 390, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 60, 91, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(28, 440, 141, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 30, 21, 21))
        self.label_1.setAutoFillBackground(True)
        self.label_1.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setMidLineWidth(1)
        self.label_1.setTextFormat(QtCore.Qt.RichText)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 21, 21))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setMidLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(50, 30, 21, 21))
        self.label_0.setAutoFillBackground(True)
        self.label_0.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_0.setMidLineWidth(1)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 192, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton_0.setText(_translate("MainWindow", "FeederConveyor"))
        self.pushButton_0.clicked.connect(lambda: switchState("buttonFeederConveyor"))
        self.pushButton_0.setCheckable(True)
        self.pushButton_0.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_0.clicked.connect(lambda: changeColor(self.pushButton_0))

        self.pushButton_1.setText(_translate("MainWindow", "EntryConveyor"))
        self.pushButton_1.clicked.connect(lambda: switchState("buttonEntryConveyor"))
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_1.clicked.connect(lambda: changeColor(self.pushButton_1))

        self.pushButton_2.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.clicked.connect(lambda: switchState("buttonLoad"))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_2.clicked.connect(lambda: changeColor(self.pushButton_2))

        self.pushButton_3.setText(_translate("MainWindow", "Unload"))
        self.pushButton_3.clicked.connect(lambda: switchState("buttonUnload"))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_3.clicked.connect(lambda: changeColor(self.pushButton_3))

        self.pushButton_4.setText(_translate("MainWindow", "Turn"))
        self.pushButton_4.clicked.connect(lambda: switchState("buttonTurn"))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_4.clicked.connect(lambda: changeColor(self.pushButton_4))

        self.pushButton_5.setText(_translate("MainWindow", "LeftConveyor"))
        self.pushButton_5.clicked.connect(lambda: switchState("buttonLeftConveyor"))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_5.clicked.connect(lambda: changeColor(self.pushButton_5))

        self.pushButton_6.setText(_translate("MainWindow", "RightConveyor"))
        self.pushButton_6.clicked.connect(lambda: switchState("buttonRightConveyor"))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setStyleSheet("background-color : #f0f0f0")
        self.pushButton_6.clicked.connect(lambda: changeColor(self.pushButton_6))

        self.label_5.setText(_translate("MainWindow", "-CONTROLS-"))
        self.label_0.setText(_translate("MainWindow", "M"))
        self.label_1.setText(_translate("MainWindow", "A"))
        self.label_2.setText(_translate("MainWindow", "E"))
        self.label.setText(_translate("MainWindow", "manual controls V1.00"))

        self.thread = Thread()
        self.thread.update.connect(lambda: changeColorLabel(label = self.label_0,
                                                            value = getNodeValue(io_root,"iManual")))
        self.thread.update.connect(lambda: changeColorLabel(label = self.label_1,
                                                            value = getNodeValue(io_root,"iAuto")))
        self.thread.update.connect(lambda: changeColorLabel(label = self.label_2,
                                                            value = getNodeValue(io_root,"iEmergencyStop"),
                                                            color_on = "lightgreen",
                                                            color_off = "red"))
        self.thread.start()

class Thread(QThread):
# Thread with signal, that emits every 1s
    def __init__(self,):
        super(QThread, self).__init__()
    update = pyqtSignal()
    def run(self):
        while True:
            time.sleep(1)
            self.update.emit()
            
if __name__ == "__main__":
    # set connection to CODESYS OPC server
    logging.info("Read/Write variable from CODESYS with OPC-UA Client")
    url = "opc.tcp://localhost:4841"
    io_root = "ns=4;s=|var|CODESYS Control Win V3 x64.Application.FIO"
    client = Client(url)
    try:
        client.connect()
    except:
        print("Connection not possible")
        time.sleep(3)
    # setup GUI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_(),client.disconnect())