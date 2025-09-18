"""
🌤️ PyQt5 Weather App
Fetches live weather data from OpenWeatherMap API and displays:
- Temperature in Celsius
- Weather description
- Weather emoji based on condition

Author: D Gerber
"""

import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Weather App")
        self.setGeometry(600, 300, 600, 400)

        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        # Labels
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("", self)
        self.emoji_label = QLabel("", self)
        self.description_label = QLabel("", self)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        # Alignments
        for widget in [self.city_label, self.city_input, self.temperature_label,
                       self.emoji_label, self.description_label]:
            widget.setAlignment(Qt.AlignCenter)

        # Styling
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#city_label {
                font-size: 36px;
                font-style: italic;
            }
            QLineEdit {
                font-size: 32px;
                padding: 10px;
            }
            QPushButton {
                font-size: 28px;
                font-weight: bold;
                padding: 10px;
            }
            QLabel#temperature_label {
                font-size: 72px;
                font-weight: bold;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 40px;
                font-weight: medium;
            }
        """)

        # Connect button to function
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        """Fetch weather data from OpenWeatherMap API."""
        city = self.city_input.text().strip()
        if not city:
            self.display_error("Please enter a city name")
            return

        params = {"q": city, "appid": self.API_KEY}

        try:
            response = requests.get(self.API_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") == 200:
                self.display_weather(data)
            else:
                self.display_error(data.get("message", "Unknown error"))

        except requests.exceptions.RequestException as e:
            self.display_error(f"Network error: {str(e)}")

    def display_weather(self, data):
        """Update the UI with weather data."""
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temp_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)

    def display_error(self, message):
        """Display an error message in the UI."""
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    @staticmethod
    def get_weather_emoji(weather_id):
        """Return a weather emoji based on OpenWeatherMap weather ID."""
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌧️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "❓"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
