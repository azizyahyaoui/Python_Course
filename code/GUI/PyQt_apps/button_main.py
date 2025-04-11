import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtWidgets import QPushButton # import the button module




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 650, 450)
        self.setWindowTitle("Push Button")
        self.button = QPushButton("Click me!",self)
        self.label = QLabel("Hello There!",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(200,100,300,200)
        self.button.setStyleSheet(" font: bold 14px;")
        self.label.setGeometry(200,300,300,200)
        self.label.setStyleSheet(" font-size: 50px;")

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("clicked")
        self.button.setText("Clicked !")
        self.label.setText("Good Bye!")
        self.button.setDisabled(True)

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()








