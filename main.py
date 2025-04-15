import sys
from PySide6 import QtAsyncio
from PySide6.QtWidgets import QApplication
from startDialog import StartDialog


if __name__ == "__main__":
    app = QApplication()
    with open('styles/style.qss',"r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window = StartDialog(app)
    sys.exit(QtAsyncio.run())
    