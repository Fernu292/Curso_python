from View.MainWinddow import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
import sys
import numpy as np
import random

class Banco():
    def __init__(self):
        self.isInit = False
        self.time = 0
        self.window = MainWindow()
        self.initGui()
        self.setButtonsActions()
        self.timer = QTimer()
        self.window.show()

    def initGui(self):
        self.window.setupUi()
        self.window.setupStyle()

    def updateChart(self):
        value = np.sin(self.time)
        self.window.append(self.time, value)
        self.time += 0.01        
    def initStyles(self):
        pass

    def setButtonsActions(self):
        self.window.StartBtn.clicked.connect(self.startTest)
    # Acciones de la app

    def startTest(self):
        print(f'Llamando al inicion de la app')
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.updateChart)
        if(self.isInit==False):
            self.timer.start()
            self.isInit = True
        else:
            self.timer.stop()


def main():
    app = QApplication(sys.argv)
    banco = Banco()
    return app.exec()


if __name__ == '__main__':
    main()