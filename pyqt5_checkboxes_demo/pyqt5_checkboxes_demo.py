#   PyQt5 CheckBox Example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 CheckBox Demo")

        # Create checkbox
        self.checkbox = QCheckBox(" Are you there? ", self)
        self.initUI()

    def initUI(self):
        # Position and style
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px; font-family: sans-serif;")
        self.checkbox.setChecked(True)
        self.checkbox.setCheckState(False)

        # Connect state change signal to slot
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You are here!!")
        else:
            print("You are lost!!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

