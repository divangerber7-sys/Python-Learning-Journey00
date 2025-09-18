#   PyQt5 Images Example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Image Demo")

        # Create a QLabel to hold the image
        label = QLabel(self)

        # Load image into QPixmap
        pixmap = QPixmap("enso.jpeg")  # Replace with your image file
        label.setPixmap(pixmap)

        # Scale the image to fit the label
        label.setScaledContents(True)

        # Resize label to half the window
        label.setGeometry(0, 0, 250, 250)

        # Center the label in the window
        label.setGeometry(
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height()
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
