import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit # import the line edit or the TextBox module




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 650, 450)
        self.line_edit = QLineEdit(self)
        self.btn_submit = QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(20, 10, 200, 40)
        self.btn_submit.setGeometry(220, 10, 200, 40)
        self.line_edit.setStyleSheet("font: 25px Arial;")
        self.btn_submit.setStyleSheet("font: 25px Arial;")
        self.line_edit.setPlaceholderText("Enter your name")

        self.btn_submit.clicked.connect(self.on_submit)

    def on_submit(self):
        text = self.line_edit.text()
        print(f"Hello Mr.{text}")



def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()








