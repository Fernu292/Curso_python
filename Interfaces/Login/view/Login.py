from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.setStyleSheet("padding: 0")
        self.contentsMargins()

        # CENTRAL WIDGET AND HBOXLAYOUT
        self.centralWidget = QWidget(self)
        self.centralWidget.resize(160*7, 90*7)
        self.setCentralWidget(self.centralWidget)

        self.h_layout = QHBoxLayout(self.centralWidget)

        # LOGIN IMG
        self.Img = QLabel(self.centralWidget)
        self.pixMap = QPixmap("/home/fernudev/Projects/Curso_python/Interfaces/Login/view/img/rocket_launch.png").scaled(600, 650,
                                                                                                                           aspectRatioMode=QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        self.Img.setPixmap(self.pixMap)
        self.Img.setGeometry(-1,-1,int(self.width()*0.6), self.height())

        # LOGIN FORM
        self.login_form = QWidget()
        self.login_v_layout = QVBoxLayout(self.login_form)
        # self.login_form.setStyleSheet("border: 1px solid red")

        self.login_title = QLabel()
        self.login_title.setText("Login Antares Aeroespace")
        self.login_title.setStyleSheet("font-weight: bold; font-size: 24px;")
        self.login_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_title.setMaximumHeight(50)

        # FORM
        self.form_inputs = QWidget()
        self.form_inputs_layout = QVBoxLayout(self.form_inputs)
        self.form_inputs.setMaximumHeight(300)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setTextMargins(5,0,0,0)
        self.email.setMaximumSize(int(self.login_form.width()*0.5), 50)
        self.email.setStyleSheet("border-radius: 15px;")
        
        self.passWord = QLineEdit()
        self.passWord.setPlaceholderText("Password")
        self.passWord.setTextMargins(5,0,0,0)
        self.passWord.setMaximumSize(int(self.login_form.width()*0.5), 50)
        self.passWord.setEchoMode(QLineEdit.EchoMode.Password)
        self.passWord.setStyleSheet("border-radius: 15px;")

        self.login_btn = QPushButton()
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_btn.setText("Login")
        self.login_btn.setStyleSheet("border-radius: 15px; background-color: #592da2; font-size: 18px; font-weight: bold")
        self.login_btn.setMinimumHeight(45)

        self.login_btn.clicked.connect(self.clickLogin)
        self.login_btn.animateClick()

        self.form_inputs_layout.addWidget(self.email)
        self.form_inputs_layout.addWidget(self.passWord)
        self.form_inputs_layout.addWidget(self.login_btn)
        self.form_inputs.setLayout(self.form_inputs_layout)
        self.form_inputs_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.form_inputs_layout.setSpacing(20)

        # GENERAL LOGIN LAYOUT
        self.login_v_layout.addWidget(self.login_title)
        self.login_v_layout.addWidget(self.form_inputs)
        self.login_v_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.login_v_layout.setSpacing(0)    
    

        self.login_form.setLayout(self.login_v_layout)

        self.h_layout.addWidget(self.Img)
        self.h_layout.addWidget(self.login_form)
        self.h_layout.setContentsMargins(0,0,0,0)

        # FINAL LAYOUT CONFIG

        self.centralWidget.setLayout(self.h_layout)
        self.resize(160*7, 90*7)
        self.setMaximumSize(160*7, 90*7)

        self.show()

    def clickLogin(self):
        self.login_btn.setStyleSheet("border-radius: 15px; background-color: #6333b2; font-size: 18px; font-weight: bold")
