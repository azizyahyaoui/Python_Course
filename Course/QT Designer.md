# QT Designer: A Quick-Start Guide for Python Devs

## 🧭 Introduction

Qt Designer is a drag-and-drop GUI builder for Qt-based applications. It allows you to create `.ui` files visually, which you can convert into Python code using tools provided by PyQt5, PyQt6, or PySide6.

This guide walks you through:

- Installing and using Qt Designer
- Converting `.ui` and `.qrc` files
- Working with PyQt5, PyQt6, and PySide6
- Power user tips and PyCharm integration

---

## ⚙️ Qt Designer Setup

Qt Designer comes bundled with:

- **PyQt5:** via `pip install pyqt5-tools`
- **PySide6:** via `pip install PySide6`

To open Qt Designer:

```bash
# If using pyqt5-tools:
<path-to-python-scripts>/pyqt5-tools/designer.exe

# If using PySide6 (standalone download or system Qt):
<path-to-qt>/bin/designer.exe
```

---

## 🏗️ Creating UI Files

1. Open Qt Designer
2. Choose a Widget type (MainWindow, Dialog, Widget, etc.)
3. Design your GUI using drag-and-drop
4. Save the file as `your_ui_file.ui`

---

## 🔁 Convert `.ui` to `.py`

### ✅ PyQt5 / PyQt6

```bash
pyuic5 your_ui_file.ui -o your_ui_file.py
# or for PyQt6:
pyuic6 your_ui_file.ui -o your_ui_file.py
```

### ✅ PySide6

```bash
pyside6-uic your_ui_file.ui -o your_ui_file.py
```

Use `where pyside6-uic` (or `Get-Command pyside6-uic` in PowerShell) to find the full path.

---

## 🎨 Convert `.qrc` to `.py`

Use `.qrc` to bundle resources (images, icons):

```xml
<RCC>
  <qresource prefix="/icons">
    <file>myicon.png</file>
  </qresource>
</RCC>
```

### ✅ Convert with PySide6

```bash
pyside6-rcc your_resources.qrc -o your_resources_rc.py
```

Then in Python:

```python
import your_resources_rc  # just import to load resources
```

---

## 🚀 PyCharm Integration

### 🔧 Add External Tool for `.ui` Files

**File > Settings > Tools > External Tools**

#### Convert UI:

- **Name:** Convert UI (PySide6)
- **Program:**
  ```
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python310\Scripts\pyside6-uic.exe
  ```
- **Arguments:**
  ```
  "$FileName$" -o "$FileNameWithoutExtension$_ui.py"
  ```
- **Working Directory:**
  ```
  $FileDir$
  ```

#### Convert QRC:

- **Name:** Convert QRC (PySide6)
- **Program:**
  ```
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python310\Scripts\pyside6-rcc.exe
  ```
- **Arguments:**
  ```
  "$FileName$" -o "$FileNameWithoutExtension$_rc.py"
  ```
- **Working Directory:**
  ```
  $FileDir$
  ```

✅ Now right-click any `.ui` or `.qrc` file and run the External Tool.

---

## 🧪 Quick Python Example (PySide6)

```python
from PySide6.QtWidgets import QApplication, QWidget
from login_window_ui import Ui_Form

app = QApplication([])
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)
window.show()
app.exec()
```

---

## 💡 Tips & Tricks

- 🧠 **Use **********``********** in PyCharm External Tools** to avoid path issues.
- 🚀 Use `.qrc` to cleanly load icons and stylesheets.
- 🧼 Don’t edit the generated UI `.py` files — subclass them if you want logic separation.
- 🔁 Regenerate `.py` every time you update `.ui` or `.qrc`.

---

## 🧩 Signals & Slots

Signals and slots are the core communication mechanism in Qt. In PySide6 or PyQt, they allow widgets to send signals that other parts of your code can respond to.

### Example:
```python
from PySide6.QtWidgets import QPushButton

button = QPushButton("Click me")
button.clicked.connect(lambda: print("Button clicked!"))
```

You can also define your own signals using `Signal` from `PySide6.QtCore`:
```python
from PySide6.QtCore import QObject, Signal

class MyObject(QObject):
    custom_signal = Signal()

    def __init__(self):
        super().__init__()
        self.custom_signal.connect(self.handle_signal)

    def handle_signal(self):
        print("Custom signal received!")
```

---

## 🧵 @Slot Decorator Explained

In Qt (and PySide6), a **slot** is a function that can be connected to a **signal**.

When a signal is emitted (like when a button is clicked), the connected slot runs. Python’s dynamic nature means you usually don't need to decorate a method with `@Slot()` — but doing so gives you benefits:

### ✅ Why Use `@Slot()`?

1. **Performance Boost** — helps Qt optimize connections.
2. **Type Safety** — allows you to define expected argument types.
3. **Integration** — improves threading and signal behavior in advanced cases.

### 🧪 Example:
```python
from PySide6.QtCore import Slot, QObject, Signal

class MyObject(QObject):
    my_signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.my_signal.connect(self.handle_value)

    @Slot(int)
    def handle_value(self, val):
        print(f"Received value: {val}")
```

This is especially useful when using custom signals or working with threads.

---

## 🧱 Custom Widgets

If the default widgets aren’t enough, you can create your own by subclassing Qt widgets:

```python
from PySide6.QtWidgets import QLabel

class ClickableLabel(QLabel):
    def mousePressEvent(self, event):
        print("Label clicked")
```

You can promote widgets in Qt Designer to use custom widgets too (right-click > Promote).

---

## 🎨 Styling with QSS (Qt Style Sheets)

Use Qt Style Sheets (like CSS) to style widgets:
```css
QPushButton {
  background-color: #3498db;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
```
Apply in code:
```python
button.setStyleSheet("QPushButton { background-color: #3498db; color: white; }")
```
Or load from `.qss` file.

---

## 🧠 MVC Patterns in Qt

You can follow MVC (Model-View-Controller) by separating your UI into multiple layers:
- **UI Layer:** the `.ui` file and generated Python code
- **Logic Layer:** a Python class that controls user interaction
- **Data Layer:** where you handle data, databases, etc.

Helps keep your GUI projects scalable and clean.

---

## 📦 Packaging Your App (PyInstaller)

To package your Qt app as a standalone `.exe`:
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
Add any `.qrc`, `.ui`, or `.qss` files via `--add-data`:
```bash
--add-data "icons.qrc;icons"
```

Use `--noconsole` to hide the terminal window in GUI apps:
```bash
pyinstaller --onefile --noconsole main.py
```
---

