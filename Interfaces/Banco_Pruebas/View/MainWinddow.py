from PyQt6 import QtCore
import sys
from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow, QWidget, QLineEdit
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1600, 900)
        self.setMaximumSize(1600, 900)
        self.data = []

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

        self.StartBtn = QPushButton(self.SideBar)
        self.StartBtn.setText("Start")
        
        ##########################################################
        # QtCharts para graficar los datos del empuje
        self.Chart = QChart()
        self.series = QLineSeries()
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.axisX.setRange(0, 10)
        self.axisY.setRange(0, 10)

        # Agregando datos al Chart
        self.Chart.addSeries(self.series)
        self.Chart.addAxis(self.axisX,QtCore.Qt.AlignmentFlag.AlignBottom)
        self.Chart.addAxis(self.axisY,QtCore.Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
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
        # Side Bar
        self.SideBar.setGeometry(0,0,150,900)
        self.SideBar.setStyleSheet("background-color: #252f43;")
        self.SideBar_Title.setStyleSheet("color:white;font-size:24px; font-weight:bold;")
        self.SideBar_Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SideBar_Title.setGeometry(0,10,150,50)

        self.StartBtn.setStyleSheet("color: white; background: none; font-weight: bold; font-size: 18px")
        self.StartBtn.setGeometry(0, 200, 150, 50)   

        self._chart_view.setGeometry(200, 100, 800, 500)

        # Motor configuration
        self.Motor.setGeometry(1050, 100, 450, 700)
        self.Motor.setStyleSheet("border: 1px solid white; border-radius: 18px")
        self._motor_title.setGeometry(100, 25, 250, 50)
        self._motor_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._motor_title.setStyleSheet("color:white; font-weight:bold; font-size:18px; border:none")
        
        self.nombre_motor.setGeometry(100, 100, 250, 40)
        self.nombre_motor.setStyleSheet("color:white; font-size: 18px; border: 1px solid gray")

        self.peso_motor.setGeometry(100, 175, 250, 40)
        self.peso_motor.setStyleSheet("color:white; font-size: 18px; border: 1px solid gray")

        self.masaPropelente_motor.setGeometry(100, 250, 250, 40)
        self.masaPropelente_motor.setStyleSheet("color:white; font-size: 18px; border: 1px solid gray")

        self.motor_btn.setGeometry(100, 500, 250, 50)
        self.motor_btn.setStyleSheet("color:white;")

    def append(self, x, y):
        print(f'{x},{y}')
        self.data.append(y)
        array = np.array(self.data)
        self.series.append(x,y)
        self.axisX.setRange(0, x+1)
        self.axisY.setRange(array.min() - 2,  array.max() + 4)
   
        
