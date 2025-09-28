import sys, os, subprocess
from PySide6.QtGui import QPixmap
from model import PPTModel
from utils.converter import convert_ppt_to_images
from translator import TranslatorModel

class PPTController:
    def __init__(self, view):
        self.view = view
        self.model = None
        self.edited_ppt_path = None
        self.translator = TranslatorModel(src_lang="ja", tgt_lang="en")  # デフォ: 日本語→英語

        # イベント接続
        view.open_btn.clicked.connect(self.load_ppt)
        view.save_btn.clicked.connect(self.save_ppt)
        view.open_in_app_btn.clicked.connect(self.open_in_app)
        view.run_btn.clicked.connect(self.run_ai)
        view.view_box.currentIndexChanged.connect(self.update_slide_view)

    def load_ppt(self):
        from PySide6.QtWidgets import QFileDialog
        path, _ = QFileDialog.getOpenFileName(self.view, "PPTを選択", "", "PowerPoint Files (*.pptx)")
        if not path:
            return
        self.model = PPTModel(path)
        text = self.model.extract_text()
        self.view.input_text.setText(text)
        self.view.ppt_path_label.setText(f"PPTパス: {path}")
        self.view.slides_pix = convert_ppt_to_images(path)
        self.view.show_slide()

    def save_ppt(self):
        text = self.view.input_text.toPlainText()
        self.edited_ppt_path = self.model.save_with_texts(text)
        self.view.output_text.append(f"PPT出力完了: {self.edited_ppt_path}")
        if self.view.view_box.currentText() == "編集後PPT":
            self.view.slides_pix = convert_ppt_to_images(self.edited_ppt_path)
            self.view.show_slide()

    def run_ai(self):
        input_text = self.view.input_text.toPlainText()
        mode = self.view.mode_box.currentText()

        if mode == "翻訳":
            # UIで翻訳方向を取得（例: "日本語→英語" or "英語→日本語"）
            lang_mode = self.view.lang_box.currentText()
            if lang_mode == "日本語→英語":
                self.translator.set_languages("ja", "en")
            else:
                self.translator.set_languages("en", "ja")

            result = self.translator.translate_text(input_text)
            self.view.output_text.setText(result)
        else:
            # デモ用ダミー処理
            engine = self.view.engine_box.currentText()
            result = f"[{engine}] {mode} 処理結果：\n\n" + input_text.upper()
            self.view.output_text.setText(result)

    def open_in_app(self):
        if self.view.view_box.currentText() == "編集後PPT" and self.edited_ppt_path:
            file_to_open = self.edited_ppt_path
        else:
            file_to_open = self.model.ppt_path
        if sys.platform == "darwin":
            subprocess.run(["open", file_to_open])
        elif sys.platform == "win32":
            os.startfile(file_to_open)
        else:
            subprocess.run(["xdg-open", file_to_open])

    def update_slide_view(self):
        if self.view.view_box.currentText() == "元のPPT":
            self.view.slides_pix = convert_ppt_to_images(self.model.ppt_path)
        elif self.edited_ppt_path:
            self.view.slides_pix = convert_ppt_to_images(self.edited_ppt_path)
        self.view.show_slide()
