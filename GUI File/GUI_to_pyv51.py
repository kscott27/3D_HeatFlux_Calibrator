# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIfirstTry2.ui'
# Created by: PyQt5 UI code generator 5.9.2


'''
@Author Alex Schnorr and Kevin Scott
5/20/18

For the use of the Cal Poly FPE program

This program is intended to provide a graphical user interface for the opperation of a cone heater
calibration device.

Version 39 updates: imcrem, sensor settings, bug fixes

Known Bugs: None
To Do Next:

*1) Fix heatflux reading
*2) Get Pause and Resume serial working
*3) Get homing routine serial working
*4) Send steps through serial
*5) Save coordinates and runtime data to csv files
*6) validate that unit switching is consistent
*7) enable to run on user coordinates or machine coordiantes from coordinate entry table
*8) Continous/incremental running serial commands
*9) step size for incremental mode
10) get 2D plot data slicing working
*11) fix 3d plot so that marker is cleared upon reset
*12) set up sensor delay time over serial
*13) run speed and linear accelartion settings via serial
14) set up serial connection auto refresh and connection, fix sloppy code
*15) Estop procedure
16) Fix window resizing issue
*17) get feedback from emberley and make appropiate changes
*17) Begin testing for bugs and making things fancy!!
18) Add timing info


*Done


'''

from PyQt5 import QtCore, QtGui, QtWidgets # ,Qt3DAnimation, PyQt3D, PyQtChart, PyQtDataVisualization
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import serial.tools.list_ports # add necessary import
import sys # add necessary import
import glob, os # add necessary import
import math
from time import sleep
from mplwidget import MplWidget
from mplwidget3d import MplWidget3D
import re
import csv

