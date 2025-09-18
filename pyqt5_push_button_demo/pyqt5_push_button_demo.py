#   PyQt5 Push Buttons Example
#   Buttons emit a signal (event) that can be connected to a slot (action).
#   Example: self.button.clicked.connect(self.on_click)

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Push Button Demo")

        # Create button and label
        self.button = QPushButton("Click Me!!!", self)
        self.label = QLabel("Aloha", self)

        self.initUI()

    def initUI(self):
        # Button styling and position
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.on_click)  # Signal → Slot

        # Label styling and position
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setFont(QFont("Arial", 20))

    # Slot function (executed when button is clicked)
    def on_click(self):
        self.label.setText("Mahalo")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
