#   PyQt5 setStyleSheet() Example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Stylesheet Demo")

        # Create buttons
        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)

        self.initUI()

    def initUI(self):
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        # Assign object names for specific styling
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Apply stylesheet
        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1 {
                background-color: hsl(120, 100%, 50.2%);
            }
            QPushButton#button2 {
                background-color: hsl(240, 100%, 50%);
            }
            QPushButton#button3 {
                background-color: hsl(60, 100%, 50%);
            }
            QPushButton#button1:hover {
                background-color: hsl(120, 100%, 80.2%);
            }
            QPushButton#button2:hover {
                background-color: hsl(240, 100%, 80%);
            }
            QPushButton#button3:hover {
                background-color: hsl(60, 100%, 80%);
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
