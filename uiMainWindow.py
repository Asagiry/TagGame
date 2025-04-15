# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QWidget)
from clickableLabel import ClicableLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow:QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Window")
        MainWindow.setFixedSize(1100, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(540, 30, 522, 522))
        self.area = QGridLayout(self.gridFrame)
        self.area.setObjectName(u"area")
        self.chip_1 = ClicableLabel(self.gridFrame)
        self.chip_1.setObjectName(u"ClicableLabel")       
        self.chip_1.setAlignment(Qt.AlignCenter) 
        self.area.addWidget(self.chip_1, 0, 0, 1, 1)
        self.chip_2 = ClicableLabel(self.gridFrame)
        self.chip_2.setObjectName(u"ClicableLabel")       
        self.chip_2.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_2, 0, 1, 1, 1)
        self.chip_3 = ClicableLabel(self.gridFrame)
        self.chip_3.setObjectName(u"ClicableLabel")       
        self.chip_3.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_3, 0, 2, 1, 1)
        self.chip_4 = ClicableLabel(self.gridFrame)
        self.chip_4.setObjectName(u"ClicableLabel")       
        self.chip_4.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_4, 0, 3, 1, 1)
        self.chip_5 = ClicableLabel(self.gridFrame)
        self.chip_5.setObjectName(u"ClicableLabel")        
        self.chip_5.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_5, 1, 0, 1, 1)
        self.chip_6 = ClicableLabel(self.gridFrame)
        self.chip_6.setObjectName(u"ClicableLabel")       
        self.chip_6.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_6, 1, 1, 1, 1)
        self.chip_7 = ClicableLabel(self.gridFrame)
        self.chip_7.setObjectName(u"ClicableLabel")       
        self.chip_7.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_7, 1, 2, 1, 1)
        self.chip_8 = ClicableLabel(self.gridFrame)
        self.chip_8.setObjectName(u"ClicableLabel")        
        self.chip_8.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_8, 1, 3, 1, 1)
        self.chip_9 = ClicableLabel(self.gridFrame)
        self.chip_9.setObjectName(u"ClicableLabel")
        self.chip_9.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_9, 2, 0, 1, 1)
        self.chip_10 = ClicableLabel(self.gridFrame)
        self.chip_10.setObjectName(u"ClicableLabel")        
        self.chip_10.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_10, 2, 1, 1, 1)
        self.chip_11 = ClicableLabel(self.gridFrame)
        self.chip_11.setObjectName(u"ClicableLabel")       
        self.chip_11.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_11, 2, 2, 1, 1)   
        self.chip_12 = ClicableLabel(self.gridFrame)
        self.chip_12.setObjectName(u"ClicableLabel")     
        self.chip_12.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_12, 2, 3, 1, 1)
        self.chip_13 = ClicableLabel(self.gridFrame)
        self.chip_13.setObjectName(u"ClicableLabel")
        self.chip_13.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_13, 3, 0, 1, 1)
        self.chip_14 = ClicableLabel(self.gridFrame)
        self.chip_14.setObjectName(u"ClicableLabel")       
        self.chip_14.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_14, 3, 1, 1, 1)   
        self.chip_15 = ClicableLabel(self.gridFrame)
        self.chip_15.setObjectName(u"ClicableLabel")       
        self.chip_15.setAlignment(Qt.AlignCenter)
        self.area.addWidget(self.chip_15, 3, 2, 1, 1)
        
       
       
        
  
        self.shuffleButton = QPushButton(self.centralwidget)
        self.shuffleButton.setObjectName(u"Button")
        self.shuffleButton.setGeometry(QRect(30, 510, 190, 40))
        
        self.saveGameButton = QPushButton(self.centralwidget)
        self.saveGameButton.setObjectName(u"Button")
        self.saveGameButton.setText("Сохранить")
        self.saveGameButton.setGeometry(QRect(250,510,190,40))
        self.saveGameButton.blockSignals(True)
        self.saveGameButton.setStyleSheet("text-decoration: line-through")
        
        self.turns = QLabel(self.centralwidget)  
        self.turns.setGeometry(QRect(30,100,350,40))
        self.turns.setObjectName(u"Label")
        
        self.timer = QLabel(self.centralwidget)
        self.timer.setText("Оставшееся время = 0")
        self.timer.setGeometry(QRect(30,170,350,40))
        self.timer.setObjectName(u"Label")
        
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setText("Назад")
        self.backButton.setGeometry(30,30,190,40)
        self.backButton.setObjectName(u"Button")
        
            
  
        self.chips = [
            [self.chip_1,self.chip_2,self.chip_3,self.chip_4],
            [self.chip_5,self.chip_6,self.chip_7,self.chip_8],
            [self.chip_9,self.chip_10,self.chip_11,self.chip_12],
            [self.chip_13,self.chip_14,self.chip_15]
                    ]
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"15 Puzzle game", None))
        self.chip_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.chip_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.chip_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.chip_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.chip_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.chip_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.chip_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.chip_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.chip_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.chip_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.chip_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.chip_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.chip_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.chip_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.chip_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.shuffleButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u0442\u044c", None))
    # retranslateUi

    