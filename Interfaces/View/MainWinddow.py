from PyQt6 import QtCore
import sys
from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow, QWidget, QLineEdit
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCharts import QChart, QChartView, QLineSeries


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1600, 900)
        self.setMaximumSize(1600, 900)

    def setupUi(self):
        ############################################################
        # Titulo
        self.Title = QLabel("Banco de pruebas")
        self.Title.setParent(self)

        ############################################################
        # Side Bar
        self.SideBar = QWidget(self)
        self.SideBar_Title = QLabel("Menu")
        self.SideBar_Title.setParent(self.SideBar)
        self.ExitBtn = QPushButton(self.SideBar)
        self.ExitBtn.setText("X")
        
        ##########################################################
        # QtCharts para graficar los datos del empuje
        self.Chart = QChart()
        self.series = QLineSeries()

        for i in range(20):
            self.series.append(i,i**2)

        # Agregando datos al Chart
        self.Chart.addSeries(self.series)
        self.Chart.createDefaultAxes()
        self.Chart.setTitle("Empuje-Tiempo")

        # Agregando el chart a la vista
        self._chart_view = QChartView(self.Chart)
        self._chart_view.setParent(self)
        ##########################################################
        # Motor Configuration
        self.nombre = ''
        self.peso = 0.0
        self.masaPropelente = 0.0

        self.Motor = QWidget(self)
        self._motor_title = QLabel("Configuracion de Motor")
        self._motor_title.setParent(self.Motor)

        self.nombre_motor = QLineEdit(self.Motor)
        self.peso_motor = QLineEdit(self.Motor)
        self.masaPropelente_motor = QLineEdit(self.Motor)

        self.motor_btn = QPushButton(self.Motor)
        self.motor_btn.setText("Config")

    def setupStyle(self):
        self.setWindowTitle("Banco de pruebas - Python")
        self.setStyleSheet("background-color: #0d131f")

        self.Title.setGeometry(750, 10, 350, 50)
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setStyleSheet("color:white; font-size:36px; font-weight:bold;")

        self.SideBar.setGeometry(0,0,300,900)
        self.SideBar.setStyleSheet("background-color: #252f43;")
        self.SideBar_Title.setStyleSheet("color:white;font-size:24px; font-weight:bold;")
        self.SideBar_Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SideBar_Title.setGeometry(75,10,150,50)

        self.ExitBtn.setStyleSheet("color: white; background-color: #274464;")
        self.ExitBtn.setGeometry(75, 700, 150, 50)        

        self._chart_view.setGeometry(350, 100, 800, 500)

        # Motor configuration
        self.Motor.setGeometry(1150, 100, 450, 700)
        self._motor_title.setGeometry(125, 25, 250, 50)
        self._motor_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._motor_title.setStyleSheet("color:white; font-weight:bold; font-size:18px;")
        
        self.nombre_motor.setGeometry(125, 100, 250, 40)
        self.nombre_motor.setStyleSheet("color:white; font-size: 18px")

        self.peso_motor.setGeometry(125, 175, 250, 40)
        self.peso_motor.setStyleSheet("color:white; font-size: 18px;")

        self.masaPropelente_motor.setGeometry(125, 250, 250, 40)
        self.masaPropelente_motor.setStyleSheet("color:white; font-size: 18px;")

        self.motor_btn.setGeometry(125, 500, 250, 50)
        self.motor_btn.setStyleSheet("color:white;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()
