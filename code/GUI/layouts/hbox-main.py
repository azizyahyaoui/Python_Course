import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtWidgets import QHBoxLayout # import the Horizontal layout module


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 650, 450)
        self.setWindowTitle("Horizontal layout")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        label_1 = QLabel("#1", self)
        label_1.setStyleSheet("background-color:red")
        label_2 = QLabel("#2", self)
        label_2.setStyleSheet("background-color:yellow")
        label_3 = QLabel("#3", self)
        label_3.setStyleSheet("background-color:green")
        label_4 = QLabel("#4", self)
        label_4.setStyleSheet("background-color:blue")
        label_5 = QLabel("#5", self)
        label_5.setStyleSheet("background-color:purple")
        label_6 = QLabel("#6", self)
        label_6.setStyleSheet("background-color:aqua")

        # Create a Horizontal layout and add labels to the UI
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(label_1)
        hbox_layout.addWidget(label_2)
        hbox_layout.addWidget(label_3)
        hbox_layout.addWidget(label_4)
        hbox_layout.addWidget(label_5)
        hbox_layout.addWidget(label_6)

        # Set layout to central widget
        central_widget.setLayout(hbox_layout)

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()







