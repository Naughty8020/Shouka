# main.py
import sys
from PySide6.QtWidgets import QApplication
from view import PPTView
from controller import PPTController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass

    view = PPTView()
    controller = PPTController(view)
    view.show()
    sys.exit(app.exec())
