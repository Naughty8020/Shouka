# ui_ppt_text.py
import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from ppt_text_extractor import extract_text

class PPTApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shouka PPT Reader")
        self.resize(400, 300)

        self.label = QLabel("PPTを選択してください")
        self.button = QPushButton("PPTを開く")
        self.button.clicked.connect(self.open_ppt)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def open_ppt(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "PPTを選択", "", "PowerPoint Files (*.pptx)")
        if file_path:
            text = extract_text(file_path)
            self.label.setText(text[:500] + "…")  # 長すぎる場合は一部だけ表示

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PPTApp()
    window.show()
    sys.exit(app.exec())
