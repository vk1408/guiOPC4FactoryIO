# guiOPC4FactoryIO
In this project I built a Graphical User Interface (GUI) for FACTORY IO scene "Sorting by Height (Advanced)" with CODESYS control. This GUI allows manual control of sorting machine actuators. The GUI, as well as Factory IO is connected to CODESYS runtime via OPC UA protocol. 
The GUI is made with QT Creator from PyQt5 module for python and then converted to .py (Python) file.
The OPC UA client is programmed using module Pure Python OPC UA:
https://github.com/FreeOpcUa/python-opcua

Here is how the scene "Sorting by Height (Advanced)" in Factory IO looks like:
![image](https://user-images.githubusercontent.com/84286885/156048658-b73d17c7-0f67-4c57-b2bd-ce2d3193d5b1.png)

This scene is a standard simulation scene that comes along with FACTORY IO Software.
To download the Factory IO go to https://factoryio.com/buy

In this scene there is one control panel, that lacks any manual control functions:
![image](https://user-images.githubusercontent.com/84286885/156052483-a6f04a51-075c-4c38-8169-327035b6df64.png)

I decided to make a simplistic GUI for manual controls to fix that:

![image](https://user-images.githubusercontent.com/84286885/156052713-56b3c5bd-2770-495a-badd-223b086ab638.png)

"E" stand for E-Stop, "A" and "M" for Auto and Manual modes.

You need to set up an OPC UA Server in CODESYS Software and connect it to Factory IO. Here is the official tutorial:
https://docs.factoryio.com/tutorials/codesys/setting-up/codesys-opc-ua-sp17/

Note, that the standart server port 4840 could be occupied by windows, so change it to 4841 if it is the case.

!!!In CODESYS you will need PLC program PLC_PRG and two variables lists FIO and GVL. FIO is used for OPC UA variables of
Factory IO and GUI, so you need to make it visible for OPC clients in "Symbol Configiration" in CODESYS.!!!

You can import variable lists and main program for CODESYS from /plc folder. Use Project->Import for that.

Versions:

CODESYS Runtime: V3.5 SP17 patch2 (64 bit)

PyQT5: 5.5.16

QT Creator: 6.0.0

opcua: 0.98.13
