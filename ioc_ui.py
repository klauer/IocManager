# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ioc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.IOCname = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.IOCname.sizePolicy().hasHeightForWidth())
        self.IOCname.setSizePolicy(sizePolicy)
        self.IOCname.setMinimumSize(QtCore.QSize(170, 0))
        self.IOCname.setReadOnly(True)
        self.IOCname.setObjectName("IOCname")
        self.gridLayout.addWidget(self.IOCname, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.heartbeat = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.heartbeat.sizePolicy().hasHeightForWidth())
        self.heartbeat.setSizePolicy(sizePolicy)
        self.heartbeat.setMinimumSize(QtCore.QSize(170, 0))
        self.heartbeat.setReadOnly(True)
        self.heartbeat.setObjectName("heartbeat")
        self.gridLayout.addWidget(self.heartbeat, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tod = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.tod.sizePolicy().hasHeightForWidth())
        self.tod.setSizePolicy(sizePolicy)
        self.tod.setMinimumSize(QtCore.QSize(170, 0))
        self.tod.setReadOnly(True)
        self.tod.setObjectName("tod")
        self.gridLayout.addWidget(self.tod, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.boottime = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.boottime.sizePolicy().hasHeightForWidth())
        self.boottime.setSizePolicy(sizePolicy)
        self.boottime.setMinimumSize(QtCore.QSize(170, 0))
        self.boottime.setReadOnly(True)
        self.boottime.setObjectName("boottime")
        self.gridLayout.addWidget(self.boottime, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.location = QtWidgets.QLineEdit(self.widget_2)
        self.location.setReadOnly(True)
        self.location.setObjectName("location")
        self.gridLayout.addWidget(self.location, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.description = QtWidgets.QLineEdit(self.widget_2)
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 2, 3, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.widget_2)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 2, 4, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.widget_2)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 3, 0, 1, 1)
        self.findpv = QtWidgets.QLineEdit(self.widget_2)
        self.findpv.setObjectName("findpv")
        self.gridLayout.addWidget(self.findpv, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1263, 23))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuIOC_Control = QtWidgets.QMenu(self.menubar)
        self.menuIOC_Control.setObjectName("menuIOC_Control")
        self.menuMisc = QtWidgets.QMenu(self.menubar)
        self.menuMisc.setObjectName("menuMisc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApply = QtWidgets.QAction(MainWindow)
        self.actionApply.setObjectName("actionApply")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionReboot = QtWidgets.QAction(MainWindow)
        self.actionReboot.setObjectName("actionReboot")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setObjectName("actionConsole")
        self.actionRemember = QtWidgets.QAction(MainWindow)
        self.actionRemember.setObjectName("actionRemember")
        self.actionAuth = QtWidgets.QAction(MainWindow)
        self.actionAuth.setObjectName("actionAuth")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHard_Reboot = QtWidgets.QAction(MainWindow)
        self.actionHard_Reboot.setObjectName("actionHard_Reboot")
        self.actionReboot_Server = QtWidgets.QAction(MainWindow)
        self.actionReboot_Server.setObjectName("actionReboot_Server")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuConfiguration.addAction(self.actionApply)
        self.menuConfiguration.addAction(self.actionSave)
        self.menuConfiguration.addAction(self.actionRevert)
        self.menuIOC_Control.addAction(self.actionReboot)
        self.menuIOC_Control.addAction(self.actionHard_Reboot)
        self.menuIOC_Control.addAction(self.actionReboot_Server)
        self.menuIOC_Control.addAction(self.actionLog)
        self.menuIOC_Control.addAction(self.actionConsole)
        self.menuMisc.addAction(self.actionHelp)
        self.menuMisc.addAction(self.actionRemember)
        self.menuMisc.addAction(self.actionAuth)
        self.menuMisc.addAction(self.actionQuit)
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuIOC_Control.menuAction())
        self.menubar.addAction(self.menuMisc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Current IOC:"))
        self.label_3.setText(_translate("MainWindow", "Heartbeat:"))
        self.label_2.setText(_translate("MainWindow", "Time of Day:"))
        self.label_4.setText(_translate("MainWindow", "Boot Time:"))
        self.label_5.setText(_translate("MainWindow", "Location:"))
        self.label_6.setText(_translate("MainWindow", "Description:"))
        self.userLabel.setText(_translate("MainWindow", "User: Guest"))
        self.label_55.setText(_translate("MainWindow", "Find PV:"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuIOC_Control.setTitle(_translate("MainWindow", "IOC Control"))
        self.menuMisc.setTitle(_translate("MainWindow", "Utilities"))
        self.actionApply.setText(_translate("MainWindow", "Apply"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionReboot.setText(_translate("MainWindow", "Soft IOC Reboot"))
        self.actionLog.setText(_translate("MainWindow", "Show Log"))
        self.actionConsole.setText(_translate("MainWindow", "Show Console"))
        self.actionRemember.setText(_translate("MainWindow", "Remember Versions"))
        self.actionAuth.setText(_translate("MainWindow", "Authenticate User"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionHard_Reboot.setText(_translate("MainWindow", "Hard IOC Reboot"))
        self.actionReboot_Server.setText(_translate("MainWindow", "Reboot Server"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