'''**************************************Auto generated code*******************************************************'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 762)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 655))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.runModeTab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runModeTab.sizePolicy().hasHeightForWidth())
        self.runModeTab.setSizePolicy(sizePolicy)
        self.runModeTab.setMinimumSize(QtCore.QSize(600, 300))
        self.runModeTab.setMaximumSize(QtCore.QSize(600, 300))
        self.runModeTab.setObjectName("runModeTab")
        self.manTab = QtWidgets.QWidget()
        self.manTab.setObjectName("manTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.manTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(44, 30, 541, 123))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.zeroZ = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setKerning(True)
        self.zeroZ.setFont(font)
        self.zeroZ.setObjectName("zeroZ")
        self.gridLayout_2.addWidget(self.zeroZ, 2, 1, 1, 1)
        self.flipZ = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.flipZ.setObjectName("flipZ")
        self.gridLayout_2.addWidget(self.flipZ, 2, 0, 1, 1)
        self.xStopButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 128, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 128, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.xStopButton.setPalette(palette)
        self.xStopButton.setObjectName("xStopButton")
        self.gridLayout_2.addWidget(self.xStopButton, 0, 4, 1, 1)
        self.zeroX = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zeroX.setObjectName("zeroX")
        self.gridLayout_2.addWidget(self.zeroX, 0, 1, 1, 1)
        self.yStopButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 128, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 128, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 124, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 62, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 1, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(126, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.yStopButton.setPalette(palette)
        self.yStopButton.setObjectName("yStopButton")
        self.gridLayout_2.addWidget(self.yStopButton, 1, 4, 1, 1)
        self.zMinusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setKerning(True)
        self.zMinusButton.setFont(font)
        self.zMinusButton.setObjectName("zMinusButton")
        self.gridLayout_2.addWidget(self.zMinusButton, 2, 3, 1, 1)
        self.flipY = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.flipY.setObjectName("flipY")
        self.gridLayout_2.addWidget(self.flipY, 1, 0, 1, 1)
        self.xPlusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.xPlusButton.setObjectName("xPlusButton")
        self.gridLayout_2.addWidget(self.xPlusButton, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.yMinusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.yMinusButton.setObjectName("yMinusButton")
        self.gridLayout_2.addWidget(self.yMinusButton, 1, 3, 1, 1)
        self.xMinusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.xMinusButton.setObjectName("xMinusButton")
        self.gridLayout_2.addWidget(self.xMinusButton, 0, 3, 1, 1)
        self.zStopButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.zStopButton.setPalette(palette)
        self.zStopButton.setObjectName("zStopButton")
        self.gridLayout_2.addWidget(self.zStopButton, 2, 4, 1, 1)
        self.zeroY = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zeroY.setObjectName("zeroY")
        self.gridLayout_2.addWidget(self.zeroY, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.flipX = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.flipX.setObjectName("flipX")
        self.gridLayout_2.addWidget(self.flipX, 0, 0, 1, 1)
        self.yPlusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.yPlusButton.setObjectName("yPlusButton")
        self.gridLayout_2.addWidget(self.yPlusButton, 1, 5, 1, 1)
        self.zPlusButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zPlusButton.setObjectName("zPlusButton")
        self.gridLayout_2.addWidget(self.zPlusButton, 2, 5, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.manTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 571, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.homeRoutineButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.homeRoutineButton.setObjectName("homeRoutineButton")
        self.verticalLayout_8.addWidget(self.homeRoutineButton)
        self.goHomeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.goHomeButton.setObjectName("goHomeButton")
        self.verticalLayout_8.addWidget(self.goHomeButton)
        self.machineRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.machineRadio.setChecked(True)
        self.machineRadio.setObjectName("machineRadio")
        self.verticalLayout_8.addWidget(self.machineRadio)
        self.userRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.userRadio.setObjectName("userRadio")
        self.verticalLayout_8.addWidget(self.userRadio)
        self.horizontalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem4 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_15.addItem(spacerItem4)
        self.keyboardCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.keyboardCheck.setChecked(True)
        self.keyboardCheck.setObjectName("keyboardCheck")
        self.verticalLayout_15.addWidget(self.keyboardCheck)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_18.addWidget(self.label_39)
        self.controlTypeDropDown = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.controlTypeDropDown.setObjectName("controlTypeDropDown")
        self.controlTypeDropDown.addItem("")
        self.controlTypeDropDown.addItem("")
        self.horizontalLayout_18.addWidget(self.controlTypeDropDown)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_17.addWidget(self.label_11)
        self.stepSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.stepSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.stepSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.stepSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stepSpinBox.setKeyboardTracking(False)
        self.stepSpinBox.setProperty("value", 1.0)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.horizontalLayout_17.addWidget(self.stepSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_10.addLayout(self.verticalLayout_15)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.manTab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(19, 10, 531, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_20.addWidget(self.label_17)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_20.addWidget(self.label_10)
        self.runModeTab.addTab(self.manTab, "")
        self.coordinateEnterTab = QtWidgets.QWidget()
        self.coordinateEnterTab.setObjectName("coordinateEnterTab")
        self.layoutWidget = QtWidgets.QWidget(self.coordinateEnterTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 352, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pointTable = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointTable.sizePolicy().hasHeightForWidth())
        self.pointTable.setSizePolicy(sizePolicy)
        self.pointTable.setMinimumSize(QtCore.QSize(200, 192))
        self.pointTable.setMaximumSize(QtCore.QSize(500, 500))
        self.pointTable.setRowCount(11)
        self.pointTable.setObjectName("pointTable")
        self.pointTable.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(2, item)
        self.pointTable.horizontalHeader().setDefaultSectionSize(100)
        self.pointTable.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout_9.addWidget(self.pointTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.entryNumber = QtWidgets.QSpinBox(self.layoutWidget)
        self.entryNumber.setMaximum(999999999)
        self.entryNumber.setProperty("value", 10)
        self.entryNumber.setObjectName("entryNumber")
        self.horizontalLayout_2.addWidget(self.entryNumber)
        self.coorSysDropDown = QtWidgets.QComboBox(self.layoutWidget)
        self.coorSysDropDown.setObjectName("coorSysDropDown")
        self.coorSysDropDown.addItem("")
        self.coorSysDropDown.addItem("")
        self.horizontalLayout_2.addWidget(self.coorSysDropDown)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.coordinateEnterTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(370, 0, 123, 241))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.coorNameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.coorNameLineEdit.setObjectName("coorNameLineEdit")
        self.verticalLayout_10.addWidget(self.coorNameLineEdit)
        self.coordinateSaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.coordinateSaveButton.setObjectName("coordinateSaveButton")
        self.verticalLayout_10.addWidget(self.coordinateSaveButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.runTableCoordButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.runTableCoordButton.setObjectName("runTableCoordButton")
        self.verticalLayout_10.addWidget(self.runTableCoordButton)
        self.runModeTab.addTab(self.coordinateEnterTab, "")
        self.datTab = QtWidgets.QWidget()
        self.datTab.setObjectName("datTab")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.datTab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(60, 20, 486, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.fileSelectDropDown = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.fileSelectDropDown.setObjectName("fileSelectDropDown")
        self.fileSelectDropDown.addItem("")
        self.horizontalLayout_9.addWidget(self.fileSelectDropDown)
        self.importButton = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setMinimumSize(QtCore.QSize(159, 0))
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_9.addWidget(self.importButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.runModeTab.addTab(self.datTab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, 8, 591, 221))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nameEnterField = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.nameEnterField.setMaxLength(12)
        self.nameEnterField.setObjectName("nameEnterField")
        self.gridLayout_3.addWidget(self.nameEnterField, 5, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)
        self.xReadings = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xReadings.sizePolicy().hasHeightForWidth())
        self.xReadings.setSizePolicy(sizePolicy)
        self.xReadings.setMaximumSize(QtCore.QSize(40, 16777215))
        self.xReadings.setMaxLength(32766)
        self.xReadings.setObjectName("xReadings")
        self.gridLayout_3.addWidget(self.xReadings, 0, 2, 1, 1)
        self.yReadings = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.yReadings.setMaximumSize(QtCore.QSize(40, 16777215))
        self.yReadings.setObjectName("yReadings")
        self.gridLayout_3.addWidget(self.yReadings, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 1, 1, 1)
        self.zReadings = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.zReadings.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zReadings.setObjectName("zReadings")
        self.gridLayout_3.addWidget(self.zReadings, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 3, 8, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.xMin = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.xMin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.xMin.setObjectName("xMin")
        self.horizontalLayout_11.addWidget(self.xMin)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 0, 3, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_13.addWidget(self.label_35)
        self.zMin = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.zMin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zMin.setObjectName("zMin")
        self.horizontalLayout_13.addWidget(self.zMin)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 2, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_12.addWidget(self.label_36)
        self.yMin = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.yMin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.yMin.setObjectName("yMin")
        self.horizontalLayout_12.addWidget(self.yMin)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 1, 3, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_14.addWidget(self.label_38)
        self.xMax = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.xMax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.xMax.setObjectName("xMax")
        self.horizontalLayout_14.addWidget(self.xMax)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 0, 5, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_15.addWidget(self.label_41)
        self.yMax = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.yMax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.yMax.setObjectName("yMax")
        self.horizontalLayout_15.addWidget(self.yMax)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 1, 5, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_16.addWidget(self.label_42)
        self.zMax = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.zMax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zMax.setObjectName("zMax")
        self.horizontalLayout_16.addWidget(self.zMax)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 2, 5, 1, 1)
        self.generateButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setMaximumSize(QtCore.QSize(100, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.generateButton.setPalette(palette)
        self.generateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout_3.addWidget(self.generateButton, 5, 8, 1, 1)
        self.drawWordButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.drawWordButton.setObjectName("drawWordButton")
        self.gridLayout_3.addWidget(self.drawWordButton, 5, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 8, 1, 1)
        self.runModeTab.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 20, 102, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_32 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_32.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_16.addWidget(self.label_32)
        self.sensorDelaySpinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.sensorDelaySpinBox.setMaximum(50)
        self.sensorDelaySpinBox.setProperty("value", 10)
        self.sensorDelaySpinBox.setObjectName("sensorDelaySpinBox")
        self.verticalLayout_16.addWidget(self.sensorDelaySpinBox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 80, 221, 140))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_44 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_22.addWidget(self.label_44)
        self.stepsPerRevDropDown = QtWidgets.QComboBox(self.layoutWidget_2)
        self.stepsPerRevDropDown.setObjectName("stepsPerRevDropDown")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.stepsPerRevDropDown.addItem("")
        self.horizontalLayout_22.addWidget(self.stepsPerRevDropDown)
        self.verticalLayout_14.addLayout(self.horizontalLayout_22)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_14.addWidget(self.label_45)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.sensorDropDown = QtWidgets.QComboBox(self.layoutWidget_2)
        self.sensorDropDown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sensorDropDown.setEditable(True)
        self.sensorDropDown.setObjectName("sensorDropDown")
        self.sensorDropDown.addItem("")
        self.horizontalLayout_23.addWidget(self.sensorDropDown)
        self.verticalLayout_14.addLayout(self.horizontalLayout_23)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(300, 20, 111, 50))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_46 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_46.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_18.addWidget(self.label_46)
        self.sensorReadingsSpinBox = QtWidgets.QSpinBox(self.layoutWidget_3)
        self.sensorReadingsSpinBox.setMinimum(1)
        self.sensorReadingsSpinBox.setMaximum(20000)
        self.sensorReadingsSpinBox.setProperty("value", 10000)
        self.sensorReadingsSpinBox.setObjectName("sensorReadingsSpinBox")
        self.verticalLayout_18.addWidget(self.sensorReadingsSpinBox)
        self.runModeTab.addTab(self.tab, "")
        self.verticalLayout_7.addWidget(self.runModeTab)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.resumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeButton.setObjectName("resumeButton")
        self.horizontalLayout_5.addWidget(self.resumeButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_5.addWidget(self.resetButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_5.addWidget(self.cancelButton)
        self.eStopButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(234, 0, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 0, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 0, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.eStopButton.setPalette(palette)
        self.eStopButton.setObjectName("eStopButton")
        self.horizontalLayout_5.addWidget(self.eStopButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(10, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem10)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_6.addWidget(self.label_40)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        spacerItem11 = QtWidgets.QSpacerItem(10, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem11)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.xUser = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.xUser.setPalette(palette)
        self.xUser.setSmallDecimalPoint(True)
        self.xUser.setObjectName("xUser")
        self.verticalLayout.addWidget(self.xUser)
        self.yUser = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.yUser.setPalette(palette)
        self.yUser.setSmallDecimalPoint(True)
        self.yUser.setObjectName("yUser")
        self.verticalLayout.addWidget(self.yUser)
        self.zUser = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.zUser.setPalette(palette)
        self.zUser.setSmallDecimalPoint(True)
        self.zUser.setObjectName("zUser")
        self.verticalLayout.addWidget(self.zUser)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setMinimumSize(QtCore.QSize(0, 25))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.xMach = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.xMach.setPalette(palette)
        self.xMach.setSmallDecimalPoint(True)
        self.xMach.setObjectName("xMach")
        self.verticalLayout_2.addWidget(self.xMach)
        self.yMach = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.yMach.setPalette(palette)
        self.yMach.setSmallDecimalPoint(True)
        self.yMach.setObjectName("yMach")
        self.verticalLayout_2.addWidget(self.yMach)
        self.zMach = QtWidgets.QLCDNumber(self.centralwidget)
        self.zMach.setEnabled(True)
        self.zMach.setBaseSize(QtCore.QSize(132, 129))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.zMach.setPalette(palette)
        self.zMach.setSmallDecimalPoint(True)
        self.zMach.setObjectName("zMach")
        self.verticalLayout_2.addWidget(self.zMach)
        spacerItem12 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem12)
        self.unitsDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.unitsDropDown.setObjectName("unitsDropDown")
        self.unitsDropDown.addItem("")
        self.unitsDropDown.addItem("")
        self.unitsDropDown.addItem("")
        self.unitsDropDown.addItem("")
        self.verticalLayout_2.addWidget(self.unitsDropDown)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 2, 2, 1, 1)
        self.m3Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.m3Temp.setPalette(palette)
        self.m3Temp.setObjectName("m3Temp")
        self.gridLayout_4.addWidget(self.m3Temp, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)
        self.m2Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.m2Temp.setPalette(palette)
        self.m2Temp.setObjectName("m2Temp")
        self.gridLayout_4.addWidget(self.m2Temp, 1, 1, 1, 1)
        self.t3Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.t3Temp.setPalette(palette)
        self.t3Temp.setObjectName("t3Temp")
        self.gridLayout_4.addWidget(self.t3Temp, 2, 3, 1, 1)
        self.m1Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.m1Temp.setPalette(palette)
        self.m1Temp.setObjectName("m1Temp")
        self.gridLayout_4.addWidget(self.m1Temp, 0, 1, 1, 1)
        self.t1Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.t1Temp.setPalette(palette)
        self.t1Temp.setObjectName("t1Temp")
        self.gridLayout_4.addWidget(self.t1Temp, 0, 3, 1, 1)
        self.t2Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.t2Temp.setPalette(palette)
        self.t2Temp.setObjectName("t2Temp")
        self.gridLayout_4.addWidget(self.t2Temp, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 3, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 1, 2, 1, 1)
        self.m4Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.m4Temp.setPalette(palette)
        self.m4Temp.setObjectName("m4Temp")
        self.gridLayout_4.addWidget(self.m4Temp, 3, 1, 1, 1)
        self.t4Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.t4Temp.setPalette(palette)
        self.t4Temp.setObjectName("t4Temp")
        self.gridLayout_4.addWidget(self.t4Temp, 3, 3, 1, 1)
        self.m5Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.m5Temp.setPalette(palette)
        self.m5Temp.setObjectName("m5Temp")
        self.gridLayout_4.addWidget(self.m5Temp, 4, 1, 1, 1)
        self.t5Temp = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.t5Temp.setPalette(palette)
        self.t5Temp.setObjectName("t5Temp")
        self.gridLayout_4.addWidget(self.t5Temp, 4, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 4, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setObjectName("label_47")
        self.gridLayout_4.addWidget(self.label_47, 4, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_12.addWidget(self.label_22)
        self.heatFlux = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 155, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.heatFlux.setPalette(palette)
        self.heatFlux.setDigitCount(6)
        self.heatFlux.setObjectName("heatFlux")
        self.verticalLayout_12.addWidget(self.heatFlux)
        self.getHeatFlux = QtWidgets.QPushButton(self.centralwidget)
        self.getHeatFlux.setObjectName("getHeatFlux")
        self.verticalLayout_12.addWidget(self.getHeatFlux)
        spacerItem13 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem13)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_13.addWidget(self.label_31)
        self.speedSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedSlider.setMinimumSize(QtCore.QSize(200, 0))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(10)
        self.speedSlider.setProperty("value", 5)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speedSlider.setTickInterval(1)
        self.speedSlider.setObjectName("speedSlider")
        self.verticalLayout_13.addWidget(self.speedSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.nodesLeft = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.nodesLeft.setPalette(palette)
        self.nodesLeft.setObjectName("nodesLeft")
        self.horizontalLayout_8.addWidget(self.nodesLeft)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_8.addWidget(self.label_34)
        self.totalNodes = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.totalNodes.setPalette(palette)
        self.totalNodes.setObjectName("totalNodes")
        self.horizontalLayout_8.addWidget(self.totalNodes)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.timeRemaining = QtWidgets.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.timeRemaining.setPalette(palette)
        self.timeRemaining.setObjectName("timeRemaining")
        self.horizontalLayout_8.addWidget(self.timeRemaining)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QtCore.QSize(100, 32))
        self.label_37.setMaximumSize(QtCore.QSize(1000, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_5.addWidget(self.label_37)
        self.dataTab = QtWidgets.QTabWidget(self.centralwidget)
        self.dataTab.setObjectName("dataTab")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.threeDPlot = MplWidget3D(self.tab_4)
        self.threeDPlot.setGeometry(QtCore.QRect(-1, -1, 551, 341))
        self.threeDPlot.setObjectName("threeDPlot")
        self.dataTab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.twoDPlot = MplWidget(self.tab_5)
        self.twoDPlot.setGeometry(QtCore.QRect(50, -10, 471, 361))
        self.twoDPlot.setObjectName("twoDPlot")
        self.twoDSpinBox = QtWidgets.QSpinBox(self.tab_5)
        self.twoDSpinBox.setGeometry(QtCore.QRect(0, 160, 48, 24))
        self.twoDSpinBox.setMinimum(0)
        self.twoDSpinBox.setMaximum(0)
        self.twoDSpinBox.setObjectName("twoDSpinBox")
        self.dataTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.outputTablePreview = QtWidgets.QTableWidget(self.tab_6)
        self.outputTablePreview.setGeometry(QtCore.QRect(0, 0, 521, 301))
        self.outputTablePreview.setObjectName("outputTablePreview")
        self.outputTablePreview.setColumnCount(5)
        self.outputTablePreview.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTablePreview.setHorizontalHeaderItem(4, item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 300, 431, 33))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.exportButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_6.addWidget(self.exportButton)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.dataNameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.dataNameLineEdit.setObjectName("dataNameLineEdit")
        self.horizontalLayout_6.addWidget(self.dataNameLineEdit)
        self.clearDataTable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clearDataTable.setObjectName("clearDataTable")
        self.horizontalLayout_6.addWidget(self.clearDataTable)
        self.dataTab.addTab(self.tab_6, "")
        self.verticalLayout_5.addWidget(self.dataTab)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.serialDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.serialDropDown.setObjectName("serialDropDown")
        self.horizontalLayout_7.addWidget(self.serialDropDown)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setMinimumSize(QtCore.QSize(140, 32))
        self.connectButton.setMaximumSize(QtCore.QSize(140, 16777215))
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_7.addWidget(self.connectButton)
        self.refreshSerButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshSerButton.sizePolicy().hasHeightForWidth())
        self.refreshSerButton.setSizePolicy(sizePolicy)
        self.refreshSerButton.setMinimumSize(QtCore.QSize(140, 32))
        self.refreshSerButton.setMaximumSize(QtCore.QSize(140, 16777215))
        self.refreshSerButton.setObjectName("refreshSerButton")
        self.horizontalLayout_7.addWidget(self.refreshSerButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSave_Settings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.runModeTab.setCurrentIndex(0)
        self.dataTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zeroZ.setText(_translate("MainWindow", "0 Z"))
        self.flipZ.setText(_translate("MainWindow", "Invert"))
        self.xStopButton.setText(_translate("MainWindow", "Stop X"))
        self.zeroX.setText(_translate("MainWindow", "0 X"))
        self.yStopButton.setText(_translate("MainWindow", "Stop Y"))
        self.zMinusButton.setText(_translate("MainWindow", "Z -"))
        self.flipY.setText(_translate("MainWindow", "Invert"))
        self.xPlusButton.setText(_translate("MainWindow", "X +"))
        self.yMinusButton.setText(_translate("MainWindow", "Y -"))
        self.xMinusButton.setText(_translate("MainWindow", "X -"))
        self.zStopButton.setText(_translate("MainWindow", "Stop Z"))
        self.zeroY.setText(_translate("MainWindow", "0 Y"))
        self.flipX.setText(_translate("MainWindow", "Invert"))
        self.yPlusButton.setText(_translate("MainWindow", "Y +"))
        self.zPlusButton.setText(_translate("MainWindow", "Z +"))
        self.homeRoutineButton.setText(_translate("MainWindow", "Run Homing Routine"))
        self.goHomeButton.setText(_translate("MainWindow", "Go to Origin"))
        self.machineRadio.setText(_translate("MainWindow", "    Machine"))
        self.userRadio.setText(_translate("MainWindow", "    User"))
        self.keyboardCheck.setText(_translate("MainWindow", "Enable Keyboard Control"))
        self.label_39.setText(_translate("MainWindow", "Control Type:"))
        self.controlTypeDropDown.setItemText(0, _translate("MainWindow", "Continous"))
        self.controlTypeDropDown.setItemText(1, _translate("MainWindow", "Incremental"))
        self.label_11.setText(_translate("MainWindow", "Step Distance:"))
        self.label_17.setText(_translate("MainWindow", "User Coordinates Setup"))
        self.label_10.setText(_translate("MainWindow", "Manual Button Control"))
        self.runModeTab.setTabText(self.runModeTab.indexOf(self.manTab), _translate("MainWindow", "Manual Control"))
        item = self.pointTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.pointTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.pointTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.pointTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.pointTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.pointTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.pointTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.pointTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.pointTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.pointTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.pointTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.pointTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.pointTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Z"))
        self.label.setText(_translate("MainWindow", "Entries:"))
        self.coorSysDropDown.setItemText(0, _translate("MainWindow", "User Coordinates"))
        self.coorSysDropDown.setItemText(1, _translate("MainWindow", "Machine Coordinates"))
        self.label_4.setText(_translate("MainWindow", "Save As:"))
        self.coordinateSaveButton.setText(_translate("MainWindow", "Save as .CSV"))
        self.runTableCoordButton.setText(_translate("MainWindow", "Run"))
        self.runModeTab.setTabText(self.runModeTab.indexOf(self.coordinateEnterTab), _translate("MainWindow", "Coordinate Entry"))
        self.label_13.setText(_translate("MainWindow", "Current Directory:"))
        self.fileSelectDropDown.setItemText(0, _translate("MainWindow", "--NO FILES DETECTED--"))
        self.importButton.setText(_translate("MainWindow", "Import Coordinates"))
        self.runModeTab.setTabText(self.runModeTab.indexOf(self.datTab), _translate("MainWindow", "From Data File"))
        self.label_33.setText(_translate("MainWindow", "Name Entry:"))
        self.label_15.setText(_translate("MainWindow", "X Nodes"))
        self.label_16.setText(_translate("MainWindow", "Y Nodes"))
        self.xReadings.setText(_translate("MainWindow", "5"))
        self.yReadings.setText(_translate("MainWindow", "5"))
        self.label_14.setText(_translate("MainWindow", "Z Nodes"))
        self.zReadings.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "X min"))
        self.xMin.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "Z min"))
        self.zMin.setText(_translate("MainWindow", "0"))
        self.label_36.setText(_translate("MainWindow", "Y min"))
        self.yMin.setText(_translate("MainWindow", "0"))
        self.label_38.setText(_translate("MainWindow", "X max"))
        self.xMax.setText(_translate("MainWindow", "5"))
        self.label_41.setText(_translate("MainWindow", "Y max"))
        self.yMax.setText(_translate("MainWindow", "5"))
        self.label_42.setText(_translate("MainWindow", "Z max"))
        self.zMax.setText(_translate("MainWindow", "5"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.drawWordButton.setText(_translate("MainWindow", "Draw Word"))
        self.runModeTab.setTabText(self.runModeTab.indexOf(self.tab_3), _translate("MainWindow", "Generated Coordinates"))
        self.label_32.setText(_translate("MainWindow", "Sensor Delay (s)"))
        self.label_44.setText(_translate("MainWindow", "Pulse/Rev:"))
        self.stepsPerRevDropDown.setCurrentText(_translate("MainWindow", "400"))
        self.stepsPerRevDropDown.setItemText(0, _translate("MainWindow", "400"))
        self.stepsPerRevDropDown.setItemText(1, _translate("MainWindow", "800"))
        self.stepsPerRevDropDown.setItemText(2, _translate("MainWindow", "1600"))
        self.stepsPerRevDropDown.setItemText(3, _translate("MainWindow", "3200"))
        self.stepsPerRevDropDown.setItemText(4, _translate("MainWindow", "6400"))
        self.stepsPerRevDropDown.setItemText(5, _translate("MainWindow", "12800"))
        self.stepsPerRevDropDown.setItemText(6, _translate("MainWindow", "25600"))
        self.stepsPerRevDropDown.setItemText(7, _translate("MainWindow", "1000"))
        self.stepsPerRevDropDown.setItemText(8, _translate("MainWindow", "2000"))
        self.stepsPerRevDropDown.setItemText(9, _translate("MainWindow", "4000"))
        self.stepsPerRevDropDown.setItemText(10, _translate("MainWindow", "5000"))
        self.stepsPerRevDropDown.setItemText(11, _translate("MainWindow", "8000"))
        self.stepsPerRevDropDown.setItemText(12, _translate("MainWindow", "10000"))
        self.stepsPerRevDropDown.setItemText(13, _translate("MainWindow", "20000"))
        self.stepsPerRevDropDown.setItemText(14, _translate("MainWindow", "25000"))
        self.label_45.setText(_translate("MainWindow", "Sensor Calibration Value: "))
        self.sensorDropDown.setCurrentText(_translate("MainWindow", "K (kW/m^2mV) = 6.28930818"))
        self.sensorDropDown.setItemText(0, _translate("MainWindow", "K (kW/m^2mV) = 6.28930818"))
        self.label_46.setText(_translate("MainWindow", "Nodal Readings"))
        self.runModeTab.setTabText(self.runModeTab.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.label_6.setText(_translate("MainWindow", "Status and Runtime Controls"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.resumeButton.setText(_translate("MainWindow", "Resume"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel Run"))
        self.eStopButton.setText(_translate("MainWindow", "Stop"))
        self.label_40.setText(_translate("MainWindow", "X"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.label_12.setText(_translate("MainWindow", "Z"))
        self.label_19.setText(_translate("MainWindow", "  User Coordinates  "))
        self.label_18.setText(_translate("MainWindow", "Operation Units:"))
        self.label_20.setText(_translate("MainWindow", "Machine Coordinates"))
        self.unitsDropDown.setItemText(0, _translate("MainWindow", "in"))
        self.unitsDropDown.setItemText(1, _translate("MainWindow", "mm"))
        self.unitsDropDown.setItemText(2, _translate("MainWindow", "cm"))
        self.unitsDropDown.setItemText(3, _translate("MainWindow", "m"))
        self.label_21.setText(_translate("MainWindow", "Temperatures (C)"))
        self.label_28.setText(_translate("MainWindow", "T3"))
        self.label_24.setText(_translate("MainWindow", "M2"))
        self.label_25.setText(_translate("MainWindow", "M3"))
        self.label_23.setText(_translate("MainWindow", "M1"))
        self.label_29.setText(_translate("MainWindow", "T4"))
        self.label_26.setText(_translate("MainWindow", "M4"))
        self.label_27.setText(_translate("MainWindow", "T1"))
        self.label_30.setText(_translate("MainWindow", "T2"))
        self.label_43.setText(_translate("MainWindow", "M5"))
        self.label_47.setText(_translate("MainWindow", "T5"))
        self.label_22.setText(_translate("MainWindow", "Heat Flux"))
        self.getHeatFlux.setText(_translate("MainWindow", "Get Heat Flux"))
        self.label_31.setText(_translate("MainWindow", "Run Speed %"))
        self.label_34.setText(_translate("MainWindow", "Nodes Left of:"))
        self.label_8.setText(_translate("MainWindow", "Reading Time(s):"))
        self.label_2.setText(_translate("MainWindow", "Program Setup"))
        self.label_37.setText(_translate("MainWindow", "Real Time Data Viewer"))
        self.dataTab.setTabText(self.dataTab.indexOf(self.tab_4), _translate("MainWindow", "3D Data Plot"))
        self.dataTab.setTabText(self.dataTab.indexOf(self.tab_5), _translate("MainWindow", "2D Plane Plot"))
        item = self.outputTablePreview.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.outputTablePreview.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.outputTablePreview.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.outputTablePreview.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.outputTablePreview.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.outputTablePreview.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.outputTablePreview.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.outputTablePreview.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.outputTablePreview.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "10"))
        item = self.outputTablePreview.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "11"))
        item = self.outputTablePreview.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "12"))
        item = self.outputTablePreview.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "13"))
        item = self.outputTablePreview.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "14"))
        item = self.outputTablePreview.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "15"))
        item = self.outputTablePreview.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Heat Flux"))
        item = self.outputTablePreview.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X"))
        item = self.outputTablePreview.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Y"))
        item = self.outputTablePreview.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Z"))
        item = self.outputTablePreview.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        self.exportButton.setText(_translate("MainWindow", ">>Export Data to CSV<<"))
        self.label_3.setText(_translate("MainWindow", "Save As:"))
        self.clearDataTable.setText(_translate("MainWindow", "Clear"))
        self.dataTab.setTabText(self.dataTab.indexOf(self.tab_6), _translate("MainWindow", "Data Table"))
        self.label_5.setText(_translate("MainWindow", "Serial Connection Manager"))
        self.connectButton.setText(_translate("MainWindow", "Connect to Device "))
        self.refreshSerButton.setText(_translate("MainWindow", "Refresh Device List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionHelp.setText(_translate("MainWindow", "User Manual"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))

        '''**************************************End of Auto generated code******************************************'''

        # system properties and values initizialization
        self.coordinateData = [] # stores all x, y, z data from csv file as 3 X N matrix
        self.machineCoordinates = [0, 0, 0] # stores current machine coordinate point
        self.userOffset = [0, 0, 0, 1, 1, 1] # offset from machine coordinates [x offset, y offset, z offset, x axis flip (1: No ,-1: yes), y axis flip, z axis flip]
        self.motor_temp1 = '---' # properties for temperatures
        self.motor_temp2 = '---'
        self.motor_temp3 = '---'
        self.motor_temp4 = '---'
        self.motor_temp5 = '---'
        self.arm_temp = '---'
        self.frame_temp = '---'
        self.water_temp = '---'
        self.heat_flux = '---'
        self.dataOutputArray = [] # output data with x,y,x, heatflux
        self.slicedData = [] # N X M array of data sliced from dataOutputArray with N slices (X distance) and M points in an X slice
        self.unitsConversionFactor = 1 # if units are changed this is used to convert
        self.threeDScat  = None #instance of 3d scatter plot object
        self.twoDScat = None #instance of 2d scatter plot object
        self.progressBar.setValue(0) # clear progress bar
        self.completionPercent = 0 # keep track of run completion percentage
        self.positionTrack = None # #instance of 3d scatter plot object marker for where sensor is on 3d graph
        self.systemIsRunningCalibration = False #keep track of when we're running
        self.systemIsPaused = False #keep track of when system pauses operation
        self.mode = 'c'
        self.timer_start = 0
        self.system_time = 0


        # system refresh and initialization
        self.ser_port =  None # default serial port
        self.refreshSerial() # load serial with avaible ports upon initialization
        self.refreshDirectoryFiles() # load current directory files
        self.outputTablePreview.setRowCount(0) #clear out the preview table
        self.unitsChange() #set units to default
        #self.sensorDelaySet() # set sensor delay to default value
        self.stepsPerRevDropDown.setCurrentIndex(2) #dealfualt to 1600 steps
        MainWindow.setWindowTitle(_translate("MainWindow", "Cal Poly FPE Heat Flux Calibration Interface")) #set program name

        # button color initialization
        self.changeButtonColor(self.xStopButton, 'red')
        self.changeButtonColor(self.yStopButton, 'red')
        self.changeButtonColor(self.zStopButton, 'red')

        # button method connects
        self.connectButton.clicked.connect(self.setupSerial) # when connect is pressed connect serial
        self.runTableCoordButton.clicked.connect(self.goToTableCoordinates) # coordinate to go to
        self.importButton.clicked.connect(self.importCsvFile) # import csv coordinate file
        self.refreshSerButton.clicked.connect(self.refreshSerial) # refresh serial list whenever it is clicked
        self.unitsDropDown.currentIndexChanged.connect(self.unitsChange) # change the units of the system
        self.xPlusButton.clicked.connect(self.xPlus) # connect manual control button with its method
        self.xPlusButton.released.connect(self.xStop) # connect manual control button with its method
        self.yPlusButton.clicked.connect(self.yPlus)  # connect manual control button with its method
        self.yPlusButton.released.connect(self.yStop)  # connect manual control button with its method
        self.zPlusButton.clicked.connect(self.zPlus)  # connect manual control button with its method
        self.zPlusButton.released.connect(self.zStop)  # connect manual control button with its method
        self.xMinusButton.clicked.connect(self.xMinus)  # connect manual control button with its method
        self.xMinusButton.released.connect(self.xStop)  # connect manual control button with its method
        self.yMinusButton.clicked.connect(self.yMinus)  # connect manual control button with its method
        self.yMinusButton.released.connect(self.yStop)  # connect manual control button with its method
        self.zMinusButton.clicked.connect(self.zMinus)  # connect manual control button with its method
        self.zMinusButton.released.connect(self.zStop)  # connect manual control button with its method
        self.xStopButton.clicked.connect(self.xStop)  # connect manual control button with its method
        self.yStopButton.clicked.connect(self.yStop)  # connect manual control button with its method
        self.zStopButton.clicked.connect(self.zStop)  # connect manual control button with its method
        self.resetButton.clicked.connect(self.reset)  # connect reset button with its method
        self.entryNumber.valueChanged.connect(self.updatePointTableSize) # update the size of the point table
        self.flipX.stateChanged.connect(self.setUserOffset) #set user offset for axis system X
        self.flipY.stateChanged.connect(self.setUserOffset) #set user offset for axis system Y
        self.flipZ.stateChanged.connect(self.setUserOffset) #set user offset for axis system Z
        self.zeroX.clicked.connect(self.zeroXOffset) #zero user offset X
        self.zeroY.clicked.connect(self.zeroYOffset) #zero user offset Y
        self.zeroZ.clicked.connect(self.zeroZOffset) #zero user offset Z
        self.getHeatFlux.clicked.connect(self.requestHeatFlux) #enable heatflux output
        self.homeRoutineButton.clicked.connect(self.homeRoutine) #run homing routine
        self.goHomeButton.clicked.connect(self.goHome) #run homing routine
        self.pauseButton.clicked.connect(self.pause) #pause machine
        self.resumeButton.clicked.connect(self.resume) #resume machine
        self.generateButton.clicked.connect(self.generateCoordinates) #generate coordinates
        self.coordinateSaveButton.clicked.connect(self.saveCoordinates) #export csv file
        self.exportButton.clicked.connect(self.saveRunData) #export csv file
        self.sensorDelaySpinBox.valueChanged.connect(self.sensorDelaySet) #adjust sensor dealy
        self.eStopButton.clicked.connect(self.eStop) #emergency stop
        self.stepsPerRevDropDown.currentIndexChanged.connect(self.changeStepScalar) # change scalar on the MCU
        self.speedSlider.valueChanged.connect(self.setSpeed)
        self.sensorReadingsSpinBox.valueChanged.connect(self.sensorReadingsSet)
        self.clearDataTable.clicked.connect(self.clearTablePreview)
        self.drawWordButton.clicked.connect(self.drawWord)
        self.twoDSpinBox.valueChanged.connect(self.newPlane)

    def drawWord(self): #expo fun

        #gather all data from GUI user entry

        self.mode = 'e'

        wordToDraw = str(self.nameEnterField.text())
        xMax = int(self.xMax.text())
        xMin = int(self.xMin.text())
        yMax = int(self.yMax.text())
        yMin = int(self.yMin.text())
        zMax = int(self.zMax.text())
        zMin = int(self.zMin.text())

        x_coordinates = []
        y_coordinates = []
        z_coordinates = []
        self.vx = []
        self.vy = []
        self.vz = []

        #kevin fun zone ************************************************************************************

        #set a baseline x velocity scaler (scaler of 4 equates to 6 kHz speed)
        v_x = 4
        v_y = 6

        zMin = 5
        zMax = 8
        x_len = 2
        
        #velocity ratio refers to v_z/v_x
        v_ratio = (zMax - zMin) / x_len
        
        #determine v_z based on v_x and v_ratio
        v_z = int(v_ratio * v_x)

        xMin = 2
        x_grid = 2.5
        
        total_chars = len(wordToDraw)
        char_index = 0
        yPress = 3.5
        yUnpress = 3
        
        
        for char in wordToDraw:
            
            if char == 'A' or char == 'a':
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #double velocity ratio
                x_coordinates.append(xMin + (char_index*x_grid) + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z))
                
                x_coordinates.append(xMin + (char_index*x_grid) + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z))
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index*x_grid) + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index*x_grid) + x_len / 4)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index*x_grid) + x_len / 4)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index*x_grid) + 3 * x_len / 4)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index*x_grid) + 3 * x_len / 4)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'B' or char == 'b':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + 2 * x_len / 3)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 5 * (zMax - zMin) / 6)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 4 * (zMax - zMin) / 6)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + 2 * x_len / 3)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 3 * (zMax - zMin) / 6)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 2 * (zMax - zMin) / 6)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 6)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + char_index*x_grid + 2 * x_len / 3)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + 2 * x_len / 3)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + 2 * x_len / 3)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'C' or char == 'c':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'D' or char == 'd':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #two-thirds standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 2 * (zMax - zMin) / 3)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z/3))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 3)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z/3))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z/3))
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                
            elif char == 'E' or char == 'e':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'F' or char == 'f':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 1 * (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                                                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'G' or char == 'g':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'H' or char == 'h':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'I' or char == 'i':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'J' or char == 'j':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)

            elif char == 'K' or char == 'k':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #half standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'L' or char == 'l':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'M' or char == 'm':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #1.5x standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(1.5*v_z))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(1.5*v_z))
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                
            elif char == 'N' or char == 'n':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'O' or char == 'o':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'P' or char == 'p':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'Q' or char == 'q':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin - (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin - (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'R' or char == 'r':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #half standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(int(2*v_x))
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'S' or char == 's':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'T' or char == 't':
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'U' or char == 'u':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'V' or char == 'v':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #double velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append((2*v_z))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(2*v_z))
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'W' or char == 'w':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                #1.5x velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + 3 * (zMax - zMin) / 4)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(1.5*v_z))
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(int(1.5*v_z))
                
                #return to standard velocity ratio
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'X' or char == 'x':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'Y' or char == 'y':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin + (zMax - zMin) / 2)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len / 2)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            elif char == 'Z' or char == 'z':
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMax)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yPress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
                x_coordinates.append(xMin + (char_index)*x_grid + x_len)
                y_coordinates.append(yUnpress)
                z_coordinates.append(zMin)
                self.vx.append(v_x)
                self.vy.append(v_y)
                self.vz.append(v_z)
                
            else:
                print ("Invalid character!")
                
            char_index = char_index + 1

        print(x_coordinates)
        print(y_coordinates)
        print(z_coordinates)
        print(self.vx)
        print(self.vy)
        print(self.vz)





        #kevin fun zone ************************************************************************************


        self.pointTable.setRowCount(0)

        for index in range(len(x_coordinates)):

            self.pointTable.insertRow(self.pointTable.rowCount()) #add a new row every time

            x_item = QTableWidgetItem()
            y_item = QTableWidgetItem()
            z_item = QTableWidgetItem()


            x_item.setText(str((x_coordinates[index]))) #kevin edit <--- this is where you put each x, y, z coordinate in (replace 'hi')
            y_item.setText(str((y_coordinates[index])))
            z_item.setText(str((z_coordinates[index])))

            self.pointTable.setItem(self.pointTable.rowCount()-1, 0, x_item) # add x coordinate to table
            self.pointTable.setItem(self.pointTable.rowCount()-1, 1, y_item) # add y coordinate to table
            self.pointTable.setItem(self.pointTable.rowCount()-1, 2, z_item) # add z coordinate to table

        self.runModeTab.setCurrentIndex(1) #switch to table tab
        self.entryNumber.setValue(int(self.pointTable.rowCount()))





    def clearTablePreview(self):
        self.outputTablePreview.setRowCount(0)
        self.dataOutputArray = []
        self.slicedData = []

    def setSpeed(self):
        pass
        try:
            sleep(.03)
            self.ser_port.write('a'.encode())
            sleep(.03)
            self.ser_port.write('v'.encode())
            sleep(.03)
            self.ser_port.write(str(self.speedSlider.value()).encode())
            sleep(.03)
            self.ser_port.write('a'.encode())
            self.ser_port.write('e'.encode())
        except Exception as e:
            print(e)

    # def setAcceleration(self):
    #     try:
    #         sleep(.03)
    #         self.ser_port.write('a'.encode())
    #         sleep(.03)
    #         self.ser_port.write('r'.encode())
    #         sleep(.03)
    #         self.ser_port.write(str(self.accelSlider.value()).encode())
    #         sleep(.03)
    #         self.ser_port.write('a'.encode())
    #         self.ser_port.write('e'.encode())
    #     except Exception as e:
    #         print(e)

    def updatePointTableSize(self): # set the number of rows in the  point table equal to the entry number spin box value

        value = self.entryNumber.value() # value in spin box
        dif = value - self.pointTable.rowCount() # difference between spin box and length of table


        if (dif > 0) or (self.pointTable.rowCount() == 0): # add rows if there are none or entry is larger than current
            for i in range(0, dif):

                self.pointTable.insertRow(self.pointTable.rowCount())

        elif (dif < 0): # take away rows if entry is smaller than current rows

            for i in range(0, -dif):

                self.pointTable.removeRow(self.pointTable.rowCount()-1)
        else:
            pass

    def eStop(self):
        self.xStop()
        self.yStop()
        self.zStop()


    def changeStepScalar(self): #change the microstep scalar whenever the value is cahgned on the GUI
        try:
            self.ser_port.write('a'.encode())
            self.ser_port.write('u'.encode())
            str(int(self.sensorDelaySpinBox.value())/200).encode()
            self.ser_port.write('a'.encode())
            self.ser_port.write('e'.encode())
        except:
            print('serial not open')

    def systemUnitsToSteps(self, system_coor, axis = None): #take outgoing units and convert to equivalent steps
        steps = int(system_coor*3.165/self.unitsConversionFactor*int(self.stepsPerRevDropDown.currentText()))

        if axis != None: #if in step/incremental mode
            if axis == 'x':
                xLocInSteps = int(self.machineCoordinates[0]*3.165/self.unitsConversionFactor*int(self.stepsPerRevDropDown.currentText()))
                steps = xLocInSteps + steps

            elif axis == 'y':
                yLocInSteps = int(self.machineCoordinates[1]*3.165/self.unitsConversionFactor*int(self.stepsPerRevDropDown.currentText()))
                steps = yLocInSteps + steps

            elif axis == 'z':
                zLocInSteps = int(self.machineCoordinates[2]*3.165/self.unitsConversionFactor*int(self.stepsPerRevDropDown.currentText()))
                steps = zLocInSteps + steps

        return int(steps) #else just send straight to absoulte coordinte

    def systemUnitsFromSteps(self, mach_steps): #take incoming steps and convert to equivalent user coordinates in IN
        system_coor = float(self.unitsConversionFactor*mach_steps/(3.165*int(self.stepsPerRevDropDown.currentText())))
        return system_coor

    def manualGo(self, axis, direction): # axis-"x", "y" or "z", direction = "f", "b"

        if(self.controlTypeDropDown.currentText() == "Incremental"): #incremental mode

            if direction == "f": #change into usable int values
                direction = 1
            elif direction == "r":
                direction = -1

            stepDistance = self.stepSpinBox.value()*direction

            if axis == 'x':
                xDistance = stepDistance
                yDistance = 0
                zDistance = 0

            elif axis == 'y':
                xDistance = 0
                yDistance = stepDistance
                zDistance = 0

            elif axis == 'z':
                xDistance = 0
                yDistance = 0
                zDistance = stepDistance

            print(str(xDistance)+' '+str(yDistance)+' '+str(zDistance))

            try:

                self.ser_port.write('i'.encode())  # send control + C for routine mode
                self.ser_port.write('x'.encode()) # send a control x
                sleep(.03)
                self.ser_port.write(str(self.systemUnitsToSteps(xDistance, 'x')).encode('utf-8')) # send x coordinate step
                sleep(.03)
                self.ser_port.write('a'.encode()) # send an enter

                self.ser_port.write('i'.encode())  # send control + C for routine mode
                self.ser_port.write('y'.encode()) # send a control x
                sleep(.03)
                self.ser_port.write(str(self.systemUnitsToSteps(yDistance, 'y')).encode('utf-8')) # send x coordinate step
                sleep(.03)
                self.ser_port.write('a'.encode()) # send an enter

                self.ser_port.write('i'.encode())  # send control + C for routine mode
                self.ser_port.write('z'.encode()) # send a control x
                sleep(.03)
                self.ser_port.write(str(self.systemUnitsToSteps(zDistance, 'z')).encode('utf-8')) # send x coordinate step
                sleep(.03)
                self.ser_port.write('a'.encode()) # send an enter
                self.ser_port.write('e'.encode())  # send control + e for end

            except Exception as e:
                print("Serial not open")
                print(str(e))

        else: #else continous mode
            try:
                sleep(.05)
                self.ser_port.write('d'.encode())
                sleep(.05)
                self.ser_port.write(axis.encode())
                #sleep(.2)
                self.ser_port.write(direction.encode())
                #sleep(.2)
                self.ser_port.write('e'.encode())
                #sleep(.2)
            except:
                print('serial not open')

    def xPlus(self): # xplus button pressed
        self.manualGo("x", "f")

    def yPlus(self): # yplus button pressed
        self.manualGo("y", "f")

    def zPlus(self): # zplus button pressed
        self.manualGo("z", "f")

    def xMinus(self): # xminus button pressed
        self.manualGo("x", "r")

    def yMinus(self): # yminus button pressed
        self.manualGo("y", "r")

    def zMinus(self): # zminus button pressed
        self.manualGo("z", "r")

    def stop(self, axis): #axis = "x", "y", "z"
        try:
            sleep(.05)
            self.ser_port.write('d'.encode())
            sleep(.05)
            self.ser_port.write(axis.encode())
            self.ser_port.write('s'.encode())
            self.ser_port.write('e'.encode())
        except:
            print('serial not open')

    def xStop(self): # xstop button pressed
        self.stop("x")

    def yStop(self): # ystop button pressed
        self.stop("y")

    def zStop(self): # zstop button pressed
        self.stop("z")

    def reset(self): # reset button pressed
        try:
            self.ser_port.write('e'.encode())
            sleep(.03)
            self.ser_port.write('r'.encode())
            self.coordinateData = [] # stores all x, y, z data from csv file as 3 X N matrix
            self.userOffset = [0,0,0,1,1,1] #clear user offset
            self.motor_temp1 = '---' # properties for temperatures
            self.motor_temp2 = '---'
            self.motor_temp3 = '---'
            self.motor_temp4 = '---'
            self.motor_temp5 = '---'
            self.arm_temp = '---'
            self.frame_temp = '---'
            self.water_temp = '---'
            self.heat_flux = '---'
            self.dataOutputArray = [] # output data with x,y,x, heatflux
            #self.threeDDataDisplay = [[0], [0], [0]] # identical to above just in addition to the coordinate of the current sensor location (x,y,z)
            self.slicedData = []
            self.outputTablePreview.setRowCount(0)
            self.changeButtonColor(self.xStopButton, 'red')
            self.changeButtonColor(self.yStopButton, 'red')
            self.changeButtonColor(self.zStopButton, 'red')
            self.changeButtonColor(self.xPlusButton, 'light grey')
            self.changeButtonColor(self.xMinusButton, 'light grey')
            self.changeButtonColor(self.yPlusButton, 'light grey')
            self.changeButtonColor(self.yMinusButton, 'light grey')
            self.changeButtonColor(self.zPlusButton, 'light grey')
            self.changeButtonColor(self.zMinusButton, 'light grey')
            self.changeButtonColor(self.eStopButton, 'light grey')
            self.changeButtonColor(self.pauseButton, 'light grey')
            self.changeButtonColor(self.resumeButton, 'light grey')

            #self.setAcceleration()
            self.setSpeed()
            #self.sensorReadingsSet()
            #self.sensorDelaySet()

            self.systemIsRunningCalibration = False
            self.mode = 'c'
            self.timer_start = 0
            self.system_time = 0

        except Exception as e:
            print("Serial not open")
            print(str(e))

    def pause(self): # pause button pressed
        if self.systemIsPaused == False:
            try:
                self.ser_port.write('p'.encode())
                self.systemIsPaused = True
                self.changeButtonColor(self.pauseButton, 'red')
            except:
                print('serial not open')

    def resume(self): # resume button pressed
        if self.systemIsPaused:
            try:
                self.ser_port.write('p'.encode())
                self.systemIsPaused = False
                self.changeButtonColor(self.pauseButton, 'light grey')
            except:
                print('serial not open')

    def sensorDelaySet(self): #set the delay time between reading the sensor and dataoutput
        try:
            return
            self.ser_port.write('a'.encode())
            self.ser_port.write('s'.encode())
            self.ser_port.write(str(self.sensorDelaySpinBox.value()).encode())
            self.ser_port.write('a'.encode())
            self.ser_port.write('e'.encode())
        except:
            print('serial not open')

    def sensorReadingsSet(self): #set the number of samples we wish to take from the sensor and average per each node
        try:
            self.ser_port.write('a'.encode())
            self.ser_port.write('n'.encode()) #edit this
            self.ser_port.write(str(self.sensorReadingsSpinBox.value()).encode())
            self.ser_port.write('a'.encode())
            self.ser_port.write('e'.encode())
        except:
            print('serial not open')


    def refreshDirectoryFiles(self):
        '''refresh file list in drop down menu that can be imported to program'''
        self.fileSelectDropDown.clear()
        os.chdir(os.getcwd())
        for file in glob.glob("*.csv"):
            self.fileSelectDropDown.addItem(str(file))

    def changeButtonColor(self, button, color): # Changes a button's color, @Param: (self, self.buttonName, 'color')
        palette = button.palette()
        role = button.backgroundRole() #choose whatever you like
        palette.setColor(role, QtGui.QColor(color))
        button.setPalette(palette)
        button.setAutoFillBackground(True)


    def setupSerial(self):
        '''Initialize the serial port before everything else'''

        if(self.ser_port == None): #ser_port initial setup

            try: # try to connect to specified serial port from drop down menu
            # Initialize the serial port before everything else
                self.ser_port = serial.Serial (self.serialDropDown.currentText(), 115200, timeout = 0.2)
                self.ser_port.close() # default close port to protect from errors if port was left open
                self.ser_port.open()
                print("Connecting")
                print(self.ser_port.is_open)
                '''Change the color of the connect button to green when the serial connects'''
                self.changeButtonColor(self.connectButton, 'green')

            except Exception as e:
                print("Failed to connect to device")
                print(str(e))

        elif(self.ser_port.is_open == False): # if program is running, but ser_port has been physically disconnected, reconnect

            try: # try to connect to specified serial port from drop down menu
                self.ser_port = serial.Serial (self.serialDropDown.currentText(), 115200, timeout = 0.2)
                self.ser_port.open()
                print("Connecting")
                print(self.ser_port.is_open)
                '''Change the color of the connect button to green when the serial connects'''
                self.changeButtonColor(self.connectButton, 'green')


            except Exception as e:
                print("Failed to reconnect to Mr Devicey device")
                print(str(e))

        else: # if the serial port is already open, close it
            print("Disconnecting serial")
            self.ser_port.close()
            '''Change the color of the connect button back to grey when the serial disconnects'''
            palette = self.connectButton.palette()
            self.changeButtonColor(self.connectButton, 'grey')
            print(self.ser_port.is_open)
            self.ser_port = None


    def refreshSerial(self):
        '''refresh serial port device availible list for user to select from'''
        try:
            self.serialDropDown.clear()
            list_of_avail_ports = (list(serial.tools.list_ports.comports()))
            list_of_avail_ports.reverse()
            for port in list_of_avail_ports:
                #self.serialDropDown.addItem(str(port).replace(' - n/a', ''))
                self.serialDropDown.addItem(str(port)[:(str(port).find(' '))]) # remove extra stuff in port name string
        except:
            pass

    def saveCoordinates (self):
        '''saves only coordinates to csv by calling exportCSVfile'''
        self.exportCsvFile(self.pointTable, self.coorNameLineEdit)

    def saveRunData (self):
        '''saves heatflux and coordinates to csv by calling exportCSVfile'''
        self.exportCsvFile(self.outputTablePreview, self.dataNameLineEdit)

    def exportCsvFile(self, dataTable, lineEditInput): #parameter of QWidgetTable
        '''saves a QwidgetTable to a csv file using the csv module'''
        if lineEditInput.text() == "":
            return

        with open(lineEditInput.text()+".csv", 'w') as myfile:
            wr = csv.writer(myfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for r in range(dataTable.rowCount()):
                try:
                    row = []
                    for c in range(dataTable.columnCount()):
                        row .append(str(dataTable.item(r,c).text())) # get values from table row
                    wr.writerow(row)
                except:
                    pass


    def importCsvFile(self):
        '''import a csv coordinate file from the current operating directory'''
        self.pointTable.setRowCount(0)

        with open (self.fileSelectDropDown.currentText(), 'r') as csvDataInput:
            lines = csvDataInput.readlines()

        for line in lines:
            split_str = line.split(',')  # seperate line entries into three lists

            try:
                 x = float(split_str[0])
                 y = float(split_str[1])
                 z = float(split_str[2])

            except (IndexError, ValueError, TypeError):  # ignore invalid entries
                pass
            else:
                z_item = QTableWidgetItem()
                z_item.setText(str(z))
                x_item = QTableWidgetItem()
                x_item.setText(str(x))
                y_item = QTableWidgetItem()
                y_item.setText(str(y))

                self.pointTable.insertRow(self.pointTable.rowCount()) #add a new row every time
                self.pointTable.setItem(self.pointTable.rowCount()-1, 0, x_item)              # add x coordinate
                self.pointTable.setItem(self.pointTable.rowCount()-1, 1, y_item)              # add y coordinate
                self.pointTable.setItem(self.pointTable.rowCount()-1, 2, z_item)              # add z coordinate


        self.runModeTab.setCurrentIndex(1) #switch to table tab
        self.entryNumber.setValue(int(self.pointTable.rowCount()))

    def generateCoordinates(self):
        '''Coordinates generated by the user'''

        self.pointTable.setRowCount(0)

        try:
            xRange = int(self.xMax.text())-int(self.xMin.text()) #get data range for each axis
            yRange = int(self.yMax.text())-int(self.yMin.text())
            zRange = int(self.zMax.text())-int(self.zMin.text())

            xMin = int(self.xMin.text()) #get minimum for each axis
            yMin = int(self.yMin.text())
            zMin = int(self.zMin.text())

            xInc = xRange/(int(self.xReadings.text())-1) #get space in between each data point
            yInc = yRange/(int(self.yReadings.text())-1)
            zInc = zRange/(int(self.zReadings.text())-1)


            for j in range (int(self.yReadings.text())): #make 3D field of coordinate points


                for k in range (int(self.zReadings.text())):


                    for i in range (int(self.xReadings.text())):

                        self.pointTable.insertRow(self.pointTable.rowCount()) #add a new row every time

                        x_item = QTableWidgetItem()
                        y_item = QTableWidgetItem()
                        z_item = QTableWidgetItem()

                        x_item.setText(str((xMin+xInc*i)))
                        y_item.setText(str((yMin+yInc*j)))
                        z_item.setText(str((zMin+zInc*k)))

                        self.pointTable.setItem(self.pointTable.rowCount()-1, 0, x_item)              # add x coordinate
                        self.pointTable.setItem(self.pointTable.rowCount()-1, 1, y_item)              # add y coordinate
                        self.pointTable.setItem(self.pointTable.rowCount()-1, 2, z_item)              # add z coordinate

        except Exception as e:
            print(str(e))

        self.runModeTab.setCurrentIndex(1) #switch to table tab
        self.entryNumber.setValue(int(self.pointTable.rowCount()))

    def goToTableCoordinates(self):
        '''go to specified positions using entered coordinates from table and original serial
        commands from the kev master, subject to change, updated to send steps'''

        if(self.ser_port != None): # check to make sure we made a serial port

            if self.ser_port.is_open: # check to make sure serial port is connected and open
                self.coordinateData.clear()
                for i in range(0, self.pointTable.rowCount()): # print all values out over serial

                    try: # get data from table, if row is empty then skip it

                        x = float(self.pointTable.item(i,0).text()) # get values from table row
                        y = float(self.pointTable.item(i,1).text())
                        z = float(self.pointTable.item(i,2).text())


                        if(self.coorSysDropDown.currentIndex()==0): #user coordinates

                            x = x + self.userOffset[0]
                            y = y + self.userOffset[1]
                            z = z + self.userOffset[2]


                        x = self.systemUnitsToSteps(x) #convert system units (i.e. in/mm/m/cm to machine steps)
                        z = self.systemUnitsToSteps(z)
                        y = self.systemUnitsToSteps(y)


                        self.coordinateData.append([x,y,z])

                    except Exception as e:
                        #print(e)
                        pass



                self.sendCoordinatesSerial(self.coordinateData)
                #print(self.coordinateData)

            else:
                print("Serial was disconnected")
        else:
            print("Serial not connected")

    def sendCoordinatesSerial(self, coordinates):
        if self.mode == 'e':
            self.sendVelocitiesSerial()
        self.ser_port.write(self.mode.encode())  # send control + C for coordinate mode or E for drawing mode
        sleep(.03)
        self.ser_port.write('x'.encode()) # send a control x
        sleep(.03)
        for i in range(len(self.coordinateData)): #iterate over every element in coordinate data
            if i >= (len(self.coordinateData)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.coordinateData[i][0]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.coordinateData[i][0]) + ",").encode('utf-8'))
            sleep(.01)
        sleep(.1)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.01)
        self.ser_port.write('y'.encode()) # send a control y
        for i in range(len(self.coordinateData)): #iterate over every element in coordinate data
            if i >= (len(self.coordinateData)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.coordinateData[i][1]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.coordinateData[i][1]) + ",").encode('utf-8'))
            sleep(.01)
        sleep(.05)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.03)
        self.ser_port.write('z'.encode()) # send a control z
        for i in range(len(self.coordinateData)): #iterate over every element in coordinate data
            if i >= (len(self.coordinateData)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.coordinateData[i][2]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.coordinateData[i][2]) + ",").encode('utf-8'))
            sleep(.01)
        sleep(.03)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.03)
        self.ser_port.write('e'.encode())  # send control + C for routine mode


        self.runModeTab.setCurrentIndex(0) #switch back to manual control tab
        self.systemIsRunningCalibration = True
        self.timer_start = self.system_time


    def sendVelocitiesSerial(self):

        self.ser_port.write('a'.encode())  # send "a" for configuration mode
        sleep(.03)
        self.ser_port.write('x'.encode()) # send a control x
        sleep(.03)
        for i in range(len(self.vx)): #iterate over every element in coordinate data
            if i >= (len(self.vx)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.vx[i]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.vx[i]) + ",").encode('utf-8'))
            sleep(.02)
        sleep(.1)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.01)
        self.ser_port.write('y'.encode()) # send a control y
        for i in range(len(self.vy)): #iterate over every element in coordinate data
            if i >= (len(self.vy)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.vy[i]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.vy[i]) + ",").encode('utf-8'))
            sleep(.02)
        sleep(.03)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.03)
        self.ser_port.write('z'.encode()) # send a control z
        for i in range(len(self.vz)): #iterate over every element in coordinate data
            if i >= (len(self.vz)-1): #last coordinate set don't add commna
                self.ser_port.write(str(self.vz[i]).encode('utf-8'))
            else: #regular coordinate set
                self.ser_port.write((str(self.vz[i]) + ",").encode('utf-8'))
            sleep(.02)
        sleep(.03)
        self.ser_port.write('a'.encode()) # send an enter
        sleep(.01)
        self.ser_port.write('e'.encode())  # send control + C for routine mode


    def readSerPort(self):
        try:
            if(self.ser_port != None):
                if(self.ser_port.is_open and self.ser_port.in_waiting):
                    data = (self.ser_port.readline()).decode ('UTF-8')
                    if data[:3] == 'm1t': # read incoming serial traffic for readout updates and put into system property
                        split_line = data.split('t')
                        self.motor_temp1 = split_line[1]
                    elif data[:3] == 'm2t':
                        split_line = data.split('t')
                        self.motor_temp2 = split_line[1]
                    elif data[:3] == 'm3t':
                        split_line = data.split('t')
                        self.motor_temp3 = split_line[1]
                    elif data[:3] == 'm4t':
                        split_line = data.split('t')
                        self.motor_temp4 = split_line[1]
                    elif data[:3] == 'm5t':
                        split_line = data.split('t')
                        self.motor_temp5 = split_line[1]
                    elif data[:3] == 'art':
                        split_line = data.split('t')
                        self.arm_temp = split_line[1]
                    elif data[:3] == 'frt':
                        split_line = data.split('t')
                        self.frame_temp = split_line[1]
                    elif data[:3] == 'wat':
                        split_line = data.split('t')
                        self.water_temp = split_line[1]
                    elif data[:3] == 'HF:':
                        data = str(data)
                        data.replace('\r\n', '')
                        split_line = re.split(':|e', data)
                        num = float(split_line[1])
                        e = int(split_line[2])
                        self.heat_flux =float('%.4f'%(num*(math.pow(10, e))))
                        self.storeOutputData() # this method runs whenever we receive a heatflux reading and stores x,y,x, hf to dataOutputArray
                        self.serWindowPrint(data) #remove after testing
                    elif data[:7] == 'MDXloc:':
                        data = str(data)
                        #split_line = re.split(':|E|\r', data)
                        #num = float(split_line[1])
                        #e = int(split_line[2])
                        #self.machineCoordinates[0] =float('%.2f'%(num*(math.pow(10, e))))
                        split_line = re.split(':|\r', data)
                        num = int(split_line[1])
                        self.machineCoordinates[0] = self.systemUnitsFromSteps(num) #convert steps to units
                    elif data[:7] == 'MDYloc:':
                        data = str(data)
                        # split_line = re.split(':|E|\r', data)
                        # num = float(split_line[1])
                        # e = int(split_line[2])
                        # self.machineCoordinates[1] =float('%.2f'%(num*(math.pow(10, e))))
                        split_line = re.split(':|\r', data)
                        num = int(split_line[1])
                        self.machineCoordinates[1] = self.systemUnitsFromSteps(num) #convert steps to units
                    elif data[:7] == 'MDZloc:':
                        data = str(data)
                        # split_line = re.split(':|E|\r', data)
                        # num = float(split_line[1])
                        # e = int(split_line[2])
                        # self.machineCoordinates[2] =float('%.2f'%(num*(math.pow(10, e))))
                        split_line = re.split(':|\r', data)
                        num = int(split_line[1])
                        self.machineCoordinates[2] = self.systemUnitsFromSteps(num) #convert steps to units

                    elif data[:2] == '!C':
                       self.systemIsRunningCalibration == False
                       self.progressUpdate(True) #clear progress stats

                    elif data[:4] == 'MDXF':
                        self.changeButtonColor(self.xPlusButton, 'green')
                        self.changeButtonColor(self.xMinusButton, 'light grey')
                        self.changeButtonColor(self.xStopButton, 'light grey')
                    elif data[:4] == 'MDXR':
                        self.changeButtonColor(self.xPlusButton, 'light grey')
                        self.changeButtonColor(self.xMinusButton, 'green')
                        self.changeButtonColor(self.xStopButton, 'light grey')
                    elif data[:4] == 'MDXS':
                        self.changeButtonColor(self.xPlusButton, 'light grey')
                        self.changeButtonColor(self.xMinusButton, 'light grey')
                        self.changeButtonColor(self.xStopButton, 'red')
                    elif data[:4] == 'MDYF':
                        self.changeButtonColor(self.yPlusButton, 'green')
                        self.changeButtonColor(self.yMinusButton, 'light grey')
                        self.changeButtonColor(self.yStopButton, 'light grey')
                    elif data[:4] == 'MDYR':
                        self.changeButtonColor(self.yPlusButton, 'light grey')
                        self.changeButtonColor(self.yMinusButton, 'green')
                        self.changeButtonColor(self.yStopButton, 'light grey')
                    elif data[:4] == 'MDYS':
                        self.changeButtonColor(self.yPlusButton, 'light grey')
                        self.changeButtonColor(self.yMinusButton, 'light grey')
                        self.changeButtonColor(self.yStopButton, 'red')
                    elif data[:4] == 'MDZF':
                        self.changeButtonColor(self.zPlusButton, 'green')
                        self.changeButtonColor(self.zMinusButton, 'light grey')
                        self.changeButtonColor(self.zStopButton, 'light grey')
                    elif data[:4] == 'MDZR':
                        self.changeButtonColor(self.zPlusButton, 'light grey')
                        self.changeButtonColor(self.zMinusButton, 'green')
                        self.changeButtonColor(self.zStopButton, 'light grey')
                    elif data[:4] == 'MDZS':
                        self.changeButtonColor(self.zPlusButton, 'light grey')
                        self.changeButtonColor(self.zMinusButton, 'light grey')
                        self.changeButtonColor(self.zStopButton, 'red')
                    else: # print to serial window if not a readout update
                        self.serWindowPrint(data)
            else:
                pass
        except Exception as e:
            print(e)
            print('Serial Error')
            #self.ser_port.close()
            #self.ser_port = None


    def serWindowPrint(self, message): # print serial coms out to window monitor
        self.plainTextEdit.appendPlainText(str(message))

    def updateReadouts(self): # update readouts such as coordinate location, temperature, time and heat flux on the UI

        self.system_time +=1

        self.xMach.display(str(self.machineCoordinates[0])) # machine coordinates
        self.yMach.display(str(self.machineCoordinates[1]))
        self.zMach.display(str(self.machineCoordinates[2]))
        self.xUser.display(str(((self.machineCoordinates[0] - self.userOffset[0]))*self.userOffset[3])) # user coordinates = machine coordinates - offest dist * flipped (either a 1 or -1)
        self.yUser.display(str(((self.machineCoordinates[1]- self.userOffset[1]))*self.userOffset[4]))
        self.zUser.display(str(((self.machineCoordinates[2] - self.userOffset[2]))*self.userOffset[5]))

        self.m1Temp.display(self.motor_temp1)
        self.m2Temp.display(self.motor_temp2)
        self.m3Temp.display(self.motor_temp3)
        self.m4Temp.display(self.motor_temp4)
        self.m5Temp.display(self.motor_temp5)
        self.t1Temp.display(self.water_temp)
        self.t2Temp.display(self.arm_temp)
        self.t3Temp.display(self.frame_temp)
        self.t4Temp.display(self.water_temp)
        self.t5Temp.display(self.frame_temp)
        self.heatFlux.display(str(self.heat_flux))

        #self.threeDDataDisplay = [x * conFac for x in self.machineCoordinates] #insert current machine coordinate into data to send to 3D plot
        #self.twoDDataDisplay = [self.threeDDataDisplay[0], self.threeDDataDisplay[1]]# insert current machine coordinate into data to send to 2D plot

        if(self.systemIsRunningCalibration):
            self.progressUpdate()

    def progressUpdate(self, clear = False):

        if clear:
            self.progressBar.setValue(100) # update progress bar
            self.totalNodes.display('0') # how many nodes for this run
            self.nodesLeft.display('0') #remaining nodes
            self.timeRemaining.display('0')

        else: #still running
            self.progressBar.setValue(len(self.dataOutputArray)/(len(self.coordinateData)+.001)) # update progress bar
            self.totalNodes.display(str(len(self.coordinateData))) # how many nodes for this run
            self.nodesLeft.display(str(len(self.coordinateData)-len(self.dataOutputArray))) #remaining nodes
            self.timeRemaining.display(str(len(self.coordinateData)-len(self.dataOutputArray)*.1))


    def updateGraphs(self): #update graphs only when on the associated tab and table always
        if(self.dataTab.currentIndex() == 0):
            self.plot_3Ddata()
        elif(self.dataTab.currentIndex() == 1):
            self.plot_2Ddata()
        self.updateDataTable()

    def plot_3Ddata(self): #plot realtime data on 3d plot

        if(self.threeDScat != None):
            self.threeDScat.remove()
        if(self.positionTrack != None):
         self.positionTrack.remove()

        self.positionTrack = self.threeDPlot.canvas.ax.scatter(self.machineCoordinates[0],self.machineCoordinates[1],self.machineCoordinates[2], c=['black'], alpha=0.5)
        try:
            list1 = [(item[0]+self.userOffset[0])*self.userOffset[3]  for item in self.dataOutputArray] #xcoordinates
            list2 = [(item[1]+self.userOffset[1])*self.userOffset[4]  for item in self.dataOutputArray] #ycoordinates
            list3 = [(item[2]+self.userOffset[2])*self.userOffset[5]  for item in self.dataOutputArray] #zcoordinates
            list4 = [(item[3]) for item in self.dataOutputArray] #heat flux
            self.threeDScat = self.threeDPlot.canvas.ax.scatter(list1,list2,list3, c=list4, cmap = 'jet', alpha=0.15, depthshade = True)
        except:
            pass
        self.threeDPlot.canvas.draw_idle()
        #self.threeDPlot.canvas.ax.colorbar()

    def plot_2Ddata(self): #plot realtime 2d Plane of data
        if(self.twoDScat!= None):
            self.twoDScat.remove()
        if self.slicedData != None and len(self.slicedData) != 0:
            try:
                plane = self.slicedData[self.twoDSpinBox.value()]
                x_points = [(point[0]+self.userOffset[0])*self.userOffset[3] for point in plane]
                z_points = [(point[1]+self.userOffset[2])*self.userOffset[5]  for point in plane]
                self.twoDScat = self.twoDPlot.canvas.ax.scatter(x_points, z_points, c=['jet'], alpha=0.15)
                self.twoDPlot.canvas.draw_idle()
            except Exception as e:
                print(e)
                pass
    def newPlane(self): #only for testing spin box if needed
        #self.twoDScat.remove()
        pass

    def updateDataTable(self): #put data into table under real time data veiwer tab
        i = self.outputTablePreview.rowCount()
        if(i < len(self.dataOutputArray)): # if there is data to add

            self.outputTablePreview.insertRow(i) #add a new row every time ********************************************************

            h_item = QTableWidgetItem()
            h_item.setText(str(self.dataOutputArray[i][3]))
            self.outputTablePreview.setItem(i, 0, h_item)              # add hf data
            x_item = QTableWidgetItem()
            x_item.setText(str(round(self.dataOutputArray[i][0],2)))
            self.outputTablePreview.setItem(i, 1, x_item)              # add x coordinate
            y_item = QTableWidgetItem()
            y_item.setText(str(round(self.dataOutputArray[i][1],2)))
            self.outputTablePreview.setItem(i, 2, y_item)              # add y coordinate
            z_item = QTableWidgetItem()
            z_item.setText(str(round(self.dataOutputArray[i][2],2)))
            self.outputTablePreview.setItem(i, 3, z_item)
            t_item = QTableWidgetItem()             # add z coordinate
            t_item.setText(str(self.dataOutputArray[i][4]))
            self.outputTablePreview.setItem(i, 4, t_item)              # add z coordinate


    def unitsChange(self): #update units of whole system when then the units drop down is changed
        unitString = self.unitsDropDown.currentText()
        if(unitString=='in'): #inches, default of the system
            self.unitsConversionFactor = 1
        elif(unitString=='mm'): #mm
            self.unitsConversionFactor = 25.4
        elif(unitString=='cm'): #cm
            self.unitsConversionFactor = 2.54
        elif(unitString=='m'): #m
            self.unitsConversionFactor = .0254
        self.changeGraphUnits(unitString)

    def requestHeatFlux(self):
        try:
            sleep(.05)
            self.ser_port.write('s'.encode())
        except:
                print('serial not open')
    def setUserOffset(self): #change the user axis offset direction from checkboxes

        if(self.flipX.isChecked()):
            self.userOffset[3] = -1
        elif(self.flipX.isChecked()==False):
            self.userOffset[3] = 1
        if(self.flipY.isChecked()):
            self.userOffset[4] = -1
        elif(self.flipY.isChecked()==False):
            self.userOffset[4] = 1
        if(self.flipZ.isChecked()):
            self.userOffset[5] = -1
        elif(self.flipZ.isChecked()==False):
            self.userOffset[5] = 1

    def zeroXOffset(self): #zero user offset from machine coordinates
        self.userOffset[0] = self.machineCoordinates[0]

    def zeroYOffset(self):
        self.userOffset[1] = self.machineCoordinates[1]

    def zeroZOffset(self):
        self.userOffset[2] = self.machineCoordinates[2]

        #update tables
    def changeGraphUnits(self, units): #change the unit base on graphs

        self.threeDPlot.canvas.ax.set_xlabel('X (' + units+ ')')
        self.threeDPlot.canvas.ax.set_ylabel('Y (' + units+ ')')
        self.threeDPlot.canvas.ax.set_zlabel('Z (' + units+ ')')
        self.threeDPlot.canvas.ax.set_xlim(0,36*self.unitsConversionFactor)
        self.threeDPlot.canvas.ax.set_ylim(0,36*self.unitsConversionFactor)
        self.threeDPlot.canvas.ax.set_zlim(0,36*self.unitsConversionFactor)

        self.twoDPlot.canvas.ax.set_xlabel('X (' + units+ ')')
        self.twoDPlot.canvas.ax.set_ylabel('Y (' + units+ ')')
        self.twoDPlot.canvas.ax.set_xlim(0,36*self.unitsConversionFactor)
        self.twoDPlot.canvas.ax.set_ylim(0,36*self.unitsConversionFactor)


    def homeRoutine(self): #run home routine to set machine home, will add option for dual or single limit switch homing
        self.xMinus()
        self.yMinus()
        self.zMinus()

    def goHome(self): #go to home, edit this to use manual go

        if(self.userRadio.isChecked): #user home
            xdata = ((self.machineCoordinates[0] - self.userOffset[0]))*self.userOffset[3]
            ydata = ((self.machineCoordinates[1] - self.userOffset[1]))*self.userOffset[4]
            zdata = ((self.machineCoordinates[2] - self.userOffset[2]))*self.userOffset[5]

            xdata = str(self.systemUnitsToSteps(xdata))
            ydata = str(self.systemUnitsToSteps(ydata))
            zdata = str(self.systemUnitsToSteps(zdata))

        else: #machine home
            xdata = str('0')
            ydata = str('0')
            zdata = str('0')
        try:
            self.ser_port.write('c'.encode())  # send control + R for routine mode
            self.ser_port.write('x'.encode()) # send a control x
            sleep(.03)
            self.ser_port.write(str(xdata).encode('utf-8')) # send x coordinate
            sleep(.03)
            self.ser_port.write('a'.encode()) # send an enter
            self.ser_port.write('y'.encode()) # send a control y
            sleep(.03)
            self.ser_port.write(str(ydata).encode('utf-8')) # send y coordinate
            sleep(.03)
            self.ser_port.write('a'.encode()) # send an enter
            self.ser_port.write('z'.encode()) # send a control z
            sleep(.03)
            self.ser_port.write(str(zdata).encode('utf-8')) # send z coordinate
            sleep(.03)
            self.ser_port.write('a'.encode()) # send an enter
            self.ser_port.write('e'.encode())  # send control + R for routine mode
        except:
            pass


    def storeOutputData(self):
        x = ((self.machineCoordinates[0] - self.userOffset[0]))*self.userOffset[3]
        y = ((self.machineCoordinates[1] - self.userOffset[1]))*self.userOffset[4]
        z = ((self.machineCoordinates[2] - self.userOffset[2]))*self.userOffset[5]
        h = str(self.heat_flux)
        t = (self.system_time - self.timer_start)/10
        self.dataOutputArray.append([x, y, z, h, t])
        self.updateSlicedData()

    def updateSlicedData(self):
        data_point = self.dataOutputArray[len(self.dataOutputArray)-1] #latest data point
        for plane in self.slicedData: #look through each plane list in sliced data
            if data_point[1] >= plane[0][1] - .25 and data_point[1] <= plane[0][1] +.25: #if there's already a plane (y = y of plane)
                plane.append([data_point[0],data_point[2]]) #Add x and y point to plane
                print(self.slicedData)
                return

        newPlane = []
        newPlane.append([data_point[0],data_point[2]]) #Add x and y to new plane
        self.slicedData.append(newPlane) # else add new plane
        self.twoDSpinBox.setMaximum(len(self.slicedData)-1)


    def statusUpdate(self): #updates files and connection status
        self.refreshDirectoryFiles()
        #self.refreshSerial()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Install the event filter that will be used later to detect key presses
        QtWidgets.qApp.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if not event.isAutoRepeat() and self.ui.keyboardCheck.isChecked():
                if event.key() == QtCore.Qt.Key_Left and self.ui.runModeTab.currentIndex()==0:
                    self.ui.xMinus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Right and self.ui.runModeTab.currentIndex()==0:
                    self.ui.xPlus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Up and self.ui.runModeTab.currentIndex()==0:
                    self.ui.yPlus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Down and self.ui.runModeTab.currentIndex()==0:
                    self.ui.yMinus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Z and self.ui.runModeTab.currentIndex()==0:
                    self.ui.zPlus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_X and self.ui.runModeTab.currentIndex()==0:
                    self.ui.zMinus()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Space and self.ui.runModeTab.currentIndex()==0:
                    self.ui.requestHeatFlux()
                    #event.accept()
                    return 1
                elif event.key() == QtCore.Qt.Key_Escape:
                    self.close()
                    #event.accept()
                    return 1
                else:
                    #event.ignore()
                    return 0

        if event.type() == QtCore.QEvent.KeyRelease and self.ui.keyboardCheck.isChecked():
            if event.key() == QtCore.Qt.Key_Left and self.ui.runModeTab.currentIndex()==0:
                self.ui.xStop()
                #event.accept()
                return 1
            elif event.key() == QtCore.Qt.Key_Right and self.ui.runModeTab.currentIndex()==0:
                self.ui.xStop()
                #event.accept()
                return 1
            elif event.key() == QtCore.Qt.Key_Up and self.ui.runModeTab.currentIndex()==0:
                self.ui.yStop()
                #event.accept()
                return 1
            elif event.key() == QtCore.Qt.Key_Down and self.ui.runModeTab.currentIndex()==0:
                self.ui.yStop()
                #event.accept()
                return 1
            elif event.key() == QtCore.Qt.Key_Z and self.ui.runModeTab.currentIndex()==0:
                self.ui.zStop()
                #event.accept()
                return 1
            elif event.key() == QtCore.Qt.Key_X and self.ui.runModeTab.currentIndex()==0:
                self.ui.zStop()
                #event.accept()
                return 1
            else:
                #event.ignore()
                return 0

        return super().eventFilter(obj, event)


if __name__ == '__main__':
    '''main of the GUI, make new UI window, start event loop, make timers, and define exit when done'''

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()


    serial_timer = QtCore.QTimer() # set up timer to read serial port incoming traffic when not busy
    serial_timer.timeout.connect(window.ui.readSerPort)
    serial_timer.start(10)

    ui_update_timer = QtCore.QTimer() # set up timer to update the readouts on the ui
    ui_update_timer.timeout.connect(window.ui.updateReadouts)
    ui_update_timer.start(100)

    graph_update_timer = QtCore.QTimer() # set up timer to update graphs
    graph_update_timer.timeout.connect(window.ui.updateGraphs)
    graph_update_timer.start(300)

    status_timer = QtCore.QTimer() # set up timer to refresh connection status and files
    status_timer.timeout.connect(window.ui.statusUpdate)
    status_timer.start(1000)

    sys.exit(app.exec_())


