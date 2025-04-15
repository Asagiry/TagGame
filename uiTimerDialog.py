# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timerAgreeDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QDialog, QLabel, QPushButton)

class Ui_TimerDialog(object):
    def setupUi(self, Dialog:QDialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Window")
        Dialog.setFixedSize(560, 400) #410 310
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"Label")
        self.label.setGeometry(QRect(30, 30, 500, 60))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"Label")
        self.label_2.setGeometry(QRect(85, 120, 390, 40))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yesButton = QPushButton(Dialog)
        self.yesButton.setObjectName(u"timerButton")
        self.yesButton.setGeometry(QRect(160, 340, 100, 25))
        self.noButton = QPushButton(Dialog)
        self.noButton.setObjectName(u"timerButton")
        self.noButton.setGeometry(QRect(300, 340, 100, 25))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u0442\u0430\u0439\u043c\u0435\u0440", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0438\u0433\u0440\u0443 \u043d\u0430 \u0432\u0440\u0435\u043c\u044f?", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u043e \u0443\u0441\u043b\u043e\u0436\u043d\u0438\u0442 \u0438\u0433\u0440\u0443 ", None))
        self.yesButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.noButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
    # retranslateUi

