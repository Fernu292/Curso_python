from PyQt6.QtWidgets import QApplication
from view.Login import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    return app.exec()

if __name__ == '__main__':
    main()