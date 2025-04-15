import asyncio
import json
from PySide6 import QtWidgets
from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog)
from mainWindow import MainWindow
from styleDialog import StyleDialog
from timerDialog import TimerDialog
from uiStartDialog import Ui_StartDialog


class StartDialog(QDialog):
    def __init__(self,app:QApplication):
        super().__init__()
        self.app = app
        
        self.uiDialog = Ui_StartDialog()
        self.uiDialog.setupUi(self)
        self.show()
        self.uiDialog.startNewButton.clicked.connect(self.newGame)
        self.uiDialog.startSaveButton.clicked.connect(self.savedGame)
        self.uiDialog.styleChoiceButton.clicked.connect(self.styleChoice)

    def newGame(self):
        
        self.timerDialog= TimerDialog(self.app)
      
        self.accept()
        
    def savedGame(self):
        file_path, _ = QFileDialog.getOpenFileName(self,'Open your save','', 'JSON Files (*.json)')
        if (file_path == ""):
            return
        with open(file_path, 'r') as file:
            saved_data = json.load(file)
            
        self.MainWindow = MainWindow(False,saved_data['turns'],self.app)
        self.MainWindow.show()
        asyncio.ensure_future(self.MainWindow.fillBoardFromJson(saved_data["grid_state"]))

        self.accept()
    def styleChoice(self):
        self.styleDialog = StyleDialog(self.app)
        self.accept()
        
    def showEvent(self, event):
        self.setWindowOpacity(0.0) 
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(100)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start() 
   