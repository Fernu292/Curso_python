from View.MainWinddow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

class Banco():
    def __init__(self):
        self.window = MainWindow()
        self.initGui()
        self.setButtonsActions()
        self.window.show()

    def initGui(self):
        self.window.setupUi()
        self.window.setupStyle()
        
    def initStyles(self):
        pass
    def setButtonsActions(self):
        self.window.ExitBtn.clicked.connect(self.exitApp)

    # Acciones de la app
    def exitApp(self):
        self.window.close()

def main():
    app = QApplication(sys.argv)
    banco = Banco()
    return app.exec()


if __name__ == '__main__':
    main()