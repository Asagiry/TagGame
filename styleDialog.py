from PySide6 import QtWidgets
from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from uiStyleDialog import Ui_StyleDialog


class StyleDialog(QDialog):
    def __init__(self,app:QApplication):
        super().__init__()
        self.uiDialog = Ui_StyleDialog()
        self.uiDialog.setupUi(self)
        self.show()
        for i in range(0,5):
            self.uiDialog.styleButtons[i].clicked.connect(self.styleChoice)            
        self.app = app
        self.styles = []
        with open('styles/style1.qss',"r") as f:
            style = f.read()
            self.styles.append(style)
        with open('styles/style2.qss',"r") as f:
            style = f.read()
            self.styles.append(style)
        with open('styles/style3.qss',"r") as f:
            style = f.read()
            self.styles.append(style)
        with open('styles/style4.qss',"r") as f:
            style = f.read()
            self.styles.append(style)
        with open('styles/style.qss',"r") as f:
            style = f.read()
            self.styles.append(style)
        
    def styleChoice(self):
        
        style = self.styles[self.uiDialog.styleButtons.index(self.sender())]
        self.app.setStyleSheet(style)   
        from startDialog import StartDialog
        self.startDialogWindow = StartDialog(self.app)
        self.accept()
        
    def showEvent(self, event):
        self.setWindowOpacity(0.0) 
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(100)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start()
