#   PyQt5 QLabels Example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("PyQt5 QLabel Demo")

        # Create a QLabel
        label = QLabel("Aloha", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(50, 50, 300, 200)

        # Add styling with CSS
        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        # Align the text (Horizontal + Vertical)
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
