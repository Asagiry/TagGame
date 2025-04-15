
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel


class ClicableLabel(QLabel):
    clicked = Signal()
    def __init__(self,parent):
        super().__init__(parent)  
   
      
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
   
   