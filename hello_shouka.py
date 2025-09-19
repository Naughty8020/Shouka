import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello Shouka")
window.resize(300, 100)

label = QLabel("Hello, Shouka!")
label.setStyleSheet("font-size: 20px; color: blue;")

layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
