
from PySide6 import QtWidgets
from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QDialog
from uiLoseDialog import Ui_LoseDialog


class LoseDialog(QDialog):
    def __init__(self,turns:int):
        super().__init__()
        self.uiDialog = Ui_LoseDialog()
        self.uiDialog.setupUi(self)
        self.show()
        self.uiDialog.turns.setText("Количество ходов = "+str(turns))
        self.uiDialog.confirm.clicked.connect(self.confirm)
        
    def confirm(self):
        self.accept()
    def showEvent(self, event):
        self.setWindowOpacity(0.0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start()
