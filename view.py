from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QComboBox
)

class PPTView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PPT ローカル翻訳")
        self.setGeometry(200, 200, 1000, 600)

        self.model_path_label = QLabel("PPTパス: なし")
        self.slide_select = QComboBox()
        self.input_text = QTextEdit()
        self.output_text = QTextEdit()
        self.open_btn = QPushButton("📂 PPTを開く")
        self.translate_btn = QPushButton("🚀 翻訳")
        self.save_btn = QPushButton("💾 保存")

        # 元/翻訳後PPTを開くためのComboBox
        self.view_box = QComboBox()
        self.view_box.addItems(["元のPPT", "翻訳後PPT"])
        self.open_in_app_btn = QPushButton("💻 選択したPPTを開く")

        layout = QVBoxLayout()
        layout.addWidget(self.model_path_label)
        layout.addWidget(QLabel("スライド選択"))
        layout.addWidget(self.slide_select)
        layout.addWidget(QLabel("スライド内容"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.translate_btn)
        layout.addWidget(QLabel("翻訳結果"))
        layout.addWidget(self.output_text)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.view_box)
        layout.addWidget(self.open_in_app_btn)
        layout.addWidget(self.open_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
