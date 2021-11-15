import socket

#from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, 
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
# Only needed for access to command line arguments
import sys

import subprocess

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Phydent")
        # defines variable
        # self.button_is_checked = True 

        self.button = QPushButton("OPEN")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.opusbutton = QPushButton("OPEN OPUS")

        self.selectopuspath = QToolButton()
        self.selectopuspath.setIcon(QIcon("bug.png]"))
        self.selectopuspath.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    
        self.labeltest = QLabel("Test")
        self.labeltest.setFont(QFont('Arial',20))

        self.layout = QHBoxLayout()

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.selectopuspath)
        self.layout.addWidget(self.labeltest)
        self.layout.addWidget(self.opusbutton)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget) 

        # button = self.button = QPushButton("OPEN")
        # button.setFont(QFont('Arial', 20))
        # button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("Phydent")
        # Set the central widget of the Window.
        #self.setCentralWidget(self.button)


    #def openOpus(self):


    def the_button_was_clicked(self):
        if process_exists('opus.exe'):
            print("clicked")
            localhost = "127.0.0.1"
            port = 80
            version = MainWindow.opusrequest(localhost,port, "GET_VERSION")
            self.button.setText(version[0])
        else:
            print("test")
        #localhost = "127.0.0.1"
        #port = 80
        #version = MainWindow.opusrequest(localhost,port, "GET_VERSION")
        #self.button.setText(version[0])
        # print("clicked")
        #self.button.setText("You already clicked me")
        # self.button.setEnabled(False)
        #self.setWindowTitle("A new window title")
    
    def opusrequest(IP,port,command):
        # print(socket.gethostbyname(socket.gethostname()))
        command=command.replace(" ", "%20")
        request="GET /OpusCommand.htm?" + command + "\r\n\r\n"
        # print(request)
        data = ""
        part = None

        #request to OPUS
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP,port))
        s.sendall(request.encode("windows-1252"))
        #construct answer partially from "byte stream"
        while True:
            part = s.recv(1048576)  # 2^20 bytes = 1 MByte        
            if (part == b''):
                break;
            else:
                data += part.decode("windows-1252")
        #Close connection and provide answer as string    
        s.close()
        return(data.split("\n\r\n"))

app = QApplication(sys.argv)

# Create an instance of a Qt widget, which will be our window
# window = QWidget()
window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()