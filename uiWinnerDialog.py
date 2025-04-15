# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWinnerDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from re import S
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QLabel, QPushButton)

class Ui_WinnerDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Window")
        Dialog.setFixedSize(570, 420)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"winnerLabel")
        self.label.setGeometry(QRect(110, 50, 330, 60))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setText("💯 Победа 💯")
        
        self.turns = QLabel(Dialog)
        self.turns.setObjectName(u"Label")
        self.turns.setGeometry(QRect(80, 200, 390, 30))
        self.turns.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        self.time = QLabel(Dialog)
        self.time.setObjectName(u"Label")
        self.time.setGeometry(QRect(80, 250, 390, 30))
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
   
        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"Button")
        self.confirm.setGeometry(QRect(110, 350, 330, 30))
        self.confirm.setText("Подтвердить")
 
        self.gamemode = QLabel(Dialog)
        self.gamemode.setObjectName(u"Label")
        self.gamemode.setGeometry(QRect(80, 150, 390, 30))
        self.gamemode.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0431\u0435\u0434\u0430", None))
        
        self.turns.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0445\u043e\u0434\u043e\u0432 = ", None))
        self.time.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f = ", None))
        self.gamemode.setText(QCoreApplication.translate("Dialog", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0438\u0433\u0440\u044b -", None))
    # retranslateUi

