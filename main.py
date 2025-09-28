import sys
from PySide6.QtWidgets import QApplication
from view import PPTView
from controller import PPTController

app = QApplication(sys.argv)
view = PPTView()
controller = PPTController(view)
view.show()
sys.exit(app.exec())
