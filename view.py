from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QComboBox, QFileDialog
)

class PPTView(QMainWindow):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.setWindowTitle("PPT ローカル翻訳")
        self.setGeometry(200, 200, 1000, 600)

        self.model_path_label = QLabel("PPTパス: なし")
        self.slide_select = QComboBox()
        self.input_text = QTextEdit()
=======
        self.setWindowTitle("Shouka PPT AI Helper")
        self.setGeometry(200, 200, 1200, 700)
        self.slide_index = 0
        self.slides_pix = []

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # 左
        left_layout = QVBoxLayout()
        self.open_btn = QPushButton("📂資料をSHOUKAさせる")
        self.ppt_path_label = QLabel("資料のパス: なし")
        self.input_text = QTextEdit()
        self.save_btn = QPushButton("💾SHOUKAした資料を出力・作成")
        self.open_in_app_btn = QPushButton("💻資料を開く・確認")
        self.view_box = QComboBox()
        self.view_box.addItems(["元のPPT", "編集後PPT"])
        self.slide_label = QLabel()
        self.slide_label.setFixedHeight(300)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.slide_label)
        self.lang_box = QComboBox()
        self.lang_box.addItems(["日本語→英語", "英語→日本語"])

        left_layout.addWidget(self.open_btn)
        left_layout.addWidget(self.ppt_path_label)
        left_layout.addWidget(QLabel("テキスト"))
        left_layout.addWidget(self.input_text)
        left_layout.addWidget(self.save_btn)
        left_layout.addWidget(self.open_in_app_btn)
        left_layout.addWidget(QLabel("表示PPT選択"))
        left_layout.addWidget(self.view_box)
        left_layout.addWidget(QLabel("翻訳方向"))
        left_layout.addWidget(self.lang_box)

        # 中央
        center_layout = QVBoxLayout()
        self.mode_box = QComboBox()
        self.mode_box.addItems(["翻訳", "トーンアップ"])
        self.engine_box = QComboBox()
        self.engine_box.addItems(["クラウドAI", "ローカルAI"])
        self.run_btn = QPushButton("🚀 実行")
        center_layout.addWidget(QLabel("モード選択"))
        center_layout.addWidget(self.mode_box)
        center_layout.addWidget(QLabel("AI エンジン"))
        center_layout.addWidget(self.engine_box)
        center_layout.addWidget(self.run_btn)

        # 右
        right_layout = QVBoxLayout()
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642
        self.output_text = QTextEdit()
        self.open_btn = QPushButton("📂 PPTを開く")
        self.translate_btn = QPushButton("🚀 翻訳")
        self.save_btn = QPushButton("💾 保存")

<<<<<<< HEAD
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
        layout.addWidget(self.open_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
=======
        layout.addLayout(left_layout, 4)
        layout.addLayout(center_layout, 1)
        layout.addLayout(right_layout, 4)

    def show_slide(self):
        if not self.slides_pix:
            return
        pixmap = self.slides_pix[self.slide_index]
        self.slide_label.setPixmap(pixmap)
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642
