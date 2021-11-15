from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QSize
# Only needed for access to command line arguments
import sys


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([])
# works too.

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Phydent")
        # defines variable
        # self.button_is_checked = True 

        self.button = QPushButton("Make Nelson suffer")
        # button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("clicked")
        self.button.setText("You already clicked me")
        self.button.setEnabled(False)
        self.setWindowTitle("A new window title")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

# 
app = QApplication(sys.argv)

# Create an instance of a Qt widget, which will be our window
# window = QWidget()
window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()