#   PyQt5 Radio Buttons Example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Radio Button Demo")

        # Payment type radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master", self)
        self.radio3 = QRadioButton("Gift Card", self)

        # Payment method radio buttons
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        # Button groups
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        # Position radio buttons
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # Apply CSS-like styling to all QRadioButtons
        self.setStyleSheet(
            "QRadioButton {"
            "font-size: 30px;"
            "font-family: sans-serif;"
            "padding: 10px;"
            "}"
        )

        # Add buttons to their groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connect toggled signals to slot
        self.radio1.toggled.connect(self.radio_button_clicked)
        self.radio2.toggled.connect(self.radio_button_clicked)
        self.radio3.toggled.connect(self.radio_button_clicked)
        self.radio4.toggled.connect(self.radio_button_clicked)
        self.radio5.toggled.connect(self.radio_button_clicked)

    def radio_button_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
