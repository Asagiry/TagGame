# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiLoseDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtWidgets import (QDialog, QLabel, QPushButton)

class Ui_LoseDialog(object):
    def setupUi(self, Dialog:QDialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Window")
        Dialog.setFixedSize(570, 420)
        Dialog.setWindowTitle("Поражение")
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"Label")
        self.label.setGeometry(QRect(95, 50, 380, 60))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setText(f"😭💀 Время вышло 💀😭")

        self.turns = QLabel(Dialog)
        self.turns.setObjectName(u"Label")
        self.turns.setGeometry(QRect(95, 150, 380, 30))
        self.turns.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"Button")
        self.confirm.setGeometry(QRect(120, 350, 330, 50))
    
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.turns.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0445\u043e\u0434\u043e\u0432 = ", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
    # retranslateUi

