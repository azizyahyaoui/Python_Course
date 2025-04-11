import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QFontDatabase


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 650, 450)
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("assets/img/clock-icon.png"))
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.time_label.setGeometry(10, 10, 650, 450)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)


        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 90px;"
            "color: hsl(111, 100%, 50%);"
        )
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("assets/fonts/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family,90)
        self.time_label.setFont(custom_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

def main():

    clock = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(clock.exec_())


if __name__ == '__main__':
    main()








