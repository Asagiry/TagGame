from PySide6 import QtWidgets
from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import (QApplication, QDialog)
from mainWindow import MainWindow
from uiTimerDialog import Ui_TimerDialog

class TimerDialog(QDialog):
    def __init__(self,app:QApplication):
        super().__init__()
        self.uiDialog = Ui_TimerDialog()
        self.uiDialog.setupUi(self)
        self.show()
        
        self.app = app
        
        self.uiDialog.yesButton.clicked.connect(self.createField)
        self.uiDialog.yesButton.setProperty("Timer",True)

        self.uiDialog.noButton.clicked.connect(self.createField)
        self.uiDialog.noButton.setProperty("Timer",False)
        
    def createField(self):
        self.accept()
        button = self.sender()
        self.MainWindow = MainWindow(button.property("Timer"),0,self.app)
        self.MainWindow.show()
        
    def showEvent(self, event):
        self.setWindowOpacity(0.0) 
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(100)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start()
