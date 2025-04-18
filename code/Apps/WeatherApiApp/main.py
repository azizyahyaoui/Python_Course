import sys, requests
from PyQt5.QtWidgets import  QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from requests import HTTPError


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("Assets/images/icon.png"))
        self.city_label = QLabel("Enter the city name: ",self)
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Tunisia,tunis...")
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_input.setObjectName("city_input")
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
            font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI Emoji;
                margin: 10px;
                padding: 10px;
                
            }
            QLabel#description_label{
                font-size: 50px;
            }
                
        """)

        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        api_key = ""
        city_name = self.city_input.text()
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
               self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your city name!")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key!")
                case 403:
                    self.display_error("Forbidden\nAccess is denied!")
                case 404:
                    self.display_error("Not Found\nCity not found!")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later!")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from the server!")
                case 503:
                    self.display_error("Service Unavailable\nServer is down please try again later!")
                case 504:
                    self.display_error("Gateway Timeout\nNo response from the server please try again later!")
                case _:
                    self.display_error(f"HTTP Error occurred!:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nPlease check your internet connection!")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nRequest time out!")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck api url!")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Something went wrong!\n{req_error}")

    def display_error(self, error_message):
        self.temperature_label.setStyleSheet("font-family: Arial;"
                                             "font-size: 30px;"
                                             "color: #f7394c;")
        self.temperature_label.setText(error_message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        #temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌦️"  # Drizzle
        elif 500 <= weather_id <= 504:
            return "🌧️"  # Rain
        elif weather_id == 511:
            return "🌨️"  # Freezing rain
        elif 520 <= weather_id <= 531:
            return "🌧️"  # Shower rain
        elif 600 <= weather_id <= 602:
            return "❄️"  # Snow
        elif 611 <= weather_id <= 616:
            return "🌨️"  # Sleet / Rain and snow
        elif 620 <= weather_id <= 622:
            return "🌨️"  # Shower snow
        elif weather_id == 701:
            return "🌫️"  # Mist
        elif weather_id == 711:
            return "💨"  # Smoke
        elif weather_id == 721:
            return "🌁"  # Haze
        elif weather_id in [731, 751, 761]:
            return "🌪️"  # Dust/Sand
        elif weather_id == 741:
            return "🌫️"  # Fog
        elif weather_id == 762:
            return "🌋"  # Volcanic ash
        elif weather_id == 771:
            return "💨"  # Squalls
        elif weather_id == 781:
            return "🌪️"  # Tornado
        elif weather_id == 800:
            return "☀️"  # Clear sky
        elif weather_id == 801:
            return "🌤️"  # Few clouds
        elif weather_id == 802:
            return "⛅"  # Scattered clouds
        elif weather_id == 803:
            return "🌥️"  # Broken clouds
        elif weather_id == 804:
            return "☁️"  # Overcast clouds
        else:
            return "❔"  # Unknown condition

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
