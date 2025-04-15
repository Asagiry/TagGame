# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QDialog, QFrame, QLabel,
    QPushButton)

class Ui_StartDialog(object):
    def setupUi(self, Dialog:QDialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Window")
        Dialog.setFixedSize(560,400)
        Dialog.setWindowTitle("Добро пожаловать в игру 15")
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"Label")
        self.label.setGeometry(QRect(30, 30, 500, 60))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.startNewButton = QPushButton(Dialog)
        self.startNewButton.setObjectName(u"Button")
        self.startNewButton.setGeometry(QRect(170, 170, 220, 40))
       
        self.startSaveButton = QPushButton(Dialog)
        self.startSaveButton.setObjectName(u"Button")
        self.startSaveButton.setGeometry(QRect(110, 240, 340, 40))
        self.startSaveButton.setText("Выбрать сохранение")
        
        self.styleChoiceButton = QPushButton(Dialog)
        self.styleChoiceButton.setObjectName(u"Button")
        self.styleChoiceButton.setGeometry(QRect(170, 310, 220, 40))
        self.styleChoiceButton.setText("Выбор стиля")
        

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0438\u0433\u0440\u0443 \u041f\u044f\u0442\u043d\u0430\u0448\u043a\u0438", None))
        self.startNewButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e", None))
    
    # retranslateUi

