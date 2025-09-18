#   PyQt5 Digital Clock Widget

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Center alignment
        self.time_label.setAlignment(Qt.AlignCenter)

        # Styling
        self.time_label.setStyleSheet("font-size: 100px; color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        # Load custom font
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # Timer updates every second
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Initial update
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
