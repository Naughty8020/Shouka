# ui_app_fontsafe.py
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QFileDialog, QComboBox, QScrollArea
)
from PySide6.QtGui import QPixmap
from pptx import Presentation
from ppt_text_extractor import extract_text  # 自作関数
from pptx.util import Inches

class PPTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shouka PPT AI Helper")
        self.setGeometry(200, 200, 1000, 600)

        self.ppt_path = ""
        self.slides_pix = []

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # ---------------- 左レイアウト ----------------
        left_layout = QVBoxLayout()
        self.open_btn = QPushButton("📂 PPTを開く")
        self.open_btn.clicked.connect(self.load_ppt)
        self.ppt_path_label = QLabel("PPTパス: なし")
        self.input_text = QTextEdit()
        self.show_slide_btn = QPushButton("PPT状態を表示")
        self.show_slide_btn.clicked.connect(self.show_slide)
        self.slide_label = QLabel()
        self.slide_label.setFixedHeight(300)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.slide_label)
        self.save_btn = QPushButton("💾 PPT出力")
        self.save_btn.clicked.connect(self.save_ppt)

        left_layout.addWidget(self.open_btn)
        left_layout.addWidget(self.ppt_path_label)
        left_layout.addWidget(QLabel("入力テキスト"))
        left_layout.addWidget(self.input_text)
        left_layout.addWidget(self.show_slide_btn)
        left_layout.addWidget(self.scroll)
        left_layout.addWidget(self.save_btn)

        # ---------------- 中央レイアウト ----------------
        center_layout = QVBoxLayout()
        self.mode_box = QComboBox()
        self.mode_box.addItems(["翻訳", "トーンアップ"])
        self.engine_box = QComboBox()
        self.engine_box.addItems(["クラウドAI", "ローカルAI"])
        self.run_btn = QPushButton("🚀 実行")
        self.run_btn.clicked.connect(self.run_ai)

        center_layout.addWidget(QLabel("モード選択"))
        center_layout.addWidget(self.mode_box)
        center_layout.addWidget(QLabel("AI エンジン"))
        center_layout.addWidget(self.engine_box)
        center_layout.addWidget(self.run_btn)

        # ---------------- 右レイアウト ----------------
        right_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        right_layout.addWidget(QLabel("出力結果"))
        right_layout.addWidget(self.output_text)

        # ---------------- 全体レイアウト ----------------
        layout.addLayout(left_layout, 4)
        layout.addLayout(center_layout, 1)
        layout.addLayout(right_layout, 4)

    # ---------------- PPT読み込み ----------------
    def load_ppt(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "PPTを選択", "", "PowerPoint Files (*.pptx)")
        if file_path:
            self.ppt_path = file_path
            self.ppt_path_label.setText(f"PPTパス: {file_path}")
            text = extract_text(file_path)
            self.input_text.setText(text)
            self.convert_ppt_to_images(file_path)

    # ---------------- スライド画像化（仮） ----------------
    def convert_ppt_to_images(self, ppt_path):
        self.slides_pix = ["slide1.png", "slide2.png"]  # 仮

    # ---------------- スライド表示（仮） ----------------
    def show_slide(self):
        if not self.slides_pix:
            return
        pix = QPixmap(self.slides_pix[0])
        self.slide_label.setPixmap(pix)

    # ---------------- AI実行（仮） ----------------
    def run_ai(self):
        mode = self.mode_box.currentText()
        engine = self.engine_box.currentText()
        input_text = self.input_text.toPlainText()
        result = f"[{engine}] {mode} 処理結果：\n\n" + input_text.upper()
        self.output_text.setText(result)

    # ---------------- フォントを保持してテキスト置き換え ----------------
    def replace_text_keep_font(self, shape, new_text):
        if not shape.has_text_frame:
            return
        paragraphs = shape.text_frame.paragraphs
        if paragraphs:
            # 最初の段落・ランに置き換え
            first_paragraph = paragraphs[0]
            if first_paragraph.runs:
                first_paragraph.runs[0].text = new_text
            else:
                first_paragraph.add_run().text = new_text
        else:
            # 段落がなければ追加
            p = shape.text_frame.add_paragraph()
            p.add_run().text = new_text

    # ---------------- 編集内容をスライドごとに保存 ----------------
    def save_ppt(self):
        if not self.ppt_path:
            return
        text = self.input_text.toPlainText()
        slides_text = text.split('--- Slide ')[1:]  # ['1 ---\n内容', '2 ---\n内容', ...]

        prs = Presentation(self.ppt_path)

        for i, slide in enumerate(prs.slides):
            if i >= len(slides_text):
                continue
            lines = slides_text[i].split('---\n', 1)[-1].strip()
            shapes_text = [s for s in slide.shapes if hasattr(s, "text") and s.has_text_frame]
            if shapes_text:
                self.replace_text_keep_font(shapes_text[0], lines)
            else:
                textbox = slide.shapes.add_textbox(
                    left=Inches(1), top=Inches(1), width=Inches(8), height=Inches(2)
                )
                self.replace_text_keep_font(textbox, lines)

        output_path = self.ppt_path.replace(".pptx", "_edited.pptx")
        prs.save(output_path)
        self.output_text.append(f"PPT出力完了: {output_path}")


# ---------------- アプリ起動 ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass

    window = PPTApp()
    window.show()
    sys.exit(app.exec())
