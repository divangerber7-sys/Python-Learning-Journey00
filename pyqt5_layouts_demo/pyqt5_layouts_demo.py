#   PyQt5 Layouts Example

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel,
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Layouts Demo")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Labels
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        # Style labels with background colors
        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:green;")
        label4.setStyleSheet("background-color:blue;")
        label5.setStyleSheet("background-color:purple;")

        # ----------- CHOOSE LAYOUT TYPE ------------
        # Example: Vertical Box Layout
        # layout = QVBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)
        # layout.addWidget(label3)
        # layout.addWidget(label4)
        # layout.addWidget(label5)

        # Example: Horizontal Box Layout
        # layout = QHBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)
        # layout.addWidget(label3)
        # layout.addWidget(label4)
        # layout.addWidget(label5)

        # Example: Grid Layout
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 1, 0)
        layout.addWidget(label4, 1, 1)
        layout.addWidget(label5, 2, 0)

        # Set layout to central widget
        central_widget.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
