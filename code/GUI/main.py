
import sys

# Import necessary PyQt5 modules
from PyQt5.QtGui import QIcon  # Provides an icon to the window
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  # GUI components
from PyQt5.QtCore import Qt  # Core functionalities like alignment
from PyQt5.QtGui import QFont, QPixmap  # Font customization and image handling


# Define the main window class, inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.setWindowTitle("My First GUI")  # Set the window title
        self.setGeometry(400, 200, 650, 450)  # Define window position and size (x, y, width, height)
        self.setWindowIcon(QIcon("assets/images/icon.png"))  # Set the window icon

        # Create a QLabel (text label)
        label = QLabel("Welcome Cats Lovers😺", self)
        label.setFont(QFont("Roboto", 25))  # Set custom font and size
        label.setGeometry(0, 0, 700, 100)  # Define label size and position
        label.setStyleSheet("color: #141313;"  # Text color
                            "background-color: #09ab9b;"  # Background color
                            "font-weight: bold;"  # Bold text
                            "font_style: italic;"  # Italic style (Incorrect, should be 'font-style')
                            "text-decoration: underline;")  # Underline text

        # Alignment options (only one can be active at a time)
        # label.setAlignment(Qt.AlignTop)       # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom)    # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter)   # VERTICALLY CENTER
        # label.setAlignment(Qt.AlignRight)     # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter)   # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft)      # HORIZONTALLY LEFT

        # Combining alignments using bitwise OR '|'
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)       # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)    # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # CENTER & CENTER OR
        label.setAlignment(Qt.AlignCenter)  # CENTER both horizontally and vertically

        # Adding an image to the GUI
        img = QLabel(self)  # Create an image label
        img.setGeometry(0, 0, 600, 700)  # Set position and size
        pixmap = QPixmap("assets/images/img1.png")  # Load image
        img.setPixmap(pixmap)  # Set the image in QLabel
        img.setScaledContents(True)  # Enable image scaling

        # Adjust the image position dynamically
        img.setGeometry((self.width() - img.width()) // 2,
                        self.height() - img.height() // 2,
                        img.width(),
                        img.height())


# Main function to run the application
def main():
    app = QApplication(sys.argv)  # Initialize the application
    window = MainWindow()  # Create an instance of the main window
    window.show()  # Display the window
    sys.exit(app.exec_())  # Execute the application and clean up on exit


# Run the application only if this script is executed directly
if __name__ == '__main__':
    main()





