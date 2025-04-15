


from PySide6 import QtWidgets
from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QDialog
from uiWinnerDialog import Ui_WinnerDialog
class WinnerDialog(QDialog):
    def __init__(self,turns:int,time:float ,gamemode:bool):
        super().__init__()
        self.uiDialog = Ui_WinnerDialog()
        self.uiDialog.setupUi(self)
        self.show()
        time = round(time,1)
        match turns:
            case x if (x<=130):
                self.uiDialog.turns.setText("🥇 Количество ходов = "+str(turns)+" 🥇")
            case x if (130<x<160):
                self.uiDialog.turns.setText("🥈 Количество ходов = "+str(turns)+" 🥈")
            case _:
                self.uiDialog.turns.setText("🥉 Количество ходов = "+str(turns)+" 🥉")
        if gamemode:
            match 60-time:
                case x if (x<=35):
                    self.uiDialog.time.setText("🥇  Время прохождения = "+str(60-time)+"s  🥇")
                case x if (35<x<45):
                    self.uiDialog.time.setText("🥈  Время прохождения = "+str(60-time)+"s  🥈")
                case _:
                    self.uiDialog.time.setText("🥉  Время прохождения = "+str(60-time)+"s  🥉")
            self.uiDialog.gamemode.setText("Сложность игры - С таймером")
        else:
            self.uiDialog.time.hide()
            self.uiDialog.gamemode.setText("Сложность игры - Без таймера")
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