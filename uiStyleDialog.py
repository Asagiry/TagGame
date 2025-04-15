# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiStyleDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_StyleDialog(object):
    def setupUi(self, Dialog:QDialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Window")
        Dialog.setFixedSize(560, 400)
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"Label")
        self.label.setGeometry(QRect(30, 40, 500, 40))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        
        self.styleChoice_1 = QPushButton(Dialog)
        self.styleChoice_1.setObjectName(u"styleChoice_1")
        self.styleChoice_1.setGeometry(QRect(30, 120, 500, 40))
        self.styleChoice_1.setText("Неоновый аквамарин")
 
        self.styleChoice_2 = QPushButton(Dialog)
        self.styleChoice_2.setObjectName(u"styleChoice_2")
        self.styleChoice_2.setGeometry(QRect(30, 170, 500, 40))
        self.styleChoice_2.setText("Тёмный")
 
        self.styleChoice_3 = QPushButton(Dialog)
        self.styleChoice_3.setObjectName(u"styleChoice_3")
        self.styleChoice_3.setGeometry(QRect(30, 220, 500, 40))
        self.styleChoice_3.setText("Красный градиент")
  
        self.styleChoice_4 = QPushButton(Dialog)
        self.styleChoice_4.setObjectName(u"styleChoice_4")
        self.styleChoice_4.setGeometry(QRect(30, 270, 500, 40))
        self.styleChoice_4.setText("Синий градиент")
  
        self.styleChoice_5 = QPushButton(Dialog)
        self.styleChoice_5.setObjectName(u"styleChoice_5")
        self.styleChoice_5.setGeometry(QRect(30, 320, 500, 40))
        self.styleChoice_5.setText("Стандартный") 
   

        
        
        
        

        self.styleButtons = [self.styleChoice_1,self.styleChoice_2,self.styleChoice_3,
                             self.styleChoice_4,self.styleChoice_5 ]
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Style choice", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0441\u0442\u0438\u043b\u044f", None))
    # retranslateUi

