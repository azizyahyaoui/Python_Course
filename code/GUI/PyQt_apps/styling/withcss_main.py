import  sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QPushButton # import the button module




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton(" #1 ",self)
        self.button2 = QPushButton(" #2 ",self)
        self.button3 = QPushButton(" #3 ",self)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1") # To style each one
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        #Applay CSS to all in one place by using multy line comment """  """
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-weight: bold;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 2px solid black;
                border-radius: 15px;
            }
            QPushButton#button1{
            background-color: hsl(4, 82%, 56%);
            }
            QPushButton#button2{
            background-color: hsl(124, 82%, 56%);
            }
            QPushButton#button3{
            background-color: hsl(237, 82%, 56%);
            }
            
            QPushButton#button1:hover{
            background-color: hsl(4, 82%, 86%);
            }
            
            QPushButton#button2:hover{
            background-color: hsl(124, 82%, 86%);
            }
            
            QPushButton#button3:hover{
            background-color: hsl(237, 82%, 86%);
            }
        
        
            """)

    def on_click(self):
        pass

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()








