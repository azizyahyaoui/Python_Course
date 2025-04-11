import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox
from PyQt5.QtCore import Qt # the checkbox is loaded by default with the Qt core




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 650, 450)
        self.checkbox = QCheckBox("Check The BOX!",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setChecked(False) # False is the default value of the checkbox
        self.checkbox.setGeometry(10, 10, 500, 100)
        self.checkbox.setStyleSheet("font: bold 30px Arial;")
        self.checkbox.stateChanged.connect(self.on_checkbox_changed)

    def on_checkbox_changed(self, state):
        self.checkbox.setChecked(state)
        if state == Qt.Checked:
            print("You checked The Box!")
        else:
            print("You unchecked The Box!")




def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()








